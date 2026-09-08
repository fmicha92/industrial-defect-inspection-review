---
title: "A Novel Dataset for Fabric Defect Detection: Bridging Gaps in Anomaly Detection"
aliases:
  - "A Novel Dataset for Fabric Defect Detection"
  - "Lusitano dataset paper"
paper_key: "sha256:a70b9c18d4e2d72ce127d13a58a1e0fd54443ab290d220fb4e4718579cd22254"
paper_type: dataset
year: 2024
venue: "Applied Sciences"
authors:
  - "Rui Carrilho"
  - "Kailash A. Hambarde"
  - "Hugo Proenca"
status: processed
processed_at: 2026-05-27
topics:
  - fabric defect detection
  - anomaly detection
  - texture inspection
  - dataset
tasks:
  - "[[Textile defect detection]]"
  - "[[Industrial anomaly detection]]"
domains:
  - "[[Textile and fiber inspection]]"
application_area: "textile manufacturing quality control"
datasets:
  - "[[Lusitano]]"
dataset_sizes:
  - "32000 normal training images"
  - "1038 normal test images"
  - "1646 defect test images"
splits:
  - "training: 32000 normal images"
  - "test: 1038 normal images and 1646 defect images"
modalities:
  - "RGB textile images"
methods:
  - "[[RD4AD]]"
  - "[[DBFAD]]"
model_family:
  - "[[Unsupervised anomaly detection]]"
  - "[[Anomaly Detection Models]]"
architectures:
  - "[[RD4AD]]"
  - "[[DBFAD]]"
losses:
  - "RD4AD similarity loss"
training_regime: "one-class anomaly detection trained on normal images only"
augmentation: []
synthetic_data: "none reported; the dataset images are not artificially generated and no data augmentation or post-processing was performed"
metrics:
  - "[[AU-ROC]]"
  - "[[mAP]]"
primary_metric: "[[AU-ROC]]"
metric_definitions:
  - "AUC is used for ROC-based anomaly detection evaluation."
  - "mAP is reported for anomaly detection performance."
baselines:
  - "DBFAD"
  - "RD4AD"
benchmarks:
  - "[[Lusitano benchmark]]"
evaluation_protocol: "train DBFAD and RD4AD on normal-only subsets of 1k, 2k, 4k, 8k, 16k, and 32k images; evaluate on the Lusitano test set"
parameters: "not reported"
compute: "NVIDIA RTX A6000 used for training and testing"
hardware: "NVIDIA RTX A6000"
training_time: "not reported"
inference_cost: "not reported"
url: "https://doi.org/10.3390/app14125298"
pdf: "paper-inbox/10_processed/Dataset/2024 - Carrilho - A Novel Dataset for Fabric Defect Detection Bridging Gaps in Anomaly Detection.pdf"
code: "DBFAD and RD4AD code repositories used; dataset artifact reported separately"
data: "https://kailashhambarde.github.io/Lusitano/"
doi: "10.3390/app14125298"
arxiv: "not reported"
related_papers:
  - "[[2021 - ZJU-Leaper A Benchmark Dataset for Fabric Defect Detection and a Comparative Study]]"
  - "[[2019 - A Public Fabric Database for Defect Detection Methods and Results]]"
related_concepts:
  - "[[Unsupervised anomaly detection]]"
  - "[[Industrial visual inspection]]"
related_methods:
  - "[[RD4AD]]"
  - "[[DBFAD]]"
related_datasets:
  - "[[Lusitano]]"
  - "[[ZJU-Leaper]]"
  - "[[AITEX]]"
related_domains:
  - "[[Textile and fiber inspection]]"
related_tasks:
  - "[[Textile defect detection]]"
  - "[[Industrial anomaly detection]]"
related_benchmarks:
  - "[[Lusitano benchmark]]"
concept_notes_created_or_updated:
  - "[[Lusitano]]"
  - "[[Lusitano benchmark]]"
  - "[[RD4AD]]"
  - "[[DBFAD]]"
