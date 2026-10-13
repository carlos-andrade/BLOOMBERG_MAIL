#!/usr/bin/env python3
"""Incremental checks for BLOOMBERG_MAIL Markdown governance.

This audits against the central GOVERNANCA header contract without pretending
that the central proposal has been formally ratified. No files are rewritten.
"""
from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
CANONICAL_CHAIN = "PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO"
CONTROL_LABELS = ("SHA-256 (conteúdo canónico)", "Commit de referência (versão anterior)")
REQUIRED_LABELS = (
    "ID", "Projeto", "Repositório", "Tipo documental", "Fase", "Estado",
    "Versão", "SHA-256 (conteúdo canónico)", "Commit de referência (versão anterior)",
    "Data de criação", "Data de atualização", "Responsável", "Aprovador",
    "Origem", "Autoridade superior", "Cadeia de autoridade",
)
SKIP_DIRS = {".git", ".venv", "venv", "__pycache__"}
HASH_RE = re.compile(r"^[0-9a-f]{64}$")
COMMIT_RE = re.compile(r"^[0-9a-f]{40}$")


def canonical_document_bytes(text: str) -> bytes:
    """Normalize UTF-8/LF, drop BOM, and remove only the two control rows."""
    text = text.removeprefix("\ufeff").replace("\r\n", "\n").replace("\r", "\n")
    lines = text.splitlines(keepends=True)
    return "".join(
        line for line in lines
        if not any(re.search(rf"\*\*{re.escape(label)}\*\*", line) for label in CONTROL_LABELS)
    ).encode("utf-8")


def parse_metadata(text: str) -> dict[str, str]:
    metadata: dict[str, str] = {}
    in_table = False
    for line in text.splitlines():
        if line.strip() == "| Campo | Valor |":
            in_table = True
            continue
        if in_table:
            if not line.strip().startswith("|"):
                if metadata:
                    break
                continue
            match = re.match(r"^\|\s*\*\*(.+?)\*\*\s*\|\s*(.*?)\s*\|\s*$", line.strip())
            if match:
                metadata[match.group(1).strip()] = match.group(2).strip()
    return metadata


def markdown_files(root: Path) -> list[Path]:
    return sorted(
        p for p in root.rglob("*.md")
        if not any(part in SKIP_DIRS for part in p.parts)
    )


def validate_markdown_links(root: Path, files: list[Path]) -> list[str]:
    errors = []
    for path in files:
        text = path.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            target = target.split("#", 1)[0].strip()
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            parsed = urlparse(target)
            if parsed.scheme or parsed.netloc:
                continue
            resolved = (path.parent / Path(unquote(target))).resolve()
            try:
                resolved.relative_to(root.resolve())
            except ValueError:
                errors.append(f"{path.relative_to(root)}: link escapes repository: {target}")
                continue
            if not resolved.exists():
                errors.append(f"{path.relative_to(root)}: missing relative link: {target}")
    return errors


def scan_document_ids(root: Path, files: list[Path]) -> tuple[list[str], int]:
    errors = []
    owners: dict[str, Path] = {}
    count = 0
    for path in files:
        meta = parse_metadata(path.read_text(encoding="utf-8"))
        doc_id = meta.get("ID", "").strip()
        if not doc_id:
            continue
        count += 1
        if doc_id in owners:
            errors.append(
                f"{path.relative_to(root)}: duplicate ID {doc_id} "
                f"(also {owners[doc_id].relative_to(root)})"
            )
        else:
            owners[doc_id] = path
    return errors, count


def validate_document(root: Path, path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    errors = []
    if not re.match(r"^#\s+\S", text):
        errors.append("missing H1 title at file start")
    meta = parse_metadata(text)
    for label in REQUIRED_LABELS:
        if label not in meta:
            errors.append(f"missing metadata: {label}")
    if not meta:
        return errors
    if not meta.get("ID", "").strip():
        errors.append("ID empty")
    if meta.get("Cadeia de autoridade", "") != CANONICAL_CHAIN:
        errors.append("authority chain differs from canonical value")
    digest = meta.get("SHA-256 (conteúdo canónico)", "")
    calculated = hashlib.sha256(canonical_document_bytes(text)).hexdigest()
    if not HASH_RE.fullmatch(digest):
        errors.append("canonical SHA-256 missing/invalid")
    elif digest != calculated:
        errors.append(f"canonical SHA-256 mismatch: expected {calculated}")
    commit = meta.get("Commit de referência (versão anterior)", "")
    match = re.search(r"/commit/([0-9a-f]{40})(?:$|[)#?])", commit)
    if not commit.startswith("N/A — documento inicial") and not match:
        errors.append("previous reference must be a GitHub commit URL or N/A — documento inicial")
    for label in (
        "Projeto", "Repositório", "Tipo documental", "Fase", "Estado", "Versão",
        "Data de criação", "Data de atualização", "Responsável", "Aprovador",
        "Origem", "Autoridade superior",
    ):
        if not meta.get(label, "").strip():
            errors.append(f"empty metadata value: {label}")
    for section in (
        "Contexto Histórico", "Estado", "Evidências", "Validação", "Resultado", "Próxima Ação",
    ):
        match_section = re.search(rf"(?m)^## {re.escape(section)}\s*$", text)
        if not match_section:
            errors.append(f"missing section: {section}")
        else:
            next_section = re.search(r"(?m)^## ", text[match_section.end():])
            part = text[match_section.end():match_section.end() + next_section.start()] if next_section else text[match_section.end():]
            if not re.search(r"\S", part):
                errors.append(f"empty section: {section}")
    return errors


def main() -> int:
    files = markdown_files(ROOT)
    failures = []
    conforming = 0
    for path in files:
        errors = validate_document(ROOT, path)
        if errors:
            failures.append((path, errors))
        else:
            conforming += 1
    id_errors, id_count = scan_document_ids(ROOT, files)
    link_errors = validate_markdown_links(ROOT, files)
    findings_count = sum(len(items) for _, items in failures) + len(id_errors) + len(link_errors)
    print(f"MARKDOWN_FILES={len(files)}")
    print(f"DOCUMENTS_PASS={conforming}")
    print(f"DOCUMENTS_WITH_FINDINGS={len(failures)}")
    print(f"IDS_FOUND={id_count}")
    print(f"ID_FINDINGS={len(id_errors)}")
    print(f"RELATIVE_LINK_FINDINGS={len(link_errors)}")
    print(f"TOTAL_FINDINGS={findings_count}")
    for path, errs in failures:
        for err in errs:
            print(f"{path.relative_to(ROOT)}: {err}")
    for err in id_errors + link_errors:
        print(err)
    if findings_count:
        print("GOVERNANCE_AUDIT=FINDINGS_PRESENT")
        return 1
    print("GOVERNANCE_AUDIT=PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
