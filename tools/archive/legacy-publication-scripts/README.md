# Publication reference scripts

| Script | Role |
|---|---|
| [apply_dataset_gap_updates.py](apply_dataset_gap_updates.py) | Applies dataset-field overrides and writes an audit CSV |
| [render_dataset_registry_table.py](render_dataset_registry_table.py) | Renders a controlled-vocabulary dataset table and supplementary CSV |
| [validate_table1_dataset_registry.py](validate_table1_dataset_registry.py) | Checks consistency between registry inputs and publication outputs |

These scripts resolve input paths relative to their parent directory, `tools/archive/`. Their input contract includes:

- `table1_dataset_resolution_and_class_counts.csv`;
- `latex_dataset_paper/tables/dataset_registry.tex`;
- `latex_dataset_paper/data/table1_dataset_registry_v1.0.0.csv` for validation.

Those input files are not included in the repository. The scripts contain dataset-specific assumptions and some commands overwrite their target files. They are not part of the supported graph checks or website build.

Use the [supported exporter](../../src/inspection_evidence/) for graph exports and the [reproducibility guide](../../../docs/REPRODUCIBILITY.md) for non-writing verification.
