"""Repository-level validation for a safe, reproducible public release."""

from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass, field
from pathlib import Path

from .exporter import load_config
from .vault import duplicate_titles, iter_notes, resolve_edges, scalar


MACHINE_PATH_RE = re.compile(r"/(?:home|Users)/[A-Za-z0-9._-]{2,}/|[A-Za-z]:\\\\(?:Users|Documents|Desktop)\\\\", re.IGNORECASE)
SENSITIVE_NAMES = re.compile(r"(?:^|[-_.])(secret|credential|token|password|private[-_]?key)(?:[-_.]|$)", re.IGNORECASE)
SECRET_CONTENT_PATTERNS = (
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"\bgh[pousr]_[A-Za-z0-9]{36,255}\b"),
    re.compile(r"\bsk-[A-Za-z0-9]{20,}\b"),
)


@dataclass
class ValidationReport:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    metrics: dict[str, int] = field(default_factory=dict)

    @property
    def ok(self) -> bool:
        return not self.errors


def _public_files(root: Path):
    excluded_roots = {
        root / ".git",
        root / "workspace",
        root / ".venv",
        root / ".conda",
        root / "venv",
        root / ".cache",
        root / "build",
        root / "dist",
        root / "website" / "node_modules",
        root / "website" / "dist",
        root / "website" / "coverage",
    }
    for directory, subdirectories, filenames in os.walk(root):
        current = Path(directory)
        subdirectories[:] = sorted(
            name for name in subdirectories
            if current / name not in excluded_roots
            and name not in {"__pycache__", ".pytest_cache"}
            and not name.endswith(".egg-info")
        )
        for name in sorted(filenames):
            path = current / name
            if path.is_file():
                yield path


def _parse_skill_frontmatter(path: Path) -> tuple[str, str] | None:
    text = path.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    name = ""
    description = ""
    for line in text[4:end].splitlines():
        if line.startswith("name:"):
            name = line.split(":", 1)[1].strip().strip("\"'")
        elif line.startswith("description:"):
            description = line.split(":", 1)[1].strip().strip("\"'")
    return name, description


def _validate_vendor_provenance(root: Path, report: ValidationReport) -> None:
    vendor_root = root / "tools" / "vendor" / "agent-skills"
    manifest_path = vendor_root / "provenance.json"
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        report.errors.append(f"invalid vendor provenance manifest: {exc}")
        return

    sources = manifest.get("sources") if isinstance(manifest, dict) else None
    if not isinstance(sources, list) or not sources:
        report.errors.append("vendor provenance manifest must contain a non-empty sources list")
        return

    covered: set[str] = set()
    duplicate_entries: set[str] = set()
    for index, source in enumerate(sources):
        if not isinstance(source, dict):
            report.errors.append(f"vendor provenance source {index} is not an object")
            continue
        source_id = source.get("id")
        repository = source.get("repository")
        license_name = source.get("license")
        skills = source.get("skills")
        if not isinstance(source_id, str) or not source_id:
            report.errors.append(f"vendor provenance source {index} lacks an id")
        if not isinstance(repository, str) or not repository.startswith("https://"):
            report.errors.append(f"vendor provenance source {source_id or index} lacks an HTTPS repository URL")
        if not isinstance(license_name, str) or not license_name:
            report.errors.append(f"vendor provenance source {source_id or index} lacks a license")
        if not isinstance(skills, list) or not all(isinstance(skill, str) and skill for skill in skills):
            report.errors.append(f"vendor provenance source {source_id or index} has an invalid skills list")
            continue
        for skill in skills:
            if skill in covered:
                duplicate_entries.add(skill)
            covered.add(skill)

    actual = {
        path.name
        for path in vendor_root.iterdir()
        if path.is_dir() and (path / "SKILL.md").is_file()
    }
    missing = sorted(actual - covered)
    nonexistent = sorted(covered - actual)
    if duplicate_entries:
        report.errors.append("vendored skills mapped more than once: " + ", ".join(sorted(duplicate_entries)))
    if missing:
        report.errors.append("vendored skills missing provenance: " + ", ".join(missing))
    if nonexistent:
        report.errors.append("provenance entries without vendored skills: " + ", ".join(nonexistent))
    report.metrics["vendored_skills"] = len(actual)
    report.metrics["vendored_skills_with_provenance"] = len(actual & covered)


