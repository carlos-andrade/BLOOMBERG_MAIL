#!/usr/bin/env python3
"""Valida cabeçalhos documentais contra o modelo canônico do projeto."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "projeto", "repositorio", "tipo_documento", "fase", "id_documento",
    "titulo", "status", "versao", "data_criacao", "data_atualizacao",
    "origem", "autoridade_documental", "cadeia_autoridade",
    "rastreabilidade", "escopo", "objetivo", "dependencias",
]
VISIBLE = [
    "Projeto", "Repositório", "Tipo", "Fase", "ID", "Status", "Versão",
    "Criação", "Atualização", "Origem", "Autoridade", "Rastreabilidade",
]
SECTIONS = [
    "Contexto Histórico", "Estado", "Evidências", "Validação", "Resultado",
    "Próxima Ação",
]
CANONICAL_CHAIN = "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
errors = []
ids = {}
count = 0

for path in sorted(ROOT.rglob("*.md")):
    if ".git" in path.parts:
        continue
    count += 1
    rel = str(path.relative_to(ROOT))
    text = path.read_text(encoding="utf-8", errors="strict")
    if not text.startswith("---\n"):
        errors.append(f"{rel}: sem Front Matter")
        continue
    end = text.find("\n---\n", 4)
    if end < 0:
        errors.append(f"{rel}: Front Matter sem fechamento")
        continue

    fm = text[4:end]
    body = text[end + 5:].lstrip("\n")
    values = {}
    for key in REQUIRED:
        match = re.search(rf"(?m)^{re.escape(key)}\s*:\s*(.*)$", fm)
        if not match:
            errors.append(f"{rel}: campo ausente: {key}")
            continue
        value = match.group(1).strip().strip('"')
        values[key] = value
        if not value or value in {"N/A", "[]", "null"} and key not in {"fase", "dependencias"}:
            errors.append(f"{rel}: campo vazio/não aplicável sem justificativa: {key}")

    doc_id = values.get("id_documento", "")
    if doc_id:
        if doc_id in ids:
            errors.append(f"{rel}: id_documento duplicado: {doc_id} (também em {ids[doc_id]})")
        else:
            ids[doc_id] = rel

    if values.get("cadeia_autoridade") != CANONICAL_CHAIN:
        errors.append(f"{rel}: cadeia de autoridade fora do padrão canônico")

    h1 = re.match(r"^#[ \t]+[^\r\n]+", body)
    if not h1:
        errors.append(f"{rel}: título Markdown não está imediatamente após o Front Matter")
        continue

    for label in VISIBLE:
        if not re.search(rf"(?m)^> \*\*{re.escape(label)}:\*\*", body):
            errors.append(f"{rel}: metadado visível ausente: {label}")

    for section in SECTIONS:
        match = re.search(rf"(?m)^## {re.escape(section)}\s*$", body)
        if not match:
            errors.append(f"{rel}: seção obrigatória ausente: {section}")
        else:
            next_section = re.search(r"(?m)^## ", body[match.end():])
            section_body = body[match.end():match.end() + next_section.start()] if next_section else body[match.end():]
            if not re.search(r"\S", section_body):
                errors.append(f"{rel}: seção sem conteúdo: {section}")

if errors:
    print("\n".join(errors))
    print(f"DOCUMENTOS_VERIFICADOS={count}")
    print(f"TOTAL_ERROS={len(errors)}")
    sys.exit(1)

print("CABECALHO_DOCUMENTAL_OK")
print(f"DOCUMENTOS_VERIFICADOS={count}")
print("FRONT_MATTER + METADADOS_VISÍVEIS + SEÇÕES + IDs ÚNICOS + CADEIA DE AUTORIDADE: OK")
