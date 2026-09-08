---
title: "Non-parametric texture defect detection using Weibull features"
aliases:
  - "Non-parametric texture defect detection using Weibull features"
paper_key: "sha256:01828060a9391e2dcf9162f58d23552135344327e64cf15437d445093c46d119"
paper_type: research
year: 2011
venue: "Proceedings of SPIE, Image Processing: Machine Vision Applications IV, volume 7877"
authors:
  - "Fabian Timm"
  - "Erhardt Barth"
status: processed
processed_at: 2026-06-09
topics:
  - "texture defect detection"
  - "Weibull image statistics"
  - "industrial optical inspection"
tasks:
  - "[[Surface defect detection]]"
  - "[[Defect classification]]"
domains:
  - "[[Multi-industry anomaly detection]]"
datasets:
  - "[[DAGM2007]]"
dataset_sizes:
  - "DAGM2007 classes 1-4; each class has 1,000 defect-free and 150 defective grayscale images"
splits:
  - "The paper evaluates all 1,150 images per selected class because the method has no learning scheme"
modalities:
  - "grayscale texture images"
methods:
  - "[[Weibull texture features]]"
  - "median-distance novelty detection"
model_family:
  - "non-parametric novelty detection"
architectures: []
metrics:
  - "[[Error rate]]"
  - "[[AU-ROC]]"
primary_metric: "[[Error rate]]"
metric_definitions:
  - "Equal error rate is reported from ROC curves."
  - "AUC is reported as threshold-independent ROC area."
  - "Total cost uses asymmetric contest costs with false positives weighted 20 and false negatives weighted 1, following the paper's sign convention."
baselines:
  - "Gabor filters"
  - "grey-level statistics"
benchmarks:
  - "[[DAGM2007]]"
evaluation_protocol: "Patch-level Weibull features are aggregated by maximum distance to a per-image median reference point; thresholds are evaluated with ROC, equal error rate, AUC, and asymmetric total cost."
parameters: "patch size 32 x 32; 50% patch overlap; Gaussian derivative filter size and sigma determined from patch size"
compute: "not reported"
hardware: "not reported"
training_time: "not applicable"
inference_cost: "described as efficient enough for real-time applications; exact latency not reported"
doi: "not reported"
url: "not reported"
pdf: "paper-inbox/10_processed/Research/2011 - Timm - Non-parametric texture defect detection using Weibull features.pdf"
code: "not reported"
data: "https://zenodo.org/records/8086136"
related_papers: []
related_concepts:
  - "[[Surface defect detection]]"
  - "[[Industrial visual inspection]]"
related_methods:
  - "[[Weibull texture features]]"
related_datasets:
  - "[[DAGM2007]]"
related_domains:
  - "[[Multi-industry anomaly detection]]"
related_tasks:
  - "[[Surface defect detection]]"
  - "[[Defect classification]]"
related_benchmarks:
  - "[[DAGM2007]]"
source_file: "paper-inbox/10_processed/Research/2011 - Timm - Non-parametric texture defect detection using Weibull features.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2011 - Timm - Non-parametric texture defect detection using Weibull features.md"
extracted_text: "paper-inbox/90_processing/text/2011 - Timm - Non-parametric texture defect detection using Weibull features.txt"
artifact_status: "paper PDF available in local inbox; code not reported; dataset public on Zenodo"
tags:
  - paper
---

# Non-parametric Texture Defect Detection Using Weibull Features

## Summary

Timm and Barth propose a non-parametric texture-defect detector that represents each local image patch by two [[Weibull texture features]]: the scale and shape parameters fitted to the patch gradient-magnitude distribution. A texture image is classified as defective when the maximum patch distance from the per-image median in Weibull space exceeds a threshold. The method is evaluated on four [[DAGM2007]] texture classes and reports strong ROC/AUC and equal-error-rate results without supervised model training.

## Paper Type

