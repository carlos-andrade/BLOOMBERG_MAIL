#!/usr/bin/env python3
import json, os, sys, time, uuid
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen

ROOT=Path(__file__).resolve().parents[1]
CONFIG=ROOT/"config"/"watchdog.example.json"
EVENTS=ROOT/"runtime"/"events.jsonl"

def now(): return datetime.now(timezone.utc).isoformat()

def emit(source,event_type,severity="INFO",state="UP",payload=None,latency_ms=None):
    EVENTS.parent.mkdir(parents=True,exist_ok=True)
    event={"event_id":str(uuid.uuid4()),"observed_at_utc":now(),"source":source,"asset_class":"system","symbol":None,"session":None,"event_type":event_type,"severity":severity,"state":state,"latency_ms":latency_ms,"quality":"OK" if state=="UP" else "DEGRADED","payload":payload or {},"schema_version":"1.0"}
    with EVENTS.open("a",encoding="utf-8") as f: f.write(json.dumps(event,ensure_ascii=False)+"\n")
    print(json.dumps(event,ensure_ascii=False))

def probe(source,endpoint):
    started=time.monotonic()
    try:
        req=Request(endpoint,headers={"User-Agent":"BLOOMBERG_MAIL-WATCHDOG/1.0"})
        with urlopen(req,timeout=10) as response:
            emit(source,"HEARTBEAT","INFO","UP",{"http_status":response.status},round((time.monotonic()-started)*1000,2))
            return True
    except Exception as exc:
        emit(source,"SOURCE_UNAVAILABLE","HIGH","DOWN",{"error":str(exc)},round((time.monotonic()-started)*1000,2))
        return False

def main():
    if not CONFIG.exists():
        emit("watchdog","CONFIG_MISSING","CRITICAL","DOWN")
        return 2
    config=json.loads(CONFIG.read_text(encoding="utf-8"))
    emit("watchdog","WATCHDOG_HEARTBEAT")
    ok=True
    for source in config.get("sources",[]):
        if not source.get("enabled"): continue
        env_name=source.get("endpoint_env")
        endpoint=os.getenv(env_name or "")
        if endpoint: ok=probe(source["id"],endpoint) and ok
        else: emit(source["id"],"ADAPTER_NOT_CONFIGURED","MEDIUM","UNKNOWN",{"environment_variable":env_name})
    return 0 if ok else 1

if __name__=="__main__": sys.exit(main())
