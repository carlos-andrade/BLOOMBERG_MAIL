#!/usr/bin/env python3
"""Valida o cabeçalho documental canônico do BLOOMBERG_MAIL."""
from pathlib import Path
import re, sys

ROOT=Path(__file__).resolve().parents[1]
REQUIRED=["projeto","repositorio","tipo_documento","fase","id_documento","titulo","status","versao","data_criacao","data_atualizacao","origem","autoridade_documental","cadeia_autoridade","rastreabilidade","escopo","objetivo","dependencias"]

errors=[]
for p in ROOT.rglob("*.md"):
    if ".git" in p.parts:
        continue
    text=p.read_text(encoding="utf-8",errors="strict")
    if not text.startswith("---\n"):
        errors.append(f"{p}: sem Front Matter")
        continue
    end=text.find("\n---\n",4)
    if end<0:
        errors.append(f"{p}: Front Matter sem fechamento")
        continue
    fm=text[4:end]
    for key in REQUIRED:
        if not re.search(rf"(?m)^{re.escape(key)}\s*:",fm):
            errors.append(f"{p}: campo ausente: {key}")
    if not re.search(r"(?m)^#\s+.+$",text[end+5:]):
        errors.append(f"{p}: título Markdown ausente")

if errors:
    print("\n".join(errors))
    print(f"TOTAL_ERROS={len(errors)}")
    sys.exit(1)
print("CABECALHO_DOCUMENTAL_OK")
