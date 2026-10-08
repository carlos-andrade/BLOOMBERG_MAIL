#!/usr/bin/env python3
"""Migra documentos Markdown para o cabeçalho documental canônico."""
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[1]
SKIP={".git"}
TODAY="2026-10-08"

def title_for(path,text):
    m=re.search(r"(?m)^#\s+(.+)$",text)
    if m: return m.group(1).strip()
    return path.stem.replace("_"," ").replace("-"," ").strip().title()

def phase_for(path):
    p=path.as_posix()
    if p.startswith("WATCHDOG/"): return "FASE-01-WATCHDOG"
    m=re.search(r"INGESTAO/(\d+)",p)
    if m: return f"FASE-{m.group(1).zfill(3)}-INGESTAO"
    if p.startswith("FONTES/"): return "FONTES"
    if p.startswith("GOVERNANCA/"): return "GOVERNANCA"
    return "N/A"

def tipo_for(path):
    p=path.as_posix()
    if p.startswith("GOVERNANCA/"): return "GOVERNANCA"
    if p.startswith("WATCHDOG/"): return "DOCUMENTO_TECNICO"
    return "DOCUMENTO"

for path in ROOT.rglob("*.md"):
    if any(part in SKIP for part in path.parts): continue
    text=path.read_text(encoding="utf-8")
    if text.startswith("---\n"): continue

    title=title_for(path,text)
    rel=path.relative_to(ROOT).as_posix()
    ident="BLOOMBERG-MAIL-"+re.sub(r"[^A-Za-z0-9]+","-",rel).strip("-").upper()

    header=f"""---
projeto: "BLOOMBERG_MAIL"
repositorio: "carlos-andrade/BLOOMBERG_MAIL"
tipo_documento: "{tipo_for(path)}"
fase: "{phase_for(path)}"
id_documento: "{ident}"
titulo: "{title.replace(chr(34), chr(39))}"
status: "IMPLEMENTADO"
versao: "1.0"
data_criacao: "{TODAY}"
data_atualizacao: "{TODAY}"
origem: "BLOOMBERG_MAIL"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA"
escopo: "{rel}"
objetivo: "Manter o documento identificável, rastreável, contextualizado e validável."
dependencias: "MODELO-PADRAO-CABECALHO"
---

# {title}

## Contexto Histórico

Documento histórico do projeto BLOOMBERG_MAIL integrado à governança documental central de carlos-andrade.

## Estado

IMPLEMENTADO — cabeçalho migrado para o padrão canônico.

## Evidências

Modelo canônico: Curioso-da-Internet-IA/CABEÇALHO/MODELO-PADRAO-CABECALHO.md.

## Validação

Cabeçalho, identificação documental e rastreabilidade foram normalizados.

## Resultado

O conteúdo original abaixo foi preservado.

## Próxima Ação

Atualizar versão, data e rastreabilidade em alterações relevantes.

---

"""
    path.write_text(header+text,encoding="utf-8")
    print(f"MIGRADO {rel}")
