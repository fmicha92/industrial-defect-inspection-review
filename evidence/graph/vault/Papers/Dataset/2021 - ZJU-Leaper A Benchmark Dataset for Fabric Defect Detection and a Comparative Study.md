---
title: "ZJU-Leaper: A Benchmark Dataset for Fabric Defect Detection and a Comparative Study"
aliases:
  - "ZJU-Leaper"
  - "ZJU-Leaper benchmark dataset"
paper_key: "doi:10.1109/tai.2021.3057027"
paper_type: dataset
year: 2021
venue: "IEEE Transactions on Artificial Intelligence"
authors:
  - "Chenkai Zhang"
  - "Shaozhe Feng"
  - "Xulongqi Wang"
  - "Yueming Wang"
status: processed
processed_at: 2026-05-27
topics:
  - fabric defect detection
  - benchmark dataset
  - textile inspection
  - industrial visual inspection
tasks:
  - "[[Textile defect detection]]"
  - "[[Defect segmentation]]"
domains:
  - "[[Textile and fiber inspection]]"
application_area: "textile manufacturing quality control"
datasets:
  - "[[ZJU-Leaper]]"
dataset_sizes:
  - "98777 total images"
  - "71127 normal images"
  - "27650 defect images"
  - "19 fabric patterns"
splits:
  - "one predefined test set per pattern group; one third of each pattern group selected for testing"
modalities:
  - "RGB fabric images"
methods:
  - "[[U-Net]]"
  - "[[Data augmentation]]"
  - "[[Transfer learning]]"
  - "[[Weakly supervised learning]]"
model_family:
  - "[[Deep convolutional neural network]]"
architectures:
  - "[[U-Net]]"
losses:
  - "pixel-wise cross-entropy for CNN-based supervised methods"
training_regime: "five progressive settings from normal-only training to fully supervised mask training"
augmentation:
  - "[[Data augmentation]]"
synthetic_data: "defect regions transferred from a small amount of real defect data into defect-free images using affine transformations and lightness/color perturbations"
metrics:
  - "[[Dice score]]"
  - "[[IoU]]"
  - "[[Precision]]"
  - "[[Recall]]"
  - "[[F1-score]]"
primary_metric: "[[F1-score]]"
metric_definitions:
  - "Pixel-level F1/Dice is TPpix / (TPpix + 1/2(FPpix + FNpix))."
  - "Region precision counts correct proposed regions over total proposed regions."
  - "Region recall counts detected ground-truth regions over total ground-truth regions."
  - "Region F1 aggregates region precision and region recall."
  - "Sample-level F1 counts matched defective/normal sample decisions."
baselines:
  - "Sparse coding"
  - "Convolutional auto-encoder"
  - "One-class SVM"
  - "Transfer learning with U-Net"
  - "Data augmentation with U-Net"
  - "Weakly supervised U-Net with label annotations"
  - "Weakly supervised U-Net with bounding-box annotations"
  - "Fully supervised U-Net with mask annotations"
benchmarks:
  - "[[ZJU-Leaper benchmark]]"
evaluation_protocol: "pixel-level, region-level, and sample-level metrics evaluated on predefined test sets for five progressive task settings"
parameters: "not reported"
compute: "not reported"
hardware: "not reported"
training_time: "not reported"
inference_cost: "not reported"
url: "https://doi.org/10.1109/TAI.2021.3057027"
pdf: "paper-inbox/10_processed/Dataset/2021 - Zhang - ZJU-Leaper A Benchmark Dataset for Fabric Defect Detection and a Comparative Study.pdf"
code: "reported available on dataset website"
data: "reported available: http://www.qaas.zju.edu.cn/zju-leaper and https://github.com/nico-zck/zju-leaper-dataset"
doi: "10.1109/TAI.2021.3057027"
arxiv: "not reported"
related_papers:
  - "[[2019 - A Public Fabric Database for Defect Detection Methods and Results]]"
related_concepts:
  - "[[Surface defect detection]]"
  - "[[Industrial visual inspection]]"
related_methods:
  - "[[U-Net]]"
  - "[[Data augmentation]]"
  - "[[Transfer learning]]"
  - "[[Weakly supervised learning]]"
related_datasets:
  - "[[ZJU-Leaper]]"
  - "[[AITEX]]"
  - "[[DAGM2007]]"
related_domains:
  - "[[Textile and fiber inspection]]"
related_tasks:
  - "[[Textile defect detection]]"
  - "[[Defect segmentation]]"
related_benchmarks:
  - "[[ZJU-Leaper benchmark]]"
concept_notes_created_or_updated:
  - "[[ZJU-Leaper]]"
  - "[[ZJU-Leaper benchmark]]"
