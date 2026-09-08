---
title: Negative performance effects of image data augmentation
aliases:
  - Augmentation can worsen image ML performance
  - Negative results from synthetic image data
tags:
  - literature-synthesis
  - data-augmentation
  - synthetic-data
---

# Negative performance effects of image data augmentation

Image augmentation and synthetic-data generation can reduce downstream performance when a transformation is unsuitable, a synthetic-to-real ratio is too high, or generated data shifts the training distribution away from the real evaluation distribution. The evidence is conditional: most retained papers also report settings, models, classes, or metrics where augmentation helps.

## Inclusion rule

A result is retained only when it provides:

1. a public or traceably accessible image dataset;
2. a numerical baseline and post-augmentation result;
3. an isolated training-data intervention rather than a model change; and
4. at least one degraded evaluation metric.

Results are excluded when the comparison changes architectures, lacks an unaugmented control, augments the test set without a fixed-test comparison, uses inaccessible data, or concerns point clouds, time series, adversarial attacks, or inference-time processing rather than image training-data augmentation.

## Findings at a glance

| Evidence | Dataset / domain | Intervention | Baseline → augmented result | Largest reported decrease | Evidence status |
|---|---|---|---|---:|---|
| [[2023 - ALADA A Lite Automatic Data Augmentation Framework for Industrial Defect Detection]] | [[Tianchi-TILE]]; ceramic-tile detection | Random brightness | RetinaNet mAP: 54.27% → 53.01% | -1.26 points (-2.32%) | Matched detector and dataset; Table 10 |
| [[2024 - Detecting Visual Anomalies in an Industrial Environment Unsupervised Methods Put to the Test on the AutoVI Dataset]] | [[AutoVI]]; automotive anomaly classification | ±15° rotation and Gaussian noise | DSR mean AUROC: 79.7% → 73.4% | -6.3 points (-7.9%) | Augmented mean calculated from Table 11; Tables 6 and 11 |
| [[2024 - Latent Diffusion Models to Enhance the Performance of Visual Defect Segmentation Networks in Steel Surface Inspection]] | [[NEU-SEG]]; steel segmentation | LoRA Stable Diffusion images, 84% synthetic | DeepLabV3+ mIoU: 71.31% → 66.12% | -5.19 points (-7.28%) | Fixed model and ratio-controlled experiment; Table 3 |
| [[2024 - Open Stamped Parts Dataset]] | [[Open Stamped Parts Dataset]]; automotive hole detection | CUT translation of simulated images | Precision: 94.4 → 73.1; modified recall: 67.2 → 58.7 | Precision -21.3 (-22.56%) | Added translation stage worsens all reported metrics |
| [[2025 - Enhancing Glass Defect Detection with Diffusion Models]] | [[MVTec AD]] bottle; glass classification | 60 DDPM defects added to 63 real defects | MobileNetV2 accuracy: 0.9012 → 0.8586 | -0.0426 (-4.73%) | Same classifier; Table 3 |
| [Low-data unsupervised visual inspection](https://arxiv.org/abs/2106.01277) | [[MVTec AD]] | Ten augmentations per original | Ledoit mean AUC: 0.962 → 0.959 | -0.003 (-0.31%) | Small aggregate decrease at maximum sample size; Table 7 |
| [Adjacent Image Augmentation](https://doi.org/10.3390/s24175616) | [[MVTec AD]] | Mosaic synthetic negatives | Zipper AUROC: 0.867122 → 0.773897 | -0.093225 (-10.75%) | Four categories decline; Table 5 |
| [Thermal-image quality-metric augmentation](https://doi.org/10.51408/1963-0125) ([OpenAlex](https://openalex.org/W4406441148)) | [[InfraredSolarModules]] | Geometry plus brightness | SqueezeNet accuracy: 88.10% → 86.17% | -1.93 points | Weaker causal evidence: validation and test sets are also augmented |
| [SynSur](https://arxiv.org/abs/2604.26633) ([OpenAlex](https://openalex.org/W7158590397)) | [[BSData]]; metal inspection | Flux.1-dev defects, 75% synthetic | LW-DETR AP: 0.666 → 0.611 | -0.055 (-8.26%) | Fixed test set; mean ± SD over three runs; Table 4 |
| [SynSur](https://arxiv.org/abs/2604.26633) ([OpenAlex](https://openalex.org/W7158590397)) | [[MSD]] scratch subset; glass inspection | Flux.1-dev scratches, 75% synthetic | YOLOv26 AP: 0.953 → 0.872 | -0.081 (-8.50%) | Fixed 80-image test set; no repeated-run uncertainty; Table 5 |

## Evidence details and caveats

### Transformation-specific harm

- **Brightness on Tianchi-TILE:** ALADA reports that brightness reduces RetinaNet mAP from 54.27% to 53.01%. Rotation and ALADA improve this dataset, and brightness improves [[GC10-DET]] and [[NEU-DET]], so the result is transformation- and dataset-specific.
- **Rotation and noise on AutoVI:** DSR declines, while CFlow, DRAEM, and partly EfficientAD benefit; PaDiM and PatchCore are largely unchanged. The 73.4% augmented mean is calculated from six class AUROCs.
- **Mosaic negatives on MVTec AD:** zipper, screw, hazelnut, and toothbrush AUROC decline by 8.29%–10.75% relative. Other synthetic-negative methods and categories improve.

### Excessive synthetic proportions

- **NEU-SEG:** DeepLabV3+ peaks at 37% synthetic data with 76.20% mIoU, then falls to 66.12% at 84% synthetic and 63.80% under synthetic-only training. The paper attributes high-ratio degradation to erroneous or confusing generated features.
- **BSData:** with 25% real and 75% synthetic data, YOLOv26 AP falls from 0.652 ± 0.006 to 0.602 ± 0.023 and recall from 0.854 ± 0.035 to 0.763 ± 0.039. LW-DETR AP falls from 0.666 ± 0.011 to 0.611 ± 0.015; AP50, AP75, and AR100 also decline.
- **MSD scratches:** the 75/25 and 50/50 real/synthetic mixtures also reduce every reported metric. Synthetic annotations use inpainting masks because SAM 3 did not delineate scratches reliably, introducing a plausible label-noise mechanism.
- **Evidence maturity:** SynSur is a zero-citation 2026 preprint, below the usual 25-citation screening threshold. Its controlled ratios are informative but require replication.

### Imperfect synthetic-to-real translation

- **Open Stamped Parts:** CUT translation reduces recall by 5.6 points, modified recall by 8.5 points, and precision by 21.3 points. The baseline is already simulation-generated, so this isolates harm from an added translation stage rather than synthetic data versus real-only training.
- **MVTec bottle DDPM:** MobileNetV2 accuracy declines, but recall, F1, and AUROC improve and precision is unchanged. Differing validation class distributions weaken any broad interpretation.
- **InfraredSolarModules:** ResNet50, SqueezeNet, and MobileNetV3 accuracy decline by 1.37, 1.93, and 0.93 points. Because augmentation is applied to validation and test sets as well as training data, this is retained as weaker evidence rather than a clean fixed-test causal comparison. OpenAlex reports one citation.

## Interpretation

The literature does not support a general claim that augmentation is harmful. It supports a narrower conclusion:

- augmentation policy must match the physical invariances of the task;
- synthetic data has an optimal range rather than a monotonic benefit;
- generated labels and domain translation can introduce noise or distribution shift;
- aggregate gains can conceal model-, class-, or metric-specific losses; and
- fixed real test sets and ratio-controlled ablations provide the strongest evidence.

## Domain search coverage

### Multi-industry anomaly detection

- **Public scope:** [[Bosch Production Line Performance]], [[Bosch Surface Defect Inspection Dataset]], [[BTAD]], [[Bottle-Cap Dataset]], [[DAGM2007]], [[Defect Spectrum]], [[Industrial-5i]], [[MVTec AD]], [[MVTec AD 2]], [[MVTec Caption]], [[MVTec LOCO AD]], [[MVTec3D]], [[Real-IAD]], [[VisA]], and [[Workpiece surface defect dataset]].
- **Retained:** two external MVTec AD results.
- **Excluded:** Bosch Production Line Performance is tabular. Other studies reported gains, changed methods without an unaugmented control, modified inference rather than training, or lacked a numerical negative pair.

### Semiconductor and electronics

- **Public scope:** [[DeepPCB]], [[DsPCBSD+]], [[Heat Sink Surface Defect Dataset]], [[HRIPCB]], [[MixedWM38]], and [[WM-811K]]. [[SSGD]] belongs to [[Glass inspection]].
- **Retained:** none.
- **Notable exclusion:** [WM-811K class-imbalance study](https://doi.org/10.9717/kmms.2025.28.10.1576) compares rotation-based oversampling levels, but the accessible material does not expose the numerical tables required to prove a decrease.

### Solar cells and photovoltaic

- **Public scope:** [[Dataset of Solar Cells Defect Segmentation]], [[ELPV Dataset]], [[EL-2019]], [[PV Panel Defect Dataset]], [[PVEL-AD]], [[SolarDK]], [[PV-IV-EL]], [[InfraredSolarModules]], [[Thermal PV Panel Detection and Fault Detection Dataset for UAV-Based Inspection]], [[BenchmarkELimages]], and [[PV-Multi-Defect]].
- **Retained:** one weaker InfraredSolarModules result.
- **Excluded:** remaining studies reported improvements, lacked matched baselines, used datasets outside this scope, or were already represented.

### Metal inspection

- **Public scope:** [[APDDD]], [[BSData]], [[CSDD]], [[GC10-DET]], [[HSS-IAD]], [[KolektorSDD]], [[KolektorSDD2]], [[LoHi-WELD]], [[Magnetic Tile Defects]], [[MPDD]], [[MPDD2]], [[NEU-CLS]], [[NEU-DET]], [[Tianchi aluminium profile surface defect dataset]], [[NEU-SEG]], [[MSDD]], [[Severstal Steel Defect Dataset]], [[X-SDD]], and [[Metal Surface Defects Dataset]].
- **Retained:** SynSur on BSData and the represented NEU-SEG diffusion study.
- **Excluded:** other studies reported only improvements, lacked a matched control, or included augmentation in every condition.

### Textile and fiber inspection

- **Public scope:** [[Batavia and Sarga woven fabric images]], [[CottonSFDG]], [[DME Fabric Defect Detection Dataset]], [[FD_Dataset]], [[FabricSpotDefect]], [[Lusitano]], [[AITEX]], [[TILDA]], and [[ZJU-Leaper]]. [[LaceCls]] and the [[Woven fabric defect dataset]] have unspecified availability.
- **Retained:** none.
- **Notable exclusions:** the [AITEX augmentation study](https://doi.org/10.1007/978-3-662-66769-9_6) has no unaugmented training pipeline; the [FabricSpotDefect transformer study](https://doi.org/10.1016/j.isci.2025.114411) improves every reported metric; ZJU-Leaper data augmentation improves all three U-Net F1 measures relative to no augmentation.

### Glass inspection

- **Public scope:** [[AGDD]], [[Glass Defects]], [[Glass Bangle Defect Detection Classification]], [[MSD]], [[MVEP]], and [[SSGD]]. [[AuGD]] is private; [[BBMP]], [[CGD]], [[Mobile Phone Flat Glass Defect Dataset]], [[OGD-DET]], and [[RSGD]] have unspecified availability.
- **Retained:** SynSur on the MSD scratch subset.
- **Excluded:** AGDD and SSGD studies augment every training condition or isolate model components; bangle studies lack an unaugmented control; Glass Defects and MVEP lack qualifying downstream comparisons.
- **Boundary:** the represented MVTec bottle result is glass-related but remains canonically associated with [[Multi-industry anomaly detection]].

### Automotive

- **Public scope:** [[CarDD]], [[AutoVI]], [[Structural Adhesive Defects Dataset]], [[Open Stamped Parts Dataset]], [[RSW gun fault prediction benchmark dataset]], [[KITTI]], and the [[SDR synthetic vehicle dataset]] across [[Automotive damage assessment]], [[Automotive manufacturing]], and [[Autonomous driving]].
- **Retained:** AutoVI and Open Stamped Parts.
- **Excluded:** [[2026 - GiPL Generative augmented iterative Pseudo-Labeling for Cross-Domain Few-Shot Object Detection]] improves CarDD results; structural-adhesive studies improve real-test mAP; KITTI camera-data mixtures improve 2D detection. KITTI negative results found for LiDAR, adversarial perturbation, or synthetic-only replacement conditions are outside the image-augmentation criterion. The RSW dataset is time-series data, and the SDR study predates the default 2020 window.

## Source pages

- [[2023 - ALADA A Lite Automatic Data Augmentation Framework for Industrial Defect Detection]]
- [[2024 - Detecting Visual Anomalies in an Industrial Environment Unsupervised Methods Put to the Test on the AutoVI Dataset]]
- [[2024 - Latent Diffusion Models to Enhance the Performance of Visual Defect Segmentation Networks in Steel Surface Inspection]]
- [[2024 - Open Stamped Parts Dataset]]
- [[2025 - Enhancing Glass Defect Detection with Diffusion Models]]