- Type: research.
- Why: The central contribution is a defect-detection method using local Weibull image statistics and novelty detection, evaluated on an existing benchmark dataset.

## Problem

- Task: [[Surface defect detection]] and image-level defect/no-defect classification.
- Setting: textured industrial surfaces with arbitrary, subtle, weakly labeled defects.
- Inputs: grayscale texture images.
- Outputs: image-level defective or non-defective decision; local anomalous patch locations are also visualized.
- Motivation: industrial optical inspection systems are often adapted to a specific texture or defect type and can fail when new defects or backgrounds appear.
- Assumptions: background texture patches form a compact cluster in Weibull scale-shape space, while defective patches deviate as outliers.

## Contribution

- Claimed: Introduces local Weibull scale and shape features for texture defect detection.
- Claimed: Uses a simple novelty detector based on distances from the median in Weibull parameter space.
- Shown: Evaluates on four DAGM2007 texture classes with EER from 0.1% to 8.5% and AUC from 0.96 to 0.99.
- Shown: The method does not require an exhaustive training set and can work on each texture image individually.

## Method

- Local patches are extracted from each texture image.
- Directional Gaussian derivative filters compute local gradient magnitudes.
- A Weibull distribution is fitted to each patch's gradient-magnitude distribution by maximum likelihood.
- The fitted Weibull shape and scale parameters define a two-dimensional feature space.
- The median of all patch features in an image is used as the reference point.
- A patch is treated as anomalous if its distance to the median is large; the image is classified as defective if the maximum patch distance exceeds a threshold.
- Patch size is selected from weak defect statistics; the paper reports 32 x 32 patches for all four evaluated DAGM classes.

## Evidence

### Experimental Setup

- Dataset: [[DAGM2007]] classes 1-4.
- Per-class data: 1,000 defect-free and 150 defective grayscale 512 x 512 images.
- Labels: weak ellipse labels, not pixel-wise masks.
- Patch overlap: 50%.
- Thresholding: optimized by minimizing total asymmetric cost.
- Costs: the paper follows the DAGM contest cost setting, with one error type weighted 20 and the other weighted 1 as stated in the experiment section.
- Metrics: equal error rate, AUC, total cost, false positives, false negatives, and false-negative rate at 100% true-negative rate.

### Main Results

| DAGM class | EER | AUC | Total cost | FP | FN | FN* |
|---|---:|---:|---:|---:|---:|---:|
| Class 1 | 8.5% | 0.96 | 190 | 3 | 130 | 47.0% |
| Class 2 | 0.1% | 0.99 | 2 | 0 | 2 | 0.2% |
| Class 3 | 1.3% | 0.99 | 28 | 0 | 28 | 2.8% |
| Class 4 | 3.2% | 0.99 | 51 | 0 | 51 | 5.1% |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[Error rate]] | ROC equal-error point on DAGM classes | percent | lower is better | yes | Reported as EER. |
| [[AU-ROC]] | Threshold-independent defect/no-defect discrimination | area under ROC | higher is better | no | AUC is 0.96-0.99 across the four classes. |
| Total cost | DAGM contest-style asymmetric classification cost | weighted error count | lower is better | no | Not a separate metric note; retained as paper-specific protocol detail. |

## ML / DL Extraction

### Task Formulation

- Input modality: grayscale texture images.
- Output target: defective or non-defective image decision, with patch outliers indicating likely defect regions.
- Supervision: weak labels are available for evaluating and sizing patches; the method itself is unsupervised/non-parametric at detection time.
- Objective: detect arbitrary deviations from a reference texture without adapting to a specific defect type.

### Model And Training

- Model family: non-parametric novelty detection.
- Architecture: not applicable.
- Parameters: patch size 32 x 32, 50% overlap, Gaussian derivative filters derived from patch size, and a distance threshold.
- Pretraining: not applicable.
- Fine-tuning: not applicable.
- Losses: not applicable.
- Optimizer: not applicable.
- Hyperparameters: filter size `ceil(p/11)` and sigma `w/5` are derived from patch size.
- Seeds: not reported.
- Training compute: not applicable.