source_file: "paper-inbox/10_processed/Dataset/2021 - Zhang - ZJU-Leaper A Benchmark Dataset for Fabric Defect Detection and a Comparative Study.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2021 - Zhang - ZJU-Leaper A Benchmark Dataset for Fabric Defect Detection and a Comparative Study.md"
extracted_text: "paper-inbox/90_processing/text/2021 - Zhang - ZJU-Leaper A Benchmark Dataset for Fabric Defect Detection and a Comparative Study.txt"
artifact_status: "dataset, evaluation code, and baseline details reported available"
tags:
  - paper
  - dataset
  - benchmark
  - textile-inspection
---

# ZJU-Leaper: A Benchmark Dataset for Fabric Defect Detection and a Comparative Study

## Summary

- Introduces [[ZJU-Leaper]], a fabric defect dataset with 98,777 images from 19 fabric patterns, including image labels, bounding boxes, and pixel-wise masks.
- Defines [[ZJU-Leaper benchmark]], a five-setting progressive benchmark that ranges from normal-only training to fully supervised mask-based training.
- Proposes an evaluation protocol with pixel-level [[Dice score]], region-level precision/recall/F1, and sample-level F1 to avoid misleading results from class imbalance and inconsistent fabric-inspection metrics.

## Paper Type

- Type: dataset / benchmark paper.
- Why: The main contribution is a new public fabric dataset, a benchmark organization, an evaluation protocol, and baseline experiments.

## Problem

- Task: [[Textile defect detection]] and [[Defect segmentation]].
- Setting: visual inspection for textile manufacturing quality control.
- Inputs: high-resolution full-color fabric images from factory and laboratory collection.
- Outputs: defective/normal image decisions, defect localization, and pixel-level defect masks depending on the task setting.
- Motivation: Existing textile datasets are described as too small, too simple, inconsistently annotated, or mismatched with practical deployment where defects are rare and fabric patterns change.
- Assumptions: Inspection models often need to work on a single fabric or a group of similar fabrics, and practical users prefer fast deployment and progressive upgrades over one general model requiring long tuning.

## Contribution

- Claimed: ZJU-Leaper provides a larger, more varied fabric inspection dataset than prior public fabric datasets.
- Claimed: The five task settings reflect practical annotation and deployment costs in textile factories.
- Claimed: The three-level evaluation protocol gives a more truthful comparison than inconsistent prior metrics.
- Shown: The dataset contains 98,777 images, including 71,127 normal images and 27,650 defective images across 19 fabric patterns.
- Shown: Baseline experiments compare methods across normal-only, small-defect-data, weakly supervised, bounding-box, and full-mask settings.
- Inferred: The benchmark is intended to encourage methods that improve under scarce-defect and scarce-annotation regimes, not only fully supervised segmentation.

## Method

- Core idea: Build a fabric defect benchmark that matches practical textile inspection constraints and compare baseline methods across increasing levels of defect annotation.
- Architecture / algorithm: The paper evaluates sparse coding, convolutional auto-encoder, one-class SVM, U-Net transfer learning, U-Net data augmentation, weakly supervised U-Net variants, and fully supervised U-Net.
- Objective / loss: CNN-based supervised baselines use pixel-wise supervision; the paper explicitly notes pixel-wise cross-entropy can bias models toward large defects.
- Optimization: CAE uses Adam with batch size 8, learning rate 1e-4, and 60 epochs. U-Net variants use reported learning rates, weight decay, batch sizes, and epochs by setting.
- Training data: training subsets defined by the five ZJU-Leaper task settings.
- Data pipeline: candidate images were collected from factories or laboratory setups, screened and adjusted, then annotated by humans with labels, boxes, and masks.
- Augmentation / synthesis: the Setting 2 data augmentation baseline extracts real defect regions using masks, applies affine transformations and lightness/color perturbations, and inserts them into defect-free images.
- Inference: methods output anomaly masks, segmentation masks, or sample-level defect decisions depending on setting.
- Complexity / deployment constraints: the paper emphasizes fast retraining and deployment for changing fabric patterns; wall-clock inference and training cost are not reported.

## ML / DL Extraction

### Task Formulation

- Input modality: RGB fabric images.
- Output target: defective/normal labels, bounding boxes, and pixel-wise masks depending on available annotation.
- Supervision: unsupervised normal-only training, small-data supervised training, weak supervision from labels or boxes, and fully supervised mask training.
- Objective: detect fabric defects under practical annotation-cost regimes.

### Model And Training