source_file: "paper-inbox/10_processed/Dataset/2024 - Carrilho - A Novel Dataset for Fabric Defect Detection Bridging Gaps in Anomaly Detection.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2024 - Carrilho - A Novel Dataset for Fabric Defect Detection Bridging Gaps in Anomaly Detection.md"
extracted_text: "paper-inbox/90_processing/text/2024 - Carrilho - A Novel Dataset for Fabric Defect Detection Bridging Gaps in Anomaly Detection.txt"
artifact_status: "dataset reported available"
tags:
  - paper
  - dataset
  - benchmark
  - textile-inspection
---

# A Novel Dataset for Fabric Defect Detection: Bridging Gaps in Anomaly Detection

## Summary

- Introduces [[Lusitano]], a real factory fabric anomaly detection dataset collected over three months in Portugal.
- Frames the dataset as a one-class [[Textile defect detection]] benchmark: training uses 32,000 normal images, while testing uses normal and defective images.
- Evaluates [[DBFAD]] and [[RD4AD]] on training subsets from 1k to 32k normal images; [[RD4AD]] reports the best Table 3 result with 0.8860 AUC and 0.9390 mAP at 32k training images.

## Paper Type

- Type: dataset / benchmark paper.
- Why: The central contribution is the Lusitano dataset and baseline evaluation for one-class fabric anomaly detection.

## Problem

- Task: [[Textile defect detection]] and [[Industrial anomaly detection]].
- Setting: textile quality control using high-resolution fabric images collected in factory conditions.
- Inputs: fabric images captured by an industrial-grade Teledyne Dalsa Linea camera.
- Outputs: anomaly/defect decisions for fabric images; localization output is discussed through the selected anomaly methods but exact output annotation format is not fully reported.
- Motivation: Human fabric inspection is labor-intensive, fatigue-prone, and reported to have 60-75% accuracy; fabric defects are rare, diverse, and difficult to standardize.
- Assumptions: One-class training is useful because normal images are easier to collect than representative labeled examples of every defect type.

## Contribution

- Claimed: The paper provides a novel fabric defect dataset from a Portuguese textile company.
- Claimed: Lusitano bridges gaps in existing fabric defect datasets by using real factory images without synthetic generation or augmentation.
- Shown: The dataset contains 32,000 normal training images and a test set with 1038 normal and 1646 defect images.
- Shown: RD4AD outperforms DBFAD across the reported AUC and mAP results.
- Inferred: The benchmark is most useful for normal-only textile anomaly detection rather than multi-class supervised defect classification.

## Method

- Core idea: collect a real factory one-class fabric dataset and benchmark two open-source anomaly detection methods on different normal-training-data volumes.
- Architecture / algorithm: [[RD4AD]] and [[DBFAD]], both distillation-based one-class anomaly detection methods.
- Objective / loss: RD4AD minimizes a similarity loss for reverse distillation; DBFAD uses a teacher-student reverse-distillation setup. Full loss definitions are not reported in the extracted text.
- Optimization: RD4AD is trained for 200 epochs with learning rate 0.005, batch size 16, image size 256 x 256, and patience 5. DBFAD is trained for 100 epochs with learning rate 0.005, batch size 16, image size 256 x 256, and patience 10.
- Training data: normal-only Lusitano subsets of 1k, 2k, 4k, 8k, 16k, and 32k images.
- Data pipeline: images collected with one camera in front of a fabric inspection machine using a strong nearly uniform light source; experiment inputs are center-cropped to 2000 x 1000 pixels.
- Augmentation / synthesis: none reported for the dataset; no artificial defects, augmentation, or post-processing were used.
- Inference: anomaly scores are computed by the selected one-class methods and evaluated against the test set.
- Complexity / deployment constraints: compute uses NVIDIA RTX A6000; training time and inference latency are not reported.

## ML / DL Extraction

### Task Formulation

- Input modality: high-resolution fabric images.
- Output target: image-level anomaly detection; localization details are not fully reported.
- Supervision: one-class, normal-only training.
- Objective: detect real fabric defects as deviations from normal textile texture.

### Model And Training

