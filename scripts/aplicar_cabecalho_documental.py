#!/usr/bin/env python3
"""Aplica o cabeçalho documental canônico sem remover conteúdo existente."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SKIP = {".git"}
TODAY = "2026-10-09"
REQUIRED = [
    "projeto", "repositorio", "tipo_documento", "fase", "id_documento",
    "titulo", "status", "versao", "data_criacao", "data_atualizacao",
    "origem", "autoridade_documental", "cadeia_autoridade",
    "rastreabilidade", "escopo", "objetivo", "dependencias",
]

def quote(value):
    return '"' + str(value).replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ") + '"'

def parse_front_matter(text):
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end < 0:
        return None, text
    fm = text[4:end]
    values = {}
    for line in fm.splitlines():
        match = re.match(r"^([a-z_]+):\\s*(.*)$", line)
        if match:
            values[match.group(1)] = match.group(2).strip().strip('"')
    return values, text[end + 5:]

def title_for(path, body):
    match = re.search(r"(?m)^#\\s+(.+)$", body)
    return match.group(1).strip() if match else path.stem.replace("_", " ").replace("-", " ").title()

def phase_for(path):
    p = path.as_posix()
    if p.startswith("WATCHDOG/"):
        return "FASE-01-WATCHDOG"
    match = re.search(r"INGESTAO/(\\d+)", p)
    if match:
        return f"FASE-{match.group(1).zfill(3)}-INGESTAO"
    if p.startswith("FONTES/"):
        return "FONTES"
    if p.startswith("GOVERNANCA/"):
        return "GOVERNANCA"
    return "N/A"

def tipo_for(path):
    p = path.as_posix()
    if p.startswith("GOVERNANCA/"):
        return "GOVERNANCA"
    if p.startswith("WATCHDOG/"):
        return "DOCUMENTO_TECNICO"
    return "DOCUMENTO"

def visible_header(v):
    labels = [
        ("Projeto", "projeto"), ("Repositório", "repositorio"),
        ("Tipo", "tipo_documento"), ("Fase", "fase"), ("ID", "id_documento"),
        ("Status", "status"), ("Versão", "versao"), ("Criação", "data_criacao"),
        ("Atualização", "data_atualizacao"), ("Origem", "origem"),
        ("Autoridade", "autoridade_documental"), ("Rastreabilidade", "rastreabilidade"),
    ]
    lines = ["> **Projeto:** " + v.get("projeto", "N/A")]
    for label, key in labels[1:]:
        lines.append(f"> **{label}:** {v.get(key, 'N/A')}")
    return "\n".join(lines) + "\n"

def add_visible_header(body, values):
    h1 = re.search(r"(?m)^#\\s+.+$", body)
    if not h1:
        title = values.get("titulo", "Documento sem título")
        body = f"# {title}\n\n" + body.lstrip()
        h1 = re.search(r"(?m)^#\\s+.+$", body)
    after = h1.end()
    tail = body[after:]
    # Não duplicar o bloco se já houver os campos principais.
    if re.search(r"(?m)^> \\*\\*Projeto:\\*\\*", tail) and re.search(r"(?m)^> \\*\\*Rastreabilidade:\\*\\*", tail):
        return body
    return body[:after] + "\n\n" + visible_header(values) + body[after:]

for path in ROOT.rglob("*.md"):
    if any(part in SKIP for part in path.parts):
        continue
    original = path.read_text(encoding="utf-8")
    values, body = parse_front_matter(original)
    rel = path.relative_to(ROOT).as_posix()

    if values is None:
        title = title_for(path, original)
        ident = "BLOOMBERG-MAIL-" + re.sub(r"[^A-Za-z0-9]+", "-", rel).strip("-").upper()
        values = {
            "projeto": "BLOOMBERG_MAIL",
            "repositorio": "carlos-andrade/BLOOMBERG_MAIL",
            "tipo_documento": tipo_for(path),
            "fase": phase_for(path),
            "id_documento": ident,
            "titulo": title,
            "status": "IMPLEMENTADO",
            "versao": "1.0",
            "data_criacao": TODAY,
            "data_atualizacao": TODAY,
            "origem": "BLOOMBERG_MAIL",
            "autoridade_documental": "GOVERNANÇA",
            "cadeia_autoridade": "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO",
            "rastreabilidade": "MODELO-PADRAO-CABECALHO — Curioso-da-Internet-IA",
            "escopo": rel,
            "objetivo": "Manter o documento identificável, rastreável, contextualizado e validável.",
            "dependencias": "MODELO-PADRAO-CABECALHO",
        }
        fm = "\n".join(f"{key}: {quote(value)}" for key, value in values.items())
        body = f"---\n{fm}\n---\n\n# {title}\n\n" + original.lstrip()

    body = add_visible_header(body, values)
    updated = "---\n" + "\n".join(
        f"{key}: {quote(values.get(key, 'N/A'))}" for key in REQUIRED
    ) + "\n---\n\n" + body.lstrip() if not original.startswith("---\n") else None

    if updated is None:
        # Preserve the existing YAML and all existing document content.
        end = original.find("\n---\n", 4)
        fm = original[4:end]
        original_body = original[end + 5:]
        updated = original[:end + 5] + "\n\n" + add_visible_header(original_body, values) if not re.search(r"(?m)^> \\*\\*Projeto:\\*\\*", original_body) else original

    if updated != original:
        path.write_text(updated, encoding="utf-8")
        print(f"PADRONIZADO {rel}")
