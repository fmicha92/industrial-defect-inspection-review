---
title: "Detecting Visual Anomalies in an Industrial Environment: Unsupervised Methods Put to the Test on the AutoVI Dataset"
aliases:
  - "Detecting Visual Anomalies in an Industrial Environment"
  - "Unsupervised Methods Put to the Test on the AutoVI Dataset"
paper_key: "sha256:42ee3d267166f3013d302993ef409f584cf0d8ff609668d48a56d90c22eb666f"
paper_type: "benchmark"
year: 2024
venue: "Computers in Industry"
authors:
  - "Philippe Carvalho"
  - "Meriem Lafou"
  - "Alexandre Durupt"
  - "Antoine Leblanc"
  - "Yves Grandvalet"
status: "processed"
processed_at: "2026-06-01"
topics:
  - "industrial visual inspection"
  - "automotive assembly"
  - "unsupervised anomaly detection"
tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Surface defect detection]]"
domains:
  - "[[Automotive manufacturing]]"
datasets:
  - "[[AutoVI]]"
methods:
  - "[[Unsupervised anomaly detection]]"
  - "[[Unsupervised learning]]"
  - "[[Patch-based anomaly detection]]"
metrics:
  - "[[AU-ROC]]"
  - "[[Average precision]]"
  - "[[Area Under Saturated Per-Region Overlap]]"
primary_metric: "[[AU-ROC]]"
benchmarks:
  - "[[AutoVI]]"
code: "https://github.com/phcarval/autovi-paper-code; https://github.com/phcarval/autovi_evaluation_code"
data: "https://zenodo.org/records/10459003"
doi: "10.1016/j.compind.2024.104151"
url: "https://doi.org/10.1016/j.compind.2024.104151"
related_concepts:
  - "[[Surface defect detection]]"
  - "[[Industrial visual inspection]]"
related_methods:
  - "[[Unsupervised anomaly detection]]"
  - "[[Unsupervised learning]]"
  - "[[Patch-based anomaly detection]]"
related_datasets:
  - "[[AutoVI]]"
related_tasks:
  - "[[Industrial anomaly detection]]"
source_file: "paper-inbox/10_processed/Benchmark/2024 - Carvalho - Detecting Visual Anomalies in an Industrial Environment Unsupervised Methods Put to the Test on the AutoVI Dataset_2.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2024 - Carvalho - Detecting Visual Anomalies in an Industrial Environment Unsupervised Methods Put to the Test on the AutoVI Dataset_2.md"
extracted_text: "paper-inbox/90_processing/text/2024 - Carvalho - Detecting Visual Anomalies in an Industrial Environment Unsupervised Methods Put to the Test on the AutoVI Dataset_2.txt"
artifact_status: "dataset and code available"
tags:
  - paper
---
# Detecting Visual Anomalies in an Industrial Environment: Unsupervised Methods Put to the Test on the AutoVI Dataset

## Summary

Carvalho et al. introduce [[AutoVI]], a public industrial visual inspection dataset captured on Renault Group automotive assembly lines, and benchmark six unsupervised anomaly-detection methods under real production conditions. The benchmark shows that methods with high scores on controlled datasets such as MVTec AD, MVTec LOCO, and VisA do not transfer uniformly to AutoVI. Patchcore achieves the best mean image-level AUROC on AutoVI at 88.4%, but no method performs reliably across all six inspection tasks, especially for logical defects, small defects, complex scenes, and high environmental variability.

### Graph Hubs

- Tasks: [[Industrial anomaly detection]], [[Surface defect detection]]
- Methods: [[Unsupervised anomaly detection]], [[Unsupervised learning]], [[Patch-based anomaly detection]]
- Datasets: [[AutoVI]]
- Benchmarks: [[AutoVI]]
- Domains: [[Automotive manufacturing]]
- Metrics: [[AU-ROC]], [[Average precision]], [[Area Under Saturated Per-Region Overlap]]
- Concepts: [[Surface defect detection]], [[Industrial visual inspection]]

## Paper Type

Benchmark paper. The paper introduces a dataset and uses it to evaluate established unsupervised visual anomaly-detection methods under real industrial acquisition conditions.

## Problem

Public visual anomaly-detection datasets often use laboratory or controlled acquisition conditions. The paper argues that these settings do not capture real assembly-line variability such as lighting changes, vibration, object positioning shifts, operators in the scene, and large surrounding scene variation. The benchmark asks whether current unsupervised methods trained only on non-defective images can detect and segment real automotive inspection defects under these conditions.