- Model family: [[Unsupervised anomaly detection]], teacher-student / reverse-distillation anomaly detection.
- Architecture: [[RD4AD]] and [[DBFAD]].
- Parameters: not reported.
- Pretraining: RD4AD uses a pre-trained teacher encoder; DBFAD uses a teacher-student architecture. Specific pretraining sources are not reported in the extracted text.
- Fine-tuning: not reported.
- Losses: RD4AD similarity loss; DBFAD details not fully reported.
- Optimizer: not reported.
- Hyperparameters: RD4AD: 200 epochs, learning rate 0.005, batch size 16, 256 x 256 image size, patience 5. DBFAD: 100 epochs, learning rate 0.005, batch size 16, 256 x 256 image size, patience 10.
- Seeds: not reported.
- Training compute: NVIDIA RTX A6000.

### Data

- Datasets: [[Lusitano]].
- Data source: Paulo de Oliveira, S.A. textile factory in Covilha, Portugal.
- Dataset size: 32,000 normal training images; test set with 1038 normal and 1646 defect images.
- Labels / annotations: normal versus defective test images are reported; defect-type labels and pixel-level masks are not reported.
- Splits: 32k normal training; 1038 normal and 1646 defect test.
- Preprocessing: center crop to 2000 x 1000 pixels for training and testing; model input size 256 x 256.
- Augmentation: none reported.
- Synthetic data: none reported.
- Leakage checks: not reported.
- License: article is CC BY; dataset license not separately reported in the extracted text.

### Evaluation

- Protocol: train DBFAD and RD4AD on 1k, 2k, 4k, 8k, 16k, and 32k normal-image subsets; test on the Lusitano normal/defect test set.
- Used performance metrics: [[AU-ROC]], [[mAP]].
- Primary metric: [[AU-ROC]].
- Metric definitions: not fully reported; ROC and precision-recall curves are used for interpretation.
- Metric direction / units: higher is better.
- Baselines: [[DBFAD]], [[RD4AD]].
- Benchmarks: [[Lusitano benchmark]].
- Statistical tests: not reported.
- Failure cases: precision remains suboptimal for both methods; subtle pixel differences between normal and defective fabrics make detection difficult.

## Evidence

### Experimental Setup

- Datasets: [[Lusitano]].
- Splits: 32k normal training images; 1038 normal and 1646 defect test images.
- Baselines: [[DBFAD]], [[RD4AD]].
- Used performance metrics: AUC/AU-ROC and mAP.
- Compute: NVIDIA RTX A6000.
- Hardware: NVIDIA RTX A6000.
- Training time: not reported.
- Inference cost: not reported.

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| DBFAD at 1k training images | [[Lusitano]] / [[Textile defect detection]] | AUC | higher | not applicable | 0.7573 | Lowest DBFAD training subset. |
| DBFAD at 32k training images | [[Lusitano]] / [[Textile defect detection]] | AUC | higher | 0.7573 | 0.7814 | Modest improvement with more normal data. |
| RD4AD at 1k training images | [[Lusitano]] / [[Textile defect detection]] | AUC | higher | not applicable | 0.8231 | Higher than DBFAD at 1k. |
| RD4AD at 32k training images | [[Lusitano]] / [[Textile defect detection]] | AUC | higher | 0.8231 | 0.8860 | Best AUC in Table 3. |
| DBFAD at 32k training images | [[Lusitano]] / [[Textile defect detection]] | mAP | higher | 0.8162 at 1k | 0.8429 | Best DBFAD mAP in Table 3. |
| RD4AD at 32k training images | [[Lusitano]] / [[Textile defect detection]] | mAP | higher | 0.8773 at 1k | 0.9390 | Best mAP in Table 3. |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[AU-ROC]] | anomaly detection | area under ROC curve | higher | yes | Reported as AUC in Table 3. |
| [[mAP]] | anomaly detection / precision-recall evaluation | mean average precision | higher | no | Reported in Table 3. |

### Ablations

- The paper varies normal-training-data volume: 1k, 2k, 4k, 8k, 16k, and 32k images.
- Both DBFAD and RD4AD improve with larger training subsets overall, but the improvements are modest and precision remains suboptimal.

