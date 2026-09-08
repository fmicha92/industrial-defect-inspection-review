---
title: "Multimodal Industrial Anomaly Detection via Hybrid Fusion"
aliases:
  - "M3DM"
  - "Multi-3D-Memory"
paper_key: "doi:10.1109/cvpr52729.2023.00776"
paper_type: research
year: 2023
venue: "CVPR 2023"
authors:
  - "Yue Wang"
  - "Jinlong Peng"
  - "Jiangning Zhang"
  - "Ran Yi"
  - "Yabiao Wang"
  - "Chengjie Wang"
status: processed
processed_at: 2026-05-22
topics:
  - "multimodal anomaly detection"
  - "RGB-D inspection"
  - "memory banks"
tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
domains:
  - "[[Multi-industry anomaly detection]]"
datasets:
  - "[[MVTec3D]]"
methods:
  - "[[Multi-3D-Memory]]"
  - "[[Unsupervised anomaly detection]]"
  - "[[Vision Transformer]]"
  - "Point Transformer"
model_family:
  - "memory bank anomaly detection"
  - "multimodal feature fusion"
metrics:
  - "[[AU-ROC]]"
  - "[[AU-PRO]]"
primary_metric: "[[AU-PRO]]"
optimizers:
  - "[[AdamW]]"
baselines:
  - "PatchCore"
  - "BTF"
  - "3D-ST"
  - "FPFH-based methods"
  - "AST"
code: "reported available: https://github.com/nomewang/M3DM"
data: "[[MVTec3D]]"
doi: "10.1109/CVPR52729.2023.00776"
arxiv: "not reported"
url: "https://doi.org/10.1109/CVPR52729.2023.00776"
pdf: "paper-inbox/10_processed/Research/2023 - Wang - Multimodal Industrial Anomaly Detection via Hybrid Fusion.pdf"
source_file: "paper-inbox/10_processed/Research/2023 - Wang - Multimodal Industrial Anomaly Detection via Hybrid Fusion.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2023 - Wang - Multimodal Industrial Anomaly Detection via Hybrid Fusion.md"
extracted_text: "paper-inbox/90_processing/text/2023 - Wang - Multimodal Industrial Anomaly Detection via Hybrid Fusion.txt"
artifact_status: "code reported available"
tags:
  - "paper"
  - "multimodal-anomaly-detection"
  - "rgb-d-inspection"
---

# Multimodal Industrial Anomaly Detection via Hybrid Fusion

## Summary

- The paper proposes [[Multi-3D-Memory]] (M3DM), a multimodal anomaly detection method for RGB images and 3D point clouds.
- M3DM uses patch-wise contrastive feature fusion, separate memory banks for RGB, 3D, and fused features, decision-layer fusion, and point feature alignment.
- On [[MVTec3D]], the paper reports 0.945 mean image-level AUROC and 0.964 mean AUPRO in the RGB + 3D setting.

## Paper Type

Research paper. It contributes an unsupervised RGB + 3D anomaly detection method and evaluates it on image-level anomaly detection and anomaly segmentation.

## Problem

Industrial inspection often has many normal examples but few defect examples. RGB-only methods can miss shape anomalies, while direct concatenation of RGB and 3D features can disturb the feature distribution and reduce detection performance.

## Contribution

- Proposes [[Multi-3D-Memory]], a hybrid fusion method for multimodal industrial anomaly detection.
- Introduces Unsupervised Feature Fusion (UFF), trained with patch-wise contrastive loss to learn interactions between RGB and point-cloud patches.
- Uses Decision Layer Fusion (DLF) with separate memory banks for RGB, point-cloud, and fused features.
- Adds Point Feature Alignment (PFA) to map 3D point features into a 2D plane aligned with RGB features.

## Method

M3DM takes an RGB image and point cloud as input. RGB features come from a DINO-pretrained ViT-B/8 model at 224 x 224 resolution, yielding 784 patch features with 768 dimensions. Point-cloud features come from a ShapeNet-pretrained Point Transformer using layer outputs {3, 7, 11}. Point Feature Alignment interpolates point features and projects them into the 2D image plane.

Unsupervised Feature Fusion fuses aligned RGB and point features with patch-wise contrastive loss. Decision Layer Fusion builds three memory banks, one each for RGB, point-cloud, and fused features, and combines their anomaly scores and segmentation maps.

## Dataset and Preprocessing

The paper evaluates on [[MVTec3D]], described as 10 categories with 2656 training samples and 1137 testing samples. Each sample contains RGB information and 3D coordinate tensors that can be mapped to a colored point cloud.

For preprocessing, M3DM estimates the background plane with RANSAC, removes points within 0.005 distance of that plane, and sets corresponding RGB pixels to 0. RGB images and position tensors are resized to 224 x 224.

## Evidence