## Contribution

- Introduces [[AutoVI]], a public automotive visual inspection benchmark with six inspection tasks captured on real assembly lines.
- Evaluates CFlow, DRAEM, DSR, EfficientAD, PaDiM, and Patchcore on AutoVI using image-level and pixel-level metrics.
- Analyzes how real-world factors such as scene complexity, defect size, logical defects, crop/window size, data augmentation, and few-shot training affect method performance.
- Releases the dataset, experiment code, and evaluation code.

## Dataset

[[AutoVI]] contains six categories:

| Category | Image size | Train | Test OK | Test defective | Total |
|---|---:|---:|---:|---:|---:|
| engine_wiring | 400 x 400 | 285 | 285 | 322 | 892 |
| pipe_clip | 400 x 400 | 195 | 196 | 141 | 532 |
| pipe_staple | 400 x 400 | 198 | 199 | 127 | 524 |
| tank_screw | 1000 x 750 | 318 | 318 | 95 | 731 |
| underbody_pipes | 1000 x 750 | 161 | 161 | 184 | 506 |
| underbody_screw | 1000 x 750 | 373 | 374 | 18 | 765 |
| Total | not applicable | 1530 | 1533 | 887 | 3950 |

Images were captured on assembly lines of a single factory. The cameras stayed fixed during shooting while items moved on the assembly line. All categories except engine_wiring used 50 mm focal lengths; engine_wiring used 25 mm. Test anomalies were deliberately built upstream on the assembly line without changing shooting conditions, then corrected after shooting.

The dataset includes both structural and logical defects. Logical defects include incorrectly fastened cables and misplaced blue hoops in engine_wiring, and missing items in pipe_staple, tank_screw, and underbody_screw. Segmentation masks are defined with saturation thresholds so that logical defects can be evaluated without forcing a model to segment every plausible context pixel.

## Method

The benchmark tests six representative unsupervised anomaly-detection methods:

- CFlow, a normalizing-flow method.
- DRAEM, a reconstruction-based method trained with synthetic defects.
- DSR, a reconstruction method using discretized latent-space representations.
- EfficientAD, a student-teacher plus autoencoder method.
- PaDiM, a patch-distribution method using multivariate Gaussian modeling of pretrained features.
- Patchcore, a patch-memory method based on distances from pretrained patch features to a memory bank.

All implementations come from Anomalib. CFlow is used because CS-Flow was unavailable at test time. EfficientAD-M is used for its stronger reported AUROC on MVTec AD and MVTec LOCO.

## Evidence

The main benchmark runs 288 experiments: 8 repetitions for each of 6 methods over 6 AutoVI classes. CFlow is trained for 100 epochs, DRAEM for 700, DSR for 500, EfficientAD for 250, while PaDiM and Patchcore need one training epoch. All methods are trained and evaluated with an Nvidia V100 GPU and 32 GB RAM.

Image-level AUROC means:

| Method | Mean AUROC |
|---|---:|
| CFlow | 51.4 +/- 5.9 |
| DRAEM | 78.6 +/- 10.8 |
| DSR | 79.7 +/- 14.3 |
| EfficientAD | 80.9 +/- 9.8 |
| PaDiM | 71.2 +/- 17.3 |
| Patchcore | 88.4 +/- 10.1 |

Average precision means:

| Method | Mean AP |
|---|---:|
| CFlow | 39.4 +/- 19.0 |
| DRAEM | 64.4 +/- 16.6 |
| DSR | 66.6 +/- 18.0 |
| EfficientAD | 56.1 +/- 24.8 |
| PaDiM | 50.2 +/- 29.7 |
| Patchcore | 72.8 +/- 14.8 |

Pixel-level segmentation by mean AUsPRO:

| Method | Mean AUsPRO |
|---|---:|
| CFlow | 22.6 +/- 24.2 |
| DRAEM | 51.1 +/- 27.6 |
| DSR | 67.2 +/- 20.3 |
| EfficientAD | 60.1 +/- 18.5 |
| PaDiM | 53.9 +/- 24.8 |
| Patchcore | 68.9 +/- 20.0 |

The best AutoVI mean AUROC, 88.4% from Patchcore, is lower than the best reported AUROCs on MVTec AD, MVTec LOCO, and VisA reported in the paper: 99.1%, 90.7%, and 98.1%, all from EfficientAD.

### Performance Metrics