def validate_repository(root: Path) -> ValidationReport:
    root = root.resolve()
    report = ValidationReport()
    required = [
        ".gitignore",
        "README.md",
        "LICENSE",
        "CITATION.cff",
        "CONTRIBUTING.md",
        "SECURITY.md",
        "THIRD_PARTY_NOTICES.md",
        "tools/config/repository.json",
        "evidence/graph/vault",
        "evidence/graph/schema",
        "evidence/graph/exports",
        "evidence/review/protocol",
        "evidence/review/publication",
        "tools/archive",
        "docs/LOCAL_WORKSPACE.md",
        "docs/licenses/MIT.txt",
        "docs/licenses/CC-BY-4.0.md",
        "tools/src/inspection_evidence",
        "tools/tests",
        "tools/skills",
        "tools/vendor/agent-skills/PROVENANCE.md",
        "tools/vendor/agent-skills/provenance.json",
        ".github/workflows/validate.yml",
    ]
    for item in required:
        if not (root / item).exists():
            report.errors.append(f"missing required path: {item}")
    if report.errors:
        return report

    try:
        config = load_config(root)
    except (OSError, json.JSONDecodeError, KeyError) as exc:
        report.errors.append(f"invalid tools/config/repository.json: {exc}")
        return report

    paths = config.get("paths", {}) if isinstance(config, dict) else {}
    for key in ("vault", "exports", "review", "publication"):
        value = paths.get(key) if isinstance(paths, dict) else None
        if not isinstance(value, str) or not value:
            report.errors.append(f"invalid configured path: {key}")
            continue
        target = (root / value).resolve()
        if not target.is_relative_to(root) or not target.is_dir():
            report.errors.append(f"configured {key} must identify an existing repository directory: {value}")
    if report.errors:
        return report

    for schema in sorted((root / "evidence" / "graph" / "schema").glob("*.json")):
        try:
            json.loads(schema.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            report.errors.append(f"invalid JSON schema {schema.relative_to(root)}: {exc}")

    machine_paths: list[str] = []
    sensitive: list[str] = []
    embedded_credentials: list[str] = []
    oversized: list[str] = []
    for path in _public_files(root):
        relative = path.relative_to(root).as_posix()
        if path.stat().st_size > 50 * 1024 * 1024:
            oversized.append(relative)
        if SENSITIVE_NAMES.search(path.name) and path.name not in {"SECURITY.md"}:
            sensitive.append(relative)
        if path.suffix.lower() in {".md", ".py", ".json", ".yml", ".yaml", ".toml", ".txt", ".csv", ".tex"}:
            text = path.read_text(encoding="utf-8", errors="replace")
            if MACHINE_PATH_RE.search(text):
                machine_paths.append(relative)
            if any(pattern.search(text) for pattern in SECRET_CONTENT_PATTERNS):
                embedded_credentials.append(relative)
    if machine_paths:
        report.errors.append("machine-specific absolute paths: " + ", ".join(machine_paths[:20]))
    if sensitive:
        report.errors.append("sensitive-looking filenames: " + ", ".join(sensitive[:20]))
    if embedded_credentials:
        report.errors.append("possible embedded credential material: " + ", ".join(embedded_credentials[:20]))
    if oversized:
        report.errors.append("files larger than 50 MiB: " + ", ".join(oversized))

    gitignore = (root / ".gitignore").read_text(encoding="utf-8", errors="replace")
    if "workspace/" not in gitignore.splitlines():
        report.errors.append(".gitignore does not exclude the local workspace")

    _validate_vendor_provenance(root, report)

    skills_dir = root / "tools" / "skills"
    for skill_dir in sorted(path for path in skills_dir.iterdir() if path.is_dir()):
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            report.errors.append(f"project skill missing SKILL.md: {skill_dir.name}")
            continue
        parsed = _parse_skill_frontmatter(skill_md)
        if not parsed:
            report.errors.append(f"project skill has invalid frontmatter: {skill_dir.name}")
            continue
        name, description = parsed
        if name != skill_dir.name:
            report.errors.append(f"project skill name mismatch: {skill_dir.name} declares {name!r}")
        if not description:
            report.errors.append(f"project skill missing description: {skill_dir.name}")
        if len(skill_md.read_text(encoding="utf-8").splitlines()) > 500:
            report.errors.append(f"project skill SKILL.md exceeds 500 lines: {skill_dir.name}")
        if not (skill_dir / "agents" / "openai.yaml").exists():
            report.warnings.append(f"project skill lacks agents/openai.yaml: {skill_dir.name}")

    vault = root / config["paths"]["vault"]
    notes = iter_notes(vault)
    edges = resolve_edges(notes)
    resolution = {kind: sum(edge.resolution == kind for edge in edges) for kind in ("resolved", "ambiguous", "unresolved")}
    duplicates = duplicate_titles(notes)
    report.metrics.update({
        "notes": len(notes),
        "edges": len(edges),
        "resolved_edges": resolution["resolved"],
        "ambiguous_edges": resolution["ambiguous"],
        "unresolved_edges": resolution["unresolved"],
        "duplicate_titles": len(duplicates),
    })
    if resolution["unresolved"]:
        examples = [f"{edge.source_id} -> {edge.target_title}" for edge in edges if edge.resolution == "unresolved"][:10]
        report.errors.append(f"unresolved wikilinks ({resolution['unresolved']}): " + "; ".join(examples))
    if resolution["ambiguous"]:
        examples = [f"{edge.source_id} -> {edge.target_title}" for edge in edges if edge.resolution == "ambiguous"][:10]
        report.errors.append(f"ambiguous wikilinks ({resolution['ambiguous']}): " + "; ".join(examples))
    if duplicates:
        report.warnings.append(f"duplicate display titles: {len(duplicates)}")

    datasets = [note for note in notes if note.node_type == "Datasets" and note.path.name != "Dataset Source Links.md"]
    public = [note for note in datasets if "Public" in Path(note.relative_path).parts]
    missing_license = [note for note in public if not (scalar(note.metadata.get("license")) or scalar(note.metadata.get("licenses")))]
    missing_access = [note for note in public if not scalar(note.metadata.get("access"))]
    report.metrics.update({
        "dataset_notes": len(datasets),
        "public_dataset_notes": len(public),
        "public_datasets_missing_license_evidence": len(missing_license),
        "public_datasets_missing_access_detail": len(missing_access),
    })
    if missing_license:
        report.warnings.append(f"public dataset notes missing license evidence: {len(missing_license)}")
    if missing_access:
        report.warnings.append(f"public dataset notes missing access detail: {len(missing_access)}")
    if "Repository contributors" in (root / "CITATION.cff").read_text(encoding="utf-8"):
        report.warnings.append("CITATION.cff still uses the contributor entity; replace it before the archival release")
    return report


def format_report(report: ValidationReport) -> str:
    lines = ["Repository validation: " + ("PASS" if report.ok else "FAIL")]
    if report.metrics:
        lines.append("Metrics:")
        lines.extend(f"  - {key}: {value}" for key, value in sorted(report.metrics.items()))
    if report.errors:
        lines.append("Errors:")
        lines.extend(f"  - {item}" for item in report.errors)
    if report.warnings:
        lines.append("Warnings:")
        lines.extend(f"  - {item}" for item in report.warnings)
    return "\n".join(lines)
