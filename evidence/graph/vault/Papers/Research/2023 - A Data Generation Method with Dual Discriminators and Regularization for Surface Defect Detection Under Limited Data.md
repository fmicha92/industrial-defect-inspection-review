---
title: "A Data Generation Method with Dual Discriminators and Regularization for Surface Defect Detection Under Limited Data"
aliases:
  - "A Data Generation Method with Dual Discriminators and Regularization for Surface Defect Detection Under Limited Data"
paper_key: "sha256:b5bf9b951bcb7a7ee05f2972337e76e762d85c14041c047720e7cde20259dcb2"
paper_type: research
year: 2023
venue: "Computers in Industry"
authors:
  - "Boheng Liu"
  - "Tianrui Zhang"
  - "Yao Yu"
  - "Ligang Miao"
status: processed
processed_at: 2026-05-22
topics:
  - "limited defect data"
  - "dual discriminator GAN"
  - "surface defect image generation"
tasks:
  - "[[Defect detection]]"
  - "[[Defect segmentation]]"
domains:
  - "[[Multi-industry anomaly detection]]"
datasets:
  - "[[GC10-DET]]"
  - "[[NEU-CLS]]"
  - "[[SAPF]]"
methods:
  - "[[Dual-discriminator GAN regularization]]"
  - "[[GAN]]"
  - "[[GAN-based surface defect augmentation]]"
  - "[[Data augmentation]]"
  - "[[Synthetic data generation]]"
model_family:
  - "[[GAN]]"
architectures:
  - "[[Dual-discriminator GAN regularization]]"
  - "DCGAN benchmark model"
metrics:
  - "[[FID]]"
  - "[[Surface Defect Score]]"
  - "[[mAP@0.50]]"
  - "[[mAP]]"
primary_metric: "[[FID]]"
metric_definitions:
  - "FID: lower is better; used for generated image quality"
  - "SDS: higher is better; proposed generated surface defect image metric"
  - "mAP@.5: higher is better; mean average precision at IoU 0.5"
  - "mAP@.5:.95: higher is better; mean mAP over IoU thresholds 0.5 to 0.95"
baselines:
  - "GAN"
  - "LSGAN"
  - "WGAN"
  - "RSGAN"
  - "WGAN-GP"
  - "DIV"
  - "LC-Reg"
benchmarks:
  - "[[GC10-DET]]"
  - "[[NEU-CLS]]"
  - "[[SAPF]]"
code: "not reported"
data: "authors state they do not have permission to share data"
doi: "10.1016/j.compind.2023.103963"
arxiv: "not reported"
url: "https://doi.org/10.1016/j.compind.2023.103963"
pdf: "paper-inbox/10_processed/Research/2023 - Liu - A Data Generation Method with Dual Discriminators and Regularization for Surface Defect Detection Under Limited Data.pdf"
related_concepts:
  - "[[Surface defect detection]]"
  - "[[Industrial visual inspection]]"
related_methods:
  - "[[Dual-discriminator GAN regularization]]"
  - "[[GAN]]"
  - "[[GAN-based surface defect augmentation]]"
  - "[[Data augmentation]]"
  - "[[Synthetic data generation]]"
related_datasets:
  - "[[GC10-DET]]"
  - "[[NEU-CLS]]"
  - "[[SAPF]]"
related_tasks:
  - "[[Defect detection]]"
  - "[[Defect segmentation]]"
related_benchmarks:
  - "[[GC10-DET]]"
  - "[[NEU-CLS]]"
  - "[[SAPF]]"
source_file: "paper-inbox/10_processed/Research/2023 - Liu - A Data Generation Method with Dual Discriminators and Regularization for Surface Defect Detection Under Limited Data.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2023 - Liu - A Data Generation Method with Dual Discriminators and Regularization for Surface Defect Detection Under Limited Data.md"
extracted_text: "paper-inbox/90_processing/text/2023 - Liu - A Data Generation Method with Dual Discriminators and Regularization for Surface Defect Detection Under Limited Data.txt"
artifact_status: "data not shareable by authors"
tags:
  - paper
  - gan
  - surface-defect-detection
  - limited-data