- Image-level operational metrics: false positive rate and false negative rate map directly to non-defective items flagged as defective and defective items missed by the inspection system.
- Threshold protocol: the paper reports TPR at fixed TNR values of 99%, 95%, and 90%, using thresholds derived from the normal-only training set rather than test defects.
- Threshold-agnostic image metrics: [[AU-ROC]] is used for comparison under different defect prior probabilities; [[Average precision]] is used because AutoVI has class imbalance between defective and non-defective populations.
- Pixel-level metric: [[Area Under Saturated Per-Region Overlap]] is used for segmentation, with sPRO curves computed up to a pixel false-positive-rate threshold of 5%.
- Best mean image-level result: Patchcore reaches 88.4 +/- 10.1 AUROC and 72.8 +/- 14.8 AP across the six AutoVI classes.
- Best mean pixel-level result: Patchcore reaches 68.9 +/- 20.0 AUsPRO, narrowly above DSR at 67.2 +/- 20.3.
- High-confidence operating point example: Patchcore reaches 98.3% TPR on underbody_pipes at 99% TNR and reaches more than 99% TPR at 95% TNR for two classes.
- Training and evaluation speed: all tested methods train in under 10 hours and evaluate at less than one second per image; PaDiM and Patchcore train in under one minute in the reported setup.

## ML/DL Extraction

- Task formulation: unsupervised image-level anomaly detection and pixel-level anomaly segmentation from normal-only training images.
- Inputs: production-line visual inspection images from six automotive assembly tasks.
- Outputs: anomaly scores, heatmaps, binary defect decisions, and segmentation masks.
- Supervision: training uses non-defective images only; defective test images and masks are used for evaluation.
- Baselines: CFlow, DRAEM, DSR, EfficientAD, PaDiM, and Patchcore.
- Evaluation metrics: FPR, FNR, TPR at fixed TNR, [[AU-ROC]], [[Average precision]], and [[Area Under Saturated Per-Region Overlap]].
- Training recipe: CFlow uses 100 epochs, DRAEM 700, DSR 500, EfficientAD 250, while PaDiM and Patchcore require one training epoch.
- Additional experiments: Gaussian-noise and rotation augmentation generally lowers mean AUROC; crop/window-size changes mostly affect small-defect categories; few-shot Patchcore usually performs worse except for the simple underbody_pipes class; EfficientAD improves on several classes when response normalization uses the full training set.
- Compute: Nvidia V100 GPU with 32 GB RAM.
- Artifacts: dataset, paper experiment code, and evaluation code are public.

## Limitations

- Existing methods are not robust across all six AutoVI tasks.
- Logical defects remain difficult, especially engine_wiring defects that require global structural reasoning.
- Small defects in complex scenes are difficult for patch-memory methods because defective patches can resemble nominal local structure.
- Real production variability causes false positives and weak anomaly heatmaps.
- Few-shot configurations usually reduce AUROC substantially unless the scene is simple and structurally stable.
- Further evaluation on lower-tier embedded hardware is needed for industrial deployment assumptions.

## Connections

### Shares Dataset

- [[AutoVI]] is introduced and benchmarked by this paper.

### Shares Task

- [[Industrial anomaly detection]] and [[Surface defect detection]] are the primary evaluation tasks.

### Shares Method

- [[Unsupervised anomaly detection]] is the learning setting: models train from non-defective images and detect deviations at test time.
- [[Patch-based anomaly detection]] is important because Patchcore and PaDiM are central baselines and Patchcore gives the best mean AUROC and mean AUsPRO.

### Shares Metric

- [[AU-ROC]] is the main image-level threshold-agnostic classification metric.
- [[Average precision]] is used because the dataset is class-imbalanced.
- [[Area Under Saturated Per-Region Overlap]] evaluates segmentation while accounting for logical-defect regions.

### Application/Domain

- [[Automotive manufacturing]] is the application domain because the images come from Renault Group assembly lines.
- [[Industrial visual inspection]] and [[Surface defect detection]] describe the broader inspection setting.

## Source Anchors

- Paper DOI: [10.1016/j.compind.2024.104151](https://doi.org/10.1016/j.compind.2024.104151)
- Dataset: [https://zenodo.org/records/10459003](https://zenodo.org/records/10459003)
- Experiment code: [https://github.com/phcarval/autovi-paper-code](https://github.com/phcarval/autovi-paper-code)
- Evaluation code: [https://github.com/phcarval/autovi_evaluation_code](https://github.com/phcarval/autovi_evaluation_code)

## Questions

- Which model changes would improve logical-defect detection without sacrificing structural-defect sensitivity?
- How do the benchmarked methods perform on embedded industrial hardware rather than a V100 GPU?
