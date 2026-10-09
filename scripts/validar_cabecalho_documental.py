#!/usr/bin/env python3
"""Valida o cabeçalho documental contra o modelo canônico do projeto."""
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
errors = []
count = 0

for path in ROOT.rglob("*.md"):
    if ".git" in path.parts:
        continue
    count += 1
    text = path.read_text(encoding="utf-8", errors="strict")
    if not text.startswith("---\n"):
        errors.append(f"{path.relative_to(ROOT)}: sem Front Matter")
        continue
    end = text.find("\n---\n", 4)
    if end < 0:
        errors.append(f"{path.relative_to(ROOT)}: Front Matter sem fechamento")
        continue
    fm = text[4:end]
    body = text[end + 5:].lstrip("\n")
    for key in REQUIRED:
        if not re.search(rf"(?m)^{re.escape(key)}\s*:", fm):
            errors.append(f"{path.relative_to(ROOT)}: campo ausente: {key}")
    h1 = re.match(r"^#\s+.+$", body)
    if not h1:
        errors.append(f"{path.relative_to(ROOT)}: título Markdown não está imediatamente após o Front Matter")
        continue
    metadata = body[h1.end():].split("\n\n", 1)[0]
    for label in VISIBLE:
        if not re.search(rf"(?m)^> \*\*{re.escape(label)}:\*\*", metadata):
            errors.append(f"{path.relative_to(ROOT)}: metadado visível ausente: {label}")
    for section in SECTIONS:
        if not re.search(rf"(?m)^## {re.escape(section)}\s*$", body):
            errors.append(f"{path.relative_to(ROOT)}: seção obrigatória ausente: {section}")
    if not re.search(r"(?m)^cadeia_autoridade:\s*.+$", fm):
        errors.append(f"{path.relative_to(ROOT)}: cadeia de autoridade vazia")
    if not re.search(r"(?m)^id_documento:\s*.+$", fm):
        errors.append(f"{path.relative_to(ROOT)}: ID documental vazio")

if errors:
    print("\n".join(errors))
    print(f"DOCUMENTOS_VERIFICADOS={count}")
    print(f"TOTAL_ERROS={len(errors)}")
    sys.exit(1)
print("CABECALHO_DOCUMENTAL_OK")
print(f"DOCUMENTOS_VERIFICADOS={count}")
print("FRONT_MATTER + METADADOS_VISÍVEIS + SEÇÕES_CANÔNICAS: OK")
