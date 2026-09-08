# Paper Note Template

Use this template when creating a full paper note. Only use information from the
actual paper/source text and explicit metadata for that paper. Do not fill gaps
from memory or model training data. Remove fields that are truly irrelevant, but
write unknown important fields as `not reported` and irrelevant fields as `not
applicable`. Write note prose as standalone scholarly content: do not describe
why material exists in the note system, where it is stored, or how it was
processed. Keep source paths and processing details in frontmatter fields.

```markdown
---
title: ""
aliases: []
paper_key:
paper_type: research
year:
venue:
authors: []
status: unread
processed_at:
topics: []
tasks: []
domains: []
application_area:
datasets: []
dataset_sizes: []
splits: []
modalities: []
methods: []
model_family: []
architectures: []
losses: []
optimizers: []
training_regime:
augmentation: []
synthetic_data:
metrics: []
primary_metric:
metric_definitions: []
baselines: []
benchmarks: []
evaluation_protocol:
parameters:
compute:
hardware:
training_time:
inference_cost:
url:
pdf:
code:
data:
doi:
arxiv:
related_papers: []
related_concepts: []
related_methods: []
related_datasets: []
related_domains: []
related_tasks: []
related_benchmarks: []
concept_notes_created_or_updated: []
source_file:
preprocessed_input:
extracted_text:
artifact_status:
tags:
  - paper
---

# {{title}}

## Summary

- 

## Paper Type

- Type:
- Why:

## Problem

- Task:
- Setting:
- Inputs:
- Outputs:
- Motivation:
- Assumptions:

## Contribution

- Claimed:
- Shown:
- Inferred:

## Method

- Core idea:
- Architecture / algorithm:
- Objective / loss:
- Optimization:
- Training data:
- Data pipeline:
- Augmentation / synthesis:
- Inference:
- Complexity / deployment constraints:

## ML / DL Extraction

### Task Formulation

- Input modality:
- Output target:
- Supervision:
- Objective:

### Model And Training

- Model family:
- Architecture:
- Parameters:
- Pretraining:
- Fine-tuning:
- Losses:
- Optimizer:
- Hyperparameters:
- Seeds:
- Training compute:

### Data

- Datasets:
- Data source:
- Dataset size:
- Labels / annotations:
- Splits:
- Preprocessing:
- Augmentation:
- Synthetic data:
- Leakage checks:
- License:

### Evaluation

- Protocol:
- Used performance metrics:
- Primary metric:
- Metric definitions:
- Metric direction / units:
- Baselines:
- Benchmarks:
- Statistical tests:
- Failure cases:

## Evidence

### Experimental Setup

- Datasets:
- Splits:
- Baselines:
- Used performance metrics:
- Compute:
- Hardware:
- Training time:
- Inference cost:

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| | | | | | | |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| | | | higher/lower | | |

### Ablations

- 

## Dataset / Benchmark Details

- Source:
- Collection:
- Annotation:
- Size:
- Splits:
- Modalities:
- License:
- Leakage risks:
- Bias / coverage:
- Maintenance:

## Review / Survey Details

- Scope:
- Inclusion criteria:
- Taxonomy:
- Major themes:
- Gaps:

## Limitations

- Stated:
- Inferred:

## Reproducibility

- Code:
- Data:
- Hyperparameters:
- Random seeds:
- Environment:
- Checkpoints / models:
- Exact preprocessing:
- Artifact status:

## Systems Details

- Hardware / software stack:
- Latency:
- Throughput:
- Memory:
- Scaling:
- Deployment assumptions:
- Cost:
- Failure modes:

## Connections

### Graph Hubs

- Tasks:
- Methods:
- Optimizers:
- Datasets:
- Benchmarks:
- Domains:
- Metrics:
- Concepts:
- Dataset-domain links:

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| | Builds on / Contrasts with / Shares dataset / Shares method / Shares task / Follow-up reading | |

### Backlinks Updated

- 

### Concept Notes Created Or Updated

| Concept note | Action | Explanation source |
|---|---|---|
| | Created / Updated | Paper text / linked papers / inferred |

## Questions

- 
```

## Extraction Checklist

- Source integrity: use only the paper/source text and explicit paper metadata; never invent missing details.
- Metadata: title, aliases, paper key, authors, year, venue, DOI/arXiv, URLs, source/preprocessed paths.
- Paper type: research, review, dataset, benchmark, systems, position, other.
- ML specifics: task, input/output, model family, architecture, loss, optimizer, training setup, data, synthetic data/augmentation, used performance metrics, baselines, ablations.
- Evidence: main numbers, comparison targets, metric direction/units, uncertainty, statistical testing if reported.
- Reliability: code/data, splits, leakage, licensing, compute, hardware, seeds, hyperparameters, missing details.
- Systems: latency, throughput, memory, scaling, deployment assumptions, cost.
- Internal links: tasks, methods/models, optimizers, datasets, domains, metrics, benchmarks, concepts, related papers.
- Relationship types: classify paper links as Builds on, Contrasts with, Shares dataset, Shares method, Shares task, Shares metric, Application/domain, or Follow-up reading.
- Baselines: link important compared models, methods, and architectures as method/model notes.
- Emerging notes: link every staged note to the source paper, a plausible stable hub when available, related staged notes, and the relevant emerging folder index.
- Duplicate control: add aliases for common spellings, acronyms, and source-specific names on new graph notes.
- Language: avoid vault-relative or processing-context prose in the note body; keep summaries, definitions, evidence, limitations, and rationales subject-facing.
- Final audit: run `python3 tools/skills/paper-processing/scripts/graph_audit.py` and resolve missing wikilinks or orphan emerging notes.
- Missing or irrelevant fields: use `not reported` for absent details and `not applicable` for non-applicable fields.
