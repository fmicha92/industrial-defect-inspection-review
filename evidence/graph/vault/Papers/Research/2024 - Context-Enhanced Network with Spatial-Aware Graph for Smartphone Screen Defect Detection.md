---
title: "Context-Enhanced Network with Spatial-Aware Graph for Smartphone Screen Defect Detection"
aliases:
  - "CE-SGNet paper"
paper_key: "sha256:b06c2180545caeb4f14d5b111a68a06701f2c365a97322822765a9461682487d"
paper_type: research
year: 2024
venue: "Sensors"
authors:
  - "Aili Liang"
  - "Qishan Wang"
  - "Xiaofeng Wu"
status: processed
processed_at: 2026-06-03
topics:
  - "smartphone screen defect detection"
  - "attention mechanism"
  - "graph reasoning"
  - "object detection"
tasks:
  - "[[Smartphone screen glass defect detection]]"
  - "[[Object detection]]"
domains:
  - "[[Glass inspection]]"
  - "[[Semiconductor and electronics]]"
datasets:
  - "[[SSGD]]"
  - "[[DeepPCB]]"
methods:
  - "[[CE-SGNet]]"
  - "[[Adaptive Receptive Field Attention Module]]"
  - "[[Spatial-aware Graph Reasoning Module]]"
  - "[[Faster R-CNN]]"
model_family:
  - "[[Faster R-CNN]]"
architectures:
  - "[[CE-SGNet]]"
metrics:
  - "[[Average precision]]"
  - "[[mAP@0.50]]"
  - "[[mAP@0.75]]"
  - "[[GFLOPs]]"
  - "[[FPS]]"
primary_metric: "[[Average precision]]"
metric_definitions:
  - "AP: average precision over IoU thresholds 0.5 to 0.95 in 0.05 increments."
  - "AP50: average precision at IoU 0.50."
  - "AP75: average precision at IoU 0.75."
  - "APs/APm/APl: AP for small, medium, and large objects."
baselines:
  - "Faster R-CNN"
  - "Cascade R-CNN"
  - "RetinaNet"
  - "FCOS"
  - "ATSS"
  - "GFL"
  - "YOLOv5-s"
  - "DETR"
  - "Deformable DETR"
benchmarks:
  - "[[SSGD benchmark]]"
code: "not reported"
data: "SSGD and PCB datasets are used; data presented in the study are available on request from the corresponding author."
doi: "10.3390/s24113430"
url: "https://doi.org/10.3390/s24113430"
pdf: "paper-inbox/10_processed/Research/2024 - Liang - Context-Enhanced Network with Spatial-Aware Graph for Smartphone Screen Defect Detection.pdf"
related_papers:
  - "[[2023 - SSGD A Smartphone Screen Glass Dataset for Defect Detection]]"
  - "[[2025 - Smartphone Screen Surface Defect Detection Using Dynamic Large Separable Kernel Attention]]"
related_concepts:
  - "[[Surface defect detection]]"
  - "[[Industrial visual inspection]]"
related_methods:
  - "[[CE-SGNet]]"
  - "[[Adaptive Receptive Field Attention Module]]"
  - "[[Spatial-aware Graph Reasoning Module]]"
related_datasets:
  - "[[SSGD]]"
  - "[[DeepPCB]]"
related_domains:
  - "[[Glass inspection]]"
  - "[[Semiconductor and electronics]]"
related_tasks:
  - "[[Smartphone screen glass defect detection]]"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2024 - Liang - Context-Enhanced Network with Spatial-Aware Graph for Smartphone Screen Defect Detection.md"
extracted_text: "paper-inbox/90_processing/text/2024 - Liang - Context-Enhanced Network with Spatial-Aware Graph for Smartphone Screen Defect Detection.txt"
---

# Context-Enhanced Network with Spatial-Aware Graph for Smartphone Screen Defect Detection

## Summary

Liang, Wang, and Wu propose CE-SGNet for smartphone screen defect detection. The method extends a Faster R-CNN plus FPN baseline with adaptive receptive-field attention and spatial-aware graph reasoning to improve detection of small, irregular, low-contrast defects.

## Paper Type

Research paper. It proposes a detector architecture and evaluates it on smartphone screen glass and PCB defect datasets.

## Problem

Smartphone screen defects are often small, irregular, low contrast, and visually close to the background. General object detectors can over-focus on background pixels, miss tiny defects, or treat region proposals independently without using relationships among defect regions.

## Contribution

- Introduces [[Adaptive Receptive Field Attention Module]], combining channel attention and spatial selection attention to capture defect-specific contextual regions.
- Introduces [[Spatial-aware Graph Reasoning Module]], which builds a learnable region-to-region graph and updates region features with spatial-aware graph attention.
- Evaluates [[CE-SGNet]] on [[SSGD]] and a PCB dataset, comparing against two-stage, one-stage, anchor-free, YOLO, and Transformer detectors.

## Method

CE-SGNet uses Faster R-CNN with FPN as the baseline. Feature maps are extracted by the backbone, fused by FPN, and reweighted by ARFAM. Region proposals are produced by RPN and RoI Align. SGRM then constructs a region graph from proposal features, classifier weights, and relative spatial positions; graph attention propagates spatial/contextual information between proposal nodes. The enhanced graph features are concatenated with original RoI features for classification and localization.