- Model family: classical reconstruction/outlier methods and [[Deep convolutional neural network]] segmentation models.
- Architecture: sparse coding, CAE, one-class SVM over CAE features, and 4-skip-connection [[U-Net]] variants.
- Parameters: sparse coding uses 128 dictionary elements; other parameter counts are not reported.
- Pretraining: transfer learning baseline pretrains a U-Net encoder on normal-image reconstruction.
- Fine-tuning: transfer learning baseline trains the transferred encoder on supervised segmentation with limited defective samples.
- Losses: pixel-wise cross-entropy is discussed for CNN-based supervised methods; exact losses for all baselines are not fully reported.
- Optimizer: Adam for CAE; optimizer for all U-Net variants is not fully reported.
- Hyperparameters: CAE uses batch size 8, learning rate 1e-4, 60 epochs; Setting 2/3/4/5 U-Net variants report learning rates, weight decay, batch sizes, and epochs in the text.
- Seeds: not reported.
- Training compute: not reported.

### Data

- Datasets: [[ZJU-Leaper]].
- Data source: factory and laboratory fabric images.
- Dataset size: 98,777 images; 27,650 defective and 71,127 normal; 19 fabric patterns.
- Labels / annotations: defective/normal label, pattern name/number, group name/number, bounding box, and pixel-wise mask.
- Splits: one predefined test set per pattern group, using one third of the data from each group.
- Preprocessing: image screening and adjustment are reported; detailed preprocessing steps are not fully reported.
- Augmentation: affine transformations and lightness/color perturbations for defect-region transfer in the Setting 2 DA baseline.
- Synthetic data: the DA baseline synthesizes defect images by transferring real defect regions into normal fabric images; the dataset itself is collected from real images.
- Leakage checks: the paper states test-set use during training and hyperparameter selection is strictly prohibited.
- License: not reported.

### Evaluation

- Protocol: five task settings evaluated on predefined test sets with pixel-level, region-level, and sample-level metrics.
- Used performance metrics: [[Dice score]], [[IoU]], [[Precision]], [[Recall]], [[F1-score]].
- Primary metric: [[F1-score]] family across pixel, region, and sample levels.
- Metric definitions: pixel-level F1/Dice, region precision, region recall, region F1, size-conditioned region F1, and sample-level F1 are defined in the paper.
- Metric direction / units: higher is better for all reported F1, Dice, precision, recall, and IoU-style metrics.
- Baselines: sparse coding, CAE, one-class SVM, transfer learning, data augmentation, weakly supervised label and bounding-box variants, and fully supervised U-Net.
- Benchmarks: [[ZJU-Leaper benchmark]].
- Statistical tests: not reported.
- Failure cases: unsupervised methods perform poorly on complex patterns and noisy factory data; models tend to miss small defects.

## Evidence

### Experimental Setup

- Datasets: [[ZJU-Leaper]].
- Splits: one third of each pattern group is reserved as the test set.
- Baselines: sparse coding, CAE, OCSVM, U-Net transfer learning, U-Net with data augmentation, weakly supervised U-Net from labels or boxes, and fully supervised U-Net.
- Used performance metrics: pixel-level F1/Dice, region precision/recall/F1, size-conditioned region F1, sample-level F1, PR AUC, and break-even point.
- Compute: not reported.
- Hardware: not reported.
- Training time: not reported.
- Inference cost: not reported.

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| Normal-only methods | [[ZJU-Leaper]] / [[Textile defect detection]] | F1 family | higher | not applicable | lower on complex patterns | SC, CAE, and OCSVM work best on simple pattern Group 1 and struggle on Groups 2-4. |
| Small defect data | [[ZJU-Leaper]] / [[Defect segmentation]] | F1 family | higher | plain U-Net | DA and TL improve | Data augmentation and transfer learning improve over limited-supervision U-Net. |
| Label-only weak supervision | [[ZJU-Leaper]] / [[Defect segmentation]] | F1 family | higher | not applicable | low relative performance | Label annotations alone are insufficient for reliable localization. |
| Bounding-box weak supervision | [[ZJU-Leaper]] / [[Defect segmentation]] | F1 family | higher | label-only setting | higher performance | Rough spatial information improves supervised detection performance. |
| Full-mask supervision | [[ZJU-Leaper]] / [[Defect segmentation]] | F1 family | higher | other settings | best overall | Fully supervised U-Net has the highest detection performance but highest annotation cost. |
| Size-conditioned evaluation | [[ZJU-Leaper]] / [[Defect segmentation]] | region F1 | higher | not applicable | lower for small defects | Models tend to detect large defects and ignore small defects. |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[Dice score]] | Pixel-level defect mask quality | TPpix / (TPpix + 1/2(FPpix + FNpix)) | higher | yes | The paper prefers Dice over IoU for overall pixel-wise evaluation under imbalance. |
| [[IoU]] | Region matching criterion | overlap over union | higher | no | Region correctness uses IoU > 0.3 or area-ratio criteria. |
| [[Precision]] | Region-level proposed-region quality | correct proposed regions / total proposed regions | higher | no | Used to form region F1. |
| [[Recall]] | Region-level ground-truth detection | detected ground-truth regions / total ground-truth regions | higher | no | Used to form region F1. |
| [[F1-score]] | Pixel, region, and sample aggregation | harmonic mean-style aggregation | higher | yes | The paper defines F1pix, F1reg, size-conditioned F1reg, and F1sam. |