| Evidence | Reported detail |
|---|---|
| Dataset | [[MVTec3D]] / MVTec-3D AD |
| Training setting | Unsupervised normal-only training |
| Feature extractors | DINO-pretrained ViT-B/8 for RGB; ShapeNet-pretrained Point Transformer for 3D |
| UFF training | AdamW, learning rate 0.003, cosine warm-up over 250 steps, batch size 256, best result under 750 training steps |
| DLF training | Two linear OCSVMs with SGD, learning rate 1e-4, 1000 steps per class |
| Best RGB + 3D result | 0.945 mean I-AUROC and 0.964 mean AUPRO |
| Code | https://github.com/nomewang/M3DM |

## Performance Metrics

Primary metric: [[AU-PRO]] for segmentation. The paper also reports image-level AUROC (I-AUROC) and pixel-level AUROC (P-AUROC). Higher is better for all reported metrics.

| Setting | I-AUROC | AUPRO | P-AUROC | Notes |
|---|---:|---:|---:|---|
| Point cloud only | 0.874 | 0.906 | 0.970 | Highest pure-3D I-AUROC reported; AUPRO affected by point-cloud/label bias. |
| RGB only | 0.850 | 0.942 | 0.987 | Uses transformer RGB features instead of original PatchCore Wide-ResNet features. |
| RGB + 3D, PatchCore + FPFH | 0.865 | AUPRO absent from extracted table | 0.992 | Strong P-AUROC but lower image-level detection. |
| RGB + 3D, AST | 0.937 | AUPRO absent from extracted table | 0.976 | AST reports P-AUROC in the extracted comparison. |
| RGB + 3D, M3DM | 0.945 | 0.964 | 0.992 | Best reported multimodal I-AUROC and AUPRO. |

### Fusion Ablation

| Variant | Memory banks | I-AUROC | AUPRO | P-AUROC |
|---|---|---:|---:|---:|
| Only point cloud | Mpt | 0.874 | 0.906 | 0.970 |
| Only RGB | Mrgb | 0.850 | 0.942 | 0.987 |
| Direct concat without UFF | Mfs | 0.857 | 0.944 | 0.987 |
| UFF single fused bank | Mfs | 0.898 | 0.956 | 0.990 |
| Two banks without DLF | Mrgb, Mpt | 0.929 | 0.953 | 0.987 |
| Two banks with DLF | Mrgb, Mpt | 0.932 | 0.959 | 0.990 |
| Full M3DM | Mrgb, Mpt, Mfs | 0.945 | 0.964 | 0.992 |

UFF adds 0.041 I-AUROC, 0.012 AUPRO, and 0.003 P-AUROC over direct concatenation in the single-fused-bank comparison. DLF adds 0.003 I-AUROC, 0.006 AUPRO, and 0.003 P-AUROC over direct two-bank score addition.

## Reproducibility and Artifacts

- Code: https://github.com/nomewang/M3DM.
- Data: [[MVTec3D]].
- UFF optimizer: [[AdamW]].
- DLF optimizer: SGD for linear OCSVM modules.
- Feature extractors: DINO-pretrained ViT-B/8 and ShapeNet-pretrained Point Transformer.

## Limitations

- The method uses multiple memory banks, which later work identifies as a source of memory and inference-time cost.
- The source discusses a bias between point clouds and ground-truth labels: missing regions may be annotated as anomalies, but pure point-cloud methods cannot report anomaly scores for non-point regions.
- AUPRO is not reported for AST in the extracted source, so the paper compares AST segmentation using P-AUROC.

## Connections

### Graph Hubs

- Tasks: [[Industrial anomaly detection]], [[Defect segmentation]]
- Methods: [[Multi-3D-Memory]], [[Unsupervised anomaly detection]], [[Vision Transformer]], Point Transformer
- Datasets: [[MVTec3D]]
- Domains: [[Multi-industry anomaly detection]]
- Metrics: [[AU-ROC]], [[AU-PRO]]

### Related Papers and Concepts

| Target | Relationship | Rationale |
|---|---|---|
| [[MVTec3D]] | Shares dataset | M3DM is evaluated on RGB and point-cloud data from MVTec 3D-AD. |
| [[2024 - Multimodal Industrial Anomaly Detection by Crossmodal Feature Mapping]] | Contrasts with | Both use RGB and 3D data, but Crossmodal Feature Mapping explicitly targets the memory/time cost of memory-bank approaches like M3DM. |
| [[2024 - Cheating Depth Enhancing 3D Surface Anomaly Detection via Depth Simulation]] | Follow-up reading | Cheating Depth cites M3DM as a strong point-cloud-backed 3D anomaly detection method and targets faster depth representations. |

## Questions

- Which MVTec-3D categories contribute most to the RGB + 3D gain over RGB-only and point-cloud-only settings?
- How large are the three memory banks under industrial-scale training data?