---
# A Data Generation Method with Dual Discriminators and Regularization for Surface Defect Detection Under Limited Data

## Summary

- Proposes a GAN-based surface defect image generation method for limited-data industrial inspection.
- Adds a second discriminator and assigns different regularization terms to the two discriminators so GAN training remains more stable when the discriminator would otherwise overfit scarce defect images.
- Evaluates generated image quality on [[GC10-DET]] and [[NEU-CLS]], then tests whether generated data improves YOLO-v5 and YOLO-v8 defect detection on [[SAPF]] and [[NEU-CLS]].
- Reports that adding generated NEU-CLS images raises YOLO-v8 mAP@.5 from 82.26 to 97.59 with a half-sized fake-image supplement.

## Paper Type

Research paper. It proposes a new GAN training architecture and regularization scheme, introduces the SDS metric, constructs the SAPF industrial dataset, and runs comparative generation and detection experiments.

## Problem

- Task: [[Defect detection]] and [[Defect segmentation]] support under limited surface defect images.
- Setting: [[Multi-industry anomaly detection]] across metal surface defects, steel-strip defects, and solar aluminum profile frame defects.
- Input: scarce real surface defect images plus generator noise vectors.
- Output: generated surface defect images used as training data for defect detection models.
- Motivation: fully supervised defect detectors need diverse training data, but improved manufacturing makes defect examples expensive and difficult to collect.

## Contribution

- Claimed: GAN-based augmentation is useful for surface defect detection, but standard GAN training collapses when only limited defect data are available because the discriminator overfits.
- Shown: A dual-discriminator GAN with adaptive regularization stabilizes training and improves generated image quality and diversity on GC10-DET and NEU-CLS.
- Shown: Generated images improve YOLO-v5 and YOLO-v8 detection mAP on SAPF and NEU-CLS when mixed with limited real data.
- Added resource: The paper constructs SAPF, a 150-image solar aluminum profile frame surface defect dataset collected in a real industrial scene, but states the authors do not have permission to share data.

## Method

The method modifies a GAN to use generator G and two discriminators, D1 and D2. D1 receives a regularization term intended to reduce discriminator overfitting to real images under limited data. D2 receives a different regularization term that makes it more sensitive to generated data and discourages the generator from producing simple low-diversity images. An overfitting heuristic lambda adaptively controls regularization strength, with alpha typically set to 0.1.

The theoretical section frames the method as minimizing a proposed L divergence between the real and generated distributions when the discriminators are optimal. The experiments use DCGAN as a benchmark model, 100-dimensional normal noise input, 128 x 128 output images, learning rate 0.0005, batch size 16, and 5k epochs for the main GAN comparisons.

## Data

| Dataset | Role | Source-reported details |
|---|---|---|
| [[GC10-DET]] | Generation benchmark | 3,570 images with 10 metal surface defect types; category counts range from 74 to 569. |
| [[NEU-CLS]] | Generation and detection benchmark | 1,800 grayscale hot-rolled steel strip images with six defect types and 300 samples per type. |
| [[SAPF]] | New industrial detection dataset | 150 solar aluminum profile frame defect images, resolution 1280 x 256; split into 100 train, 25 validation, and 25 test images. |

## Performance Metrics

### Generation Metrics

| Metric | Definition / use | Direction |
|---|---|---|
| [[FID]] | Frechet Perception Distance between generated and real image distributions; the paper adjusts feature dimensionality to 768 for small sample comparisons. | Lower is better |
| [[Surface Defect Score]] | Proposed metric: train ResNet18 to distinguish real from fake defect images, then convert fake-image classification accuracy into a similarity score. | Higher is better |

The paper argues that FID can be misleading for surface defect generation because generated images may receive a good FID even when the defect region disappears. SDS is introduced to better reflect whether fake surface defect images resemble real defect images.

### Detection Metrics