### Ablations

- The paper compares the same task across progressively richer annotation settings rather than reporting a single architecture ablation.
- The baseline discussion indicates that adding limited supervision, transfer learning, data augmentation, and rough spatial annotations improves over normal-only or label-only settings.

## Dataset / Benchmark Details

- Source: fabric images collected from factories and laboratory setups.
- Collection: around 5,000 images per fabric type after screening and adjustment; laboratory images use stable camera settings and fixed illumination.
- Annotation: six people with normal visual function identify defects and label silhouettes; three annotators independently label many images, and final masks are assembled by averaging their outputs.
- Size: 98,777 images from 19 fabric patterns.
- Splits: predefined test sets, one per pattern group, with one third of the group data held out.
- Modalities: RGB visual fabric images.
- License: not reported.
- Leakage risks: the paper explicitly forbids using test data for model training and hyperparameter selection, but does not report additional leakage audits.
- Bias / coverage: ZJU-Leaper reduces center bias relative to compared fabric datasets and contains broader defect-size variation; Group 5 factory data has poorer image quality, illumination consistency, and annotation accuracy.
- Maintenance: the authors state future work includes expanding the dataset and maintaining a performance table.

## Limitations

- Stated: ZJU-Leaper is not a perfect representation of the real fabric world.
- Stated: the baseline experiments cover only part of the possible future method space.
- Stated: unsupervised anomaly detection on image data fails to reach satisfactory performance under insufficient annotation.
- Inferred: the dataset is specific to fabric textures and may not transfer directly to non-textile industrial surfaces.
- Inferred: exact numerical table values should be checked in the original PDF when precise benchmark ranking is required, because the compact extracted text did not preserve the full Table III numeric layout.

## Reproducibility

- Code: evaluation protocol and experiment details reported available on the dataset website.
- Data: reported available at http://www.qaas.zju.edu.cn/zju-leaper and https://github.com/nico-zck/zju-leaper-dataset.
- Hyperparameters: many baseline learning rates, batch sizes, weight decay values, and epoch counts are reported in the paper text.
- Random seeds: not reported.
- Environment: not reported.
- Checkpoints / models: not reported.
- Exact preprocessing: not fully reported.
- Artifact status: dataset, evaluation code, and baseline details reported available.

## Connections

### Graph Hubs

- Tasks: [[Textile defect detection]], [[Defect segmentation]]
- Datasets: [[ZJU-Leaper]], [[AITEX]], [[DAGM2007]]
- Methods: [[U-Net]], [[Data augmentation]], [[Transfer learning]], [[Weakly supervised learning]], [[Deep convolutional neural network]]
- Metrics: [[Dice score]], [[IoU]], [[Precision]], [[Recall]], [[F1-score]]
- Domains: [[Textile and fiber inspection]], [[Industrial visual inspection]]
- Benchmarks: [[ZJU-Leaper benchmark]]

### Builds On

- [[2019 - A Public Fabric Database for Defect Detection Methods and Results]]: both address public fabric defect benchmark construction, but ZJU-Leaper adds larger scale, richer annotations, progressive task settings, and a three-level evaluation protocol.

### Shares Dataset

- [[ZJU-Leaper]]: introduced by this paper.

### Shares Task

- [[Textile defect detection]]: the benchmark targets automated fabric defect inspection.
- [[Defect segmentation]]: mask annotations and U-Net baselines evaluate pixel-level localization.

### Shares Method

- [[U-Net]]: used as the segmentation baseline across supervised and weakly supervised settings.
- [[Data augmentation]]: used to synthesize additional training examples from a small amount of real defect data.
- [[Transfer learning]]: used to transfer a reconstruction-pretrained U-Net encoder into limited-supervision segmentation.
- [[Weakly supervised learning]]: label and bounding-box settings evaluate lower-cost annotation regimes.

### Shares Metric

- [[Dice score]]: selected for pixel-level mask evaluation.
- [[IoU]]: used as a region matching criterion.
- [[F1-score]]: used across pixel, region, and sample evaluation levels.

### Application / Domain

- [[Textile and fiber inspection]]: the paper studies fabric inspection for textile manufacturing quality control.
- [[Industrial visual inspection]]: the paper frames automated fabric inspection as a manufacturing automation and quality-control problem.

### Follow-Up Reading

- [[Surface defect detection]]: broader task family for industrial surface inspection with scarce defects and annotation constraints.

## Questions

- What license and access status currently apply to the ZJU-Leaper dataset and code?
- Which later methods report results on the official ZJU-Leaper benchmark protocol?
- Are the five settings still used consistently in follow-up papers, or do later works use custom splits?
