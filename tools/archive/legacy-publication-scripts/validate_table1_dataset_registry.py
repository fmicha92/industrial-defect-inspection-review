#!/usr/bin/env python3
"""Validate Table 1 against its source and versioned supplementary registry."""

from __future__ import annotations

import csv
import re
from pathlib import Path

import render_dataset_registry_table as registry


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_TASKS = set(registry.TASK_LABELS.values())
COUNT_CODE_PATTERN = re.compile(
    r"\b(?:N(?:lab|ann|mask|real|syn|cls|det|source|patch|aug)?|"
    r"M(?:aug)?|K(?:prod|pattern|texture)?|tr-n|val-n|te-n|te-a)\s*="
)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def table_rows() -> list[list[str]]:
    rows: list[list[str]] = []
    for line in registry.TABLE_PATH.read_text(encoding="utf-8").splitlines():
        if "citep{" not in line or line.lstrip().startswith("%"):
            continue
        cells = line.strip().removesuffix(r"\\").strip().split(" & ")
        if len(cells) != 6:
            raise AssertionError(f"Table row does not have six columns: {line}")
        rows.append(cells)
    return rows


def main() -> None:
    source = read_csv(registry.SOURCE_CSV)
    supplement = read_csv(registry.SUPPLEMENT_PATH)
    rows = table_rows()

    source_names = [record["dataset_name"] for record in source]
    supplement_names = [record["dataset_name"] for record in supplement]
    table_names = [registry.dataset_key(cells[0]) for cells in rows]

    assert len(source_names) == 61, "Source audit must contain 61 rows"
    assert len(set(source_names)) == 61, "Source audit contains duplicate names"
    assert source_names == supplement_names == table_names, (
        "Source, supplement, and LaTeX table must have the same 61 rows in order"
    )
    assert all(len(cells) == 6 for cells in rows), "Every dataset row must have six columns"

    table_text = registry.TABLE_PATH.read_text(encoding="utf-8")
    assert "Dataset & Task(s) & Annotation & Modality & Resolution & Samples/classes" in table_text
    assert "Cross-domain industrial benchmarks" in table_text
    assert "Multi-industry anomaly" not in table_text
    assert table_text.count(registry.NOTES_BEGIN) == 1
    assert table_text.count(registry.NOTES_END) == 1

    forbidden_resolution_terms = ("preprocess", "model input", "paper downsample")
    by_name = {record["dataset_name"]: record for record in supplement}

    for cells in rows:
        name = registry.dataset_key(cells[0])
        task_terms = {term.strip() for term in cells[1].split(";")}
        assert task_terms <= EXPECTED_TASKS, f"Uncontrolled task term for {name}: {task_terms}"
        assert cells[1] == registry.TASKS[name]
        assert cells[2] == registry.ANNOTATIONS[name]
        assert cells[4] == registry.RESOLUTIONS[name]
        assert cells[5] == registry.SAMPLE_SUMMARIES[name]
        assert not COUNT_CODE_PATTERN.search(cells[5]), (
            f"Compact count code remains for {name}: {cells[5]}"
        )
        assert any(char.isdigit() for char in cells[5]), f"Missing counts for {name}"
        assert any(
            term in cells[5].lower()
            for term in (
                "class", "type", "pattern", "condition", "product", "label",
                "binary", "defect", "level", "category", "anomaly", "foreground",
            )
        ), f"Missing label semantics for {name}: {cells[5]}"
        assert not any(term in cells[4].lower() for term in forbidden_resolution_terms)

        record = by_name[name]
        assert record["registry_version"] == registry.REGISTRY_VERSION
        assert record["metadata_snapshot_date"] == registry.SNAPSHOT_DATE
        assert record["task_controlled"] == cells[1]
        assert all(value.strip() for value in record.values()), f"Empty supplementary field for {name}"
        if "Anomaly detection" in task_terms:
            assert record["normal_only_training"] != "not applicable"
        if record["release_discrepancy"] != "none identified":
            assert registry.DAGGER in cells[5], f"Missing discrepancy marker for {name}"

    print(
        "Validated 61 Table 1 rows, six columns, full controlled task terms, "
        "plain-language counts, native/released resolutions, discrepancy markers, "
        "and Supplementary Data S1."
    )


if __name__ == "__main__":
    main()