### Data

- Dataset: [[DAGM2007]].
- Data source: Bosch-provided DAGM 2007 weakly supervised industrial optical inspection benchmark.
- Dataset size used: four texture classes, each with 1,000 defect-free and 150 defective images.
- Labels / annotations: weak ellipses around defects; the paper emphasizes that exact pixel-wise defect locations are not available.
- Splits: no train/test split is used for model learning because the method has no learning scheme; classification error is estimated on all 1,150 images per class.
- Preprocessing: patch extraction and gradient-magnitude computation.
- Augmentation: not reported.
- Synthetic data: the benchmark images are artificially generated, but the paper does not synthesize additional data.
- Leakage checks: not reported.
- License: not reported in the paper.

### Evaluation

- Protocol: evaluate ROC curves and thresholded classification on four DAGM texture classes.
- Used performance metrics: [[Error rate]], [[AU-ROC]], total cost, false positives, false negatives, and FN*.
- Primary metric: [[Error rate]].
- Metric direction / units: lower is better for EER and total cost; higher is better for AUC.
- Baselines: the abstract contrasts with Gabor filters and grey-level statistics but does not provide a full reproduced baseline table.
- Benchmarks: [[DAGM2007]].
- Statistical tests: not reported.
- Failure cases: class 1 is most difficult; the paper attributes this to challenging background/defect combinations and defects that are hard to detect manually.

## Limitations

- Evaluation covers four DAGM2007 classes rather than all ten classes.
- Baseline comparisons are discussed broadly, but the extracted text does not include detailed side-by-side baseline results.
- Threshold optimization uses benchmark labels; deployment behavior under unseen production shifts is not quantified.
- Pixel-wise localization is not fully evaluated because DAGM labels are weak ellipses rather than exact masks.

## Reproducibility

- Code: not reported.
- Data: [[DAGM2007]] is publicly hosted at [Zenodo record 8086136](https://zenodo.org/records/8086136).
- Implementation details: patch size, overlap, Gaussian derivative filter relationships, Weibull maximum-likelihood fitting, median reference point, and distance-threshold novelty detection are reported.
- Environment: not reported.

## Connections

### Graph Hubs

- Tasks: [[Surface defect detection]], [[Defect classification]]
- Methods: [[Weibull texture features]]
- Datasets: [[DAGM2007]]
- Domains: [[Multi-industry anomaly detection]]
- Metrics: [[Error rate]], [[AU-ROC]]

### Shares Dataset

| Related item | Relationship | Rationale |
|---|---|---|
| [[DAGM2007]] | Shares dataset | The paper evaluates its texture-defect detector on DAGM2007 classes 1-4. |

### Shares Task

| Related item | Relationship | Rationale |
|---|---|---|
| [[Surface defect detection]] | Shares task | The method detects local defects on textured industrial surfaces. |
| [[Defect classification]] | Shares task | Evaluation reports image-level defective/non-defective decisions. |

### Shares Method

| Related item | Relationship | Rationale |
|---|---|---|
| [[Weibull texture features]] | Introduces/uses method | The central representation is a two-parameter Weibull fit to local gradient magnitudes. |

### Application / Domain

| Related item | Relationship | Rationale |
|---|---|---|
| [[Industrial visual inspection]] | Application area | The paper frames automated optical inspection as the target deployment setting. |
| [[Multi-industry anomaly detection]] | Dataset/domain route | DAGM2007 is a synthetic multi-texture inspection benchmark rather than one specific industrial material or product. |

## Questions

- Is there a stable DOI for the SPIE paper record beyond the local PDF metadata? It was not reported in the available extraction.
- Would the method retain its reported efficiency and accuracy on newer real-world industrial anomaly datasets such as [[MVTec AD]] or [[Real-IAD]]?