| Metric | Definition / use | Direction |
|---|---|---|
| [[mAP@0.50]] | Mean average precision at IoU threshold 0.5, reported as mAP@.5. | Higher is better |
| [[mAP]] | The paper also reports mAP@.5:.95, averaged over IoU thresholds from 0.5 to 0.95 in steps of 0.05. | Higher is better |

## Main Results

| Experiment | Dataset | Baseline / comparison | Paper result |
|---|---|---|---|
| GAN objective comparison | GC10-DET | GAN, LSGAN, WGAN, RSGAN | The proposed method has the best FID in all 10 defect categories in Table 1. |
| Regularization comparison | NEU-CLS | WGAN-GP, DIV, LC-Reg | The proposed method reports lower average FID than the comparison methods and the best SDS across all listed NEU-CLS defect categories. |
| Ablation | NEU subset with 100 defect images | no R1/R2, R1 only, R2 only | FID improves from 45.63 with neither term to 21.74 with both R1 and R2; SDS improves from 2 to 14. |
| Detection augmentation | SAPF + YOLO-v5 | real images only vs real plus generated | mAP@.5 improves from 96.94 to 99.56 when using twice as many generated images as real images. |
| Detection augmentation | SAPF + YOLO-v8 | real images only vs real plus generated | mAP@.5 improves from 92.41 to 99.51 with a half-sized generated-image supplement. |
| Detection augmentation | NEU-CLS + YOLO-v5 | real images only vs real plus generated | mAP@.5 improves from 88.24 to 94.25 with twice as many generated images as real images. |
| Detection augmentation | NEU-CLS + YOLO-v8 | real images only vs real plus generated | mAP@.5 improves from 82.26 to 97.59 with a half-sized generated-image supplement. |

## Limitations

- Data are not shareable according to the paper's data availability statement.
- The paper notes a threshold effect: adding more generated images does not always further improve the detector.
- The authors attribute the threshold to limited GAN generation ability and generated small defects that may not align with test-image annotations.
- SAPF is small, with 100 training, 25 validation, and 25 test images after manual cleaning.

## Reproducibility

- Code: not reported.
- Data: not shared; authors state they do not have permission to share data.
- Hardware: Intel Core i9-9900 CPU, 32 GB memory, GeForce GTX 3080 10 GB GPU.
- Main GAN settings: PyTorch, DCGAN benchmark model, learning rate 0.0005, batch size 16, 5k epochs, 128 x 128 generated image resolution.
- Detection models: YOLO-v5 and YOLO-v8 with fixed hyperparameters; exact hyperparameters are not fully listed in the extracted text.

## Connections

### Graph Hubs

- Tasks: [[Defect detection]], [[Defect segmentation]]
- Methods: [[Dual-discriminator GAN regularization]], [[GAN]], [[GAN-based surface defect augmentation]], [[Data augmentation]], [[Synthetic data generation]]
- Datasets: [[GC10-DET]], [[NEU-CLS]], [[SAPF]]
- Domains: [[Multi-industry anomaly detection]]
- Metrics: [[FID]], [[Surface Defect Score]], [[mAP@0.50]], [[mAP]]
- Concepts: [[Surface defect detection]], [[Industrial visual inspection]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2023 - DG-GAN A High Quality Defect Image Generation Method for Defect Detection]] | Shares method and setting | Both study GAN-based surface defect image generation for detection support under scarce data. |
| [[2023 - A New Contrastive GAN With Data Augmentation for Surface Defect Recognition Under Limited Data]] | Shares limited-data setting | Both use NEU-CLS and GAN-based augmentation in limited-data surface defect recognition. |
| [[2023 - A Deep-Learning-Based Approach for Aircraft Engine Defect Detection]] | Shares augmentation motivation | Both use GAN-generated defect imagery to address limited defect data, but this paper focuses on multi-industry surface defect generation and YOLO detection. |

## Questions

- Are SAPF annotations or trained YOLO models available through any channel not captured by the paper's data availability statement?
- How robust is SDS when the ResNet18 discriminator is trained with different splits or model capacity?