## Evidence

Datasets:

- [[SSGD]]: 2504 images at 1500 x 1000 pixels, seven defect categories, split into LB101 and LB201 subsets and randomly divided 4:1 into train/test.
- PCB dataset: 693 images, six defect categories, image resolutions from 3056 x 2464 to 2904 x 1521, randomly divided 4:1 into train/test.

SSGD comparison:

| Dataset split | Model | AP | AP50 | AP75 | APs | APm | APl |
|---|---|---:|---:|---:|---:|---:|---:|
| LB101 | Faster R-CNN | 20.3 | 47.3 | 17.0 | 13.4 | 28.2 | 34.4 |
| LB101 | CE-SGNet | 24.0 | 51.2 | 20.3 | 17.5 | 30.3 | 41.9 |
| LB201 | Faster R-CNN | 20.4 | 43.8 | 16.4 | 20.7 | 18.7 | 22.1 |
| LB201 | CE-SGNet | 22.7 | 48.1 | 18.8 | 22.9 | 21.6 | 23.4 |

Ablation on SSGD-LB101:

| Variant | ARFAM | SGRM | AP | AP50 |
|---|---|---|---:|---:|
| Baseline | no | no | 20.3 | 47.3 |
| ARFAM only | yes | no | 22.6 | 50.0 |
| SGRM only | no | yes | 22.3 | 48.1 |
| CE-SGNet | yes | yes | 24.0 | 51.2 |

Generalization to PCB:

| Model | AP | AP50 | AP75 | APs | APm | APl |
|---|---:|---:|---:|---:|---:|---:|
| Faster R-CNN | 52.8 | 96.3 | 50.3 | 35.5 | 52.7 | 47.1 |
| CE-SGNet | 53.8 | 97.0 | 52.7 | 40.0 | 53.7 | 50.8 |

Efficiency comparison reports CE-SGNet at 347.27 GFLOPs, 61.31M parameters, and 7.9 FPS. YOLOv5-s is much faster at 54.2 FPS but lower on the reported AP metrics.

## ML/DL Extraction

- Task formulation: object detection for smartphone screen glass defects and PCB defects.
- Base architecture: Faster R-CNN with ResNet50 backbone and FPN.
- Added modules: ARFAM after FPN; SGRM after RoI Align and before the detection head.
- Optimizer: SGD, momentum 0.9, weight decay 0.05.
- Learning rate: 0.02 initial, reduced by 10x at epochs 8 and 11.
- Batch size: 8.
- Schedule: 12 epochs.
- Pretraining: COCO-pretrained weights for all models.
- Augmentation: random flips and multi-scale training.
- Hardware: 8 NVIDIA GeForce RTX 3090 GPUs.
- Evaluation: COCO-style AP, AP50, AP75, APs, APm, APl; final metrics averaged over five experiments.

## Limitations

- CE-SGNet has high computational cost and a complex model structure: 347.27 GFLOPs, 61.31M parameters, and 7.9 FPS.
- The paper states that real-time deployment may require lightweight acceleration.
- Screen-glass optical properties can make visually perceived defects ambiguous; increasing sensitivity can increase false positives.
- Code availability is not reported.

## Connections

### Graph Hubs

- Tasks: [[Smartphone screen glass defect detection]], [[Object detection]]
- Methods: [[CE-SGNet]], [[Adaptive Receptive Field Attention Module]], [[Spatial-aware Graph Reasoning Module]], [[Faster R-CNN]]
- Datasets: [[SSGD]], [[DeepPCB]]
- Domains: [[Glass inspection]], [[Semiconductor and electronics]]
- Metrics: [[Average precision]], [[mAP@0.50]], [[mAP@0.75]], [[GFLOPs]], [[FPS]]

### Relationship Rationale

- Shares task: [[Smartphone screen glass defect detection]] because the primary experiments are on SSGD smartphone screen glass defects.
- Shares dataset: [[SSGD]] is the main benchmark, evaluated separately on LB101 and LB201.
- Shares dataset: [[DeepPCB]] is used for cross-domain generalization experiments on PCB defects.
- Shares method: [[CE-SGNet]] is the proposed detector.
- Shares method: [[Adaptive Receptive Field Attention Module]] and [[Spatial-aware Graph Reasoning Module]] are the paper's two proposed modules.
- Application/domain: [[Glass inspection]] and [[Semiconductor and electronics]] because smartphone screen glass is an electronics manufacturing inspection target.
- Follow-up reading: [[2023 - SSGD A Smartphone Screen Glass Dataset for Defect Detection]] introduces the main dataset, and [[2025 - Smartphone Screen Surface Defect Detection Using Dynamic Large Separable Kernel Attention]] evaluates a newer YOLO-style detector on SSGD.

## Questions

- Can CE-SGNet be made fast enough for production inspection without losing the AP gains from graph reasoning?
- How much of the SSGD improvement comes from ARFAM context modeling versus SGRM proposal-relationship modeling on each defect class?