## Dataset / Benchmark Details

- Source: Paulo de Oliveira, S.A. textile factory in Covilha, Portugal.
- Collection: January to March 2024, with one camera placed in front of a fabric inspection machine and a strong nearly uniform light source.
- Annotation: normal/defect test labels are reported; defect class taxonomy and mask/box annotations are not reported.
- Size: 32,000 normal training images; 1038 normal and 1646 defect test images.
- Splits: one normal-only training split and one mixed normal/defect test split.
- Modalities: high-resolution visual fabric images.
- License: article is CC BY; dataset license not separately reported.
- Leakage risks: not reported.
- Bias / coverage: the dataset uses real factory images and real defects, but the paper states future work should segregate fabric types and improve lighting/camera positioning.
- Maintenance: the authors state they intend to continue collecting data, expanding the dataset, and testing new benchmark methods.

## Limitations

- Stated: DBFAD and RD4AD results are suboptimal, especially precision.
- Stated: future dataset improvements include segregating fabric types and better tuning lighting and camera position.
- Inferred: lack of reported defect masks or defect-type labels limits segmentation and multi-class evaluation.
- Inferred: exact generalization beyond the source factory is unclear.

## Reproducibility

- Code: DBFAD code at https://github.com/SimonThomine/DBFAD; RD4AD code at https://github.com/hq-deng/RD4AD.git.
- Data: https://kailashhambarde.github.io/Lusitano/.
- Hyperparameters: reported for RD4AD and DBFAD.
- Random seeds: not reported.
- Environment: not reported.
- Checkpoints / models: not reported.
- Exact preprocessing: center crop to 2000 x 1000 and model input size 256 x 256 are reported.
- Artifact status: dataset reported available.

## Connections

### Graph Hubs

- Tasks: [[Textile defect detection]], [[Industrial anomaly detection]]
- Datasets: [[Lusitano]], [[ZJU-Leaper]], [[AITEX]]
- Methods: [[RD4AD]], [[DBFAD]], [[Unsupervised anomaly detection]], [[Anomaly Detection Models]]
- Metrics: [[AU-ROC]], [[mAP]]
- Domains: [[Textile and fiber inspection]], [[Industrial visual inspection]]
- Benchmarks: [[Lusitano benchmark]]

### Builds On

- [[2021 - ZJU-Leaper A Benchmark Dataset for Fabric Defect Detection and a Comparative Study]]: cited as a recent improvement in fabric defect datasets; Lusitano is smaller but focuses on one-class normal-only training under factory conditions.

### Contrasts With

- [[2019 - A Public Fabric Database for Defect Detection Methods and Results]]: both address fabric inspection datasets, but Lusitano emphasizes one-class anomaly detection with real factory normal training images.

### Shares Dataset

- [[Lusitano]]: introduced by this paper.

### Shares Task

- [[Textile defect detection]]: main application.
- [[Industrial anomaly detection]]: one-class anomaly framing.

### Shares Method

- [[RD4AD]]: best reported baseline in Table 3.
- [[DBFAD]]: fabric-specific distillation baseline evaluated across all training subset sizes.
- [[Unsupervised anomaly detection]]: training uses normal samples only.

### Shares Metric

- [[AU-ROC]]: primary reported anomaly detection metric.
- [[mAP]]: reported alongside AUC.

### Application / Domain

- [[Textile and fiber inspection]]: images come from a textile factory.
- [[Industrial visual inspection]]: the paper frames fabric inspection as factory quality control.

### Follow-Up Reading

- [[Lusitano benchmark]]: benchmark protocol and key reported results.
- [[ZJU-Leaper benchmark]]: larger fabric benchmark with richer progressive annotation settings.

## Questions

- What exact dataset license applies to Lusitano beyond the article's CC BY license?
- Does Lusitano include pixel masks, bounding boxes, or only image-level normal/defect labels?
- How do newer anomaly detection methods beyond DBFAD and RD4AD perform under the same one-class protocol?
