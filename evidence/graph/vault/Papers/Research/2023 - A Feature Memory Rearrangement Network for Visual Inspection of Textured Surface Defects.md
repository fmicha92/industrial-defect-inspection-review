---
title: "A Feature Memory Rearrangement Network for Visual Inspection of Textured Surface Defects Toward Edge Intelligent Manufacturing"
aliases:
  - "Feature Memory Rearrangement Network"
paper_key: "doi:10.1109/tase.2022.3204368"
paper_type: research
year: 2023
venue: "IEEE Transactions on Automation Science and Engineering"
authors:
  - "Haiming Yao"
  - "Wenyong Yu"
  - "Xue Wang"
status: processed
processed_at: 2026-05-20
topics:
  - textured surface inspection
  - anomaly detection
  - edge intelligence
  - background reconstruction
tasks:
  - "[[Surface defect detection]]"
  - "[[Defect segmentation]]"
  - "[[Industrial anomaly detection]]"
domains:
  - "[[Smart manufacturing]]"
  - "[[Multi-industry anomaly detection]]"
datasets:
  - "[[MVTec AD]]"
  - "[[DAGM]]"
  - "[[RSDDs]]"
  - "[[Printed product surface dataset]]"
methods:
  - "[[FMR-Net]]"
  - "[[Unsupervised anomaly detection]]"
  - "[[Unsupervised anomaly localization]]"
  - "[[Synthetic data generation]]"
  - "[[Edge intelligence]]"
model_family:
  - "[[Anomaly Detection Models]]"
architectures:
  - "[[FMR-Net]]"
metrics:
  - "[[AU-ROC|AUC ROC]]"
  - "[[Precision]]"
  - "[[Recall]]"
  - "[[F1-score|F1-measure]]"
  - "[[Inference time|average inference time]]"
primary_metric: "[[AU-ROC]]"
doi: "10.1109/TASE.2022.3204368"
arxiv: "not reported"
related_papers:
  - "[[2023 - Collaborative Discrepancy Optimization for Reliable Image Anomaly Localization]]"
related_concepts:
  - "[[Unsupervised anomaly detection]]"
  - "[[Unsupervised anomaly localization]]"
  - "[[Defect segmentation]]"
  - "[[Synthetic data generation]]"
  - "[[Edge intelligence]]"
related_methods:
  - "[[FMR-Net]]"
  - "[[Unsupervised anomaly detection]]"
  - "[[Unsupervised anomaly localization]]"
  - "[[Synthetic data generation]]"
  - "[[Edge intelligence]]"
related_datasets:
  - "[[MVTec AD]]"
  - "[[DAGM]]"
  - "[[RSDDs]]"
  - "[[Printed product surface dataset]]"
related_tasks:
  - "[[Surface defect detection]]"
  - "[[Defect segmentation]]"
  - "[[Industrial anomaly detection]]"
concept_notes_created_or_updated:
  - "[[FMR-Net]]"
  - "[[Unsupervised anomaly detection]]"
  - "[[Unsupervised anomaly localization]]"
  - "[[MVTec AD]]"
  - "[[Defect segmentation]]"
  - "[[Synthetic data generation]]"
  - "[[Edge intelligence]]"
  - "[[Smart manufacturing]]"
url: "https://doi.org/10.1109/TASE.2022.3204368"
pdf: "paper-inbox/10_processed/Other/2023 - Yao - A Feature Memory Rearrangement Network for Visual Inspection of Textured Surface Defects Toward Edge Intelligent Manufacturing.pdf"
source_file: "paper-inbox/10_processed/Other/2023 - Yao - A Feature Memory Rearrangement Network for Visual Inspection of Textured Surface Defects Toward Edge Intelligent Manufacturing.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2023 - Yao - A Feature Memory Rearrangement Network for Visual Inspection of Textured Surface Defects Toward Edge Intelligent Manufacturing.md"
extracted_text: "paper-inbox/90_processing/text/2023 - Yao - A Feature Memory Rearrangement Network for Visual Inspection of Textured Surface Defects Toward Edge Intelligent Manufacturing.txt"
artifact_status: "processed"
tags:
  - paper
  - anomaly-detection
  - edge-intelligence
  - surface-inspection
---

# A Feature Memory Rearrangement Network for Visual Inspection of Textured Surface Defects

## Summary

- The paper proposes FMR-Net, an unsupervised visual inspection framework for textured surface defects.
- FMR-Net uses synthetic defects during training, a contrastive memory feature module, global feature rearrangement, two-phase training, and multimodal inspection.
- The paper also evaluates edge-cloud deployment via multilevel detection.

## Contribution

- Claimed: FMR-Net can inspect various textured surface defects without real labeled defect samples and is suitable for edge intelligent manufacturing.
- Shown: Experiments compare against AE-SSIM, MemAE, f-AnoGAN, GANomaly, RIAD, MS-FCAE, Lv's method, Uninformed Students, and others on multiple datasets.
- Inferred: The method prioritizes accurate localization and robust reconstruction over being the fastest lightweight model.

## Method

- Encoding module extracts multi-scale textured surface features.
- Contrastive-learning-based memory feature module builds a normal feature memory bank.
- Global feature rearrangement suppresses residual defect reconstruction.
- Decoding module reconstructs normal texture background.
- Multimodal inspection fuses multiple anomaly indications; multilevel inference supports patch-level early exit and pixel-level full inference.

## Evidence

| Evidence | Reported detail |
|---|---|
| Processing efficiency | FMR-Net average inference time reported as 19.1 for 512 x 512 images under the paper's hardware setup |
| MVTec AD texture comparison | FMR-Net reports best comprehensive inspection accuracy across all defect and texture types, with AUC ROC gains over the second-best method on four texture categories and slight underperformance on leather |
| Binarization task | FMR-Net is superior in precision across texture samples and second to AFEAN in recall |
| RSDDs multilevel detection | Patch-level method requires about 1-2 ms, compared with 7-8 ms for pixel-level detection |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Source detail |
|---|---|---|---|---|---|
| [[AU-ROC|AUC ROC]] | MVTec AD texture anomaly detection, ablations, robustness tests, RSDDs, and PPS defects | Area under the ROC curve for positive/negative inspection accuracy | higher | yes | The source names AUC ROC as the mainstream anomaly-detection indicator and primary comparative metric. |
| [[Precision]] | Defect binarization, RSDDs, and PPS inspection | Thresholded detection precision | higher | no | Used with recall and F1-measure because AU-ROC does not reflect fixed-threshold inspection behavior. |
| [[Recall]] | Defect binarization, RSDDs, and PPS inspection | Thresholded detection recall | higher | no | FMR-Net ranks second to AFEAN on recall in the binarization task and slightly trails GANomaly on RSDDs recall. |
| [[F1-score|F1-measure]] | Defect binarization, RSDDs, and PPS inspection | Combined precision/recall score | higher | no | The paper reports F1-measure for thresholded defect inspection comparisons. |
| [[Inference time|average inference time]] | Efficiency comparison and multilevel rail inspection | Runtime per image or patch under stated hardware | lower | no | FMR-Net reports 19.1 AIT for 512 x 512 images; RSDDs patch-level early exit is about 1-2 ms versus 7-8 ms pixel-level inference. |

## Limitations

- For MAGtile microdefects, the paper reports a relatively large gap between FMR-Net and AFEAN due to an insensitive modality response.
- The extracted text does not include complete table values for all compared datasets.
- Edge deployment details are tied to the authors' AOI equipment and NVIDIA Jetson AGX edge nodes.

## Connections

### Graph Hubs

- Tasks: [[Surface defect detection]], [[Defect segmentation]]
- Methods: [[FMR-Net]], [[Unsupervised anomaly detection]], [[Unsupervised anomaly localization]], [[Synthetic data generation]], [[Edge intelligence]]
- Datasets: [[MVTec AD]], [[DAGM]], [[RSDDs]], [[Printed product surface dataset]]
- Domains: [[Smart manufacturing]], [[Multi-industry anomaly detection]], [[Industrial visual inspection]]
- Metrics: [[AU-ROC|AUC ROC]], [[Precision]], [[Recall]], [[F1-score|F1-measure]], [[Inference time|average inference time]]
- Concepts: [[Domain gap]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2023 - Collaborative Discrepancy Optimization for Reliable Image Anomaly Localization]] | Shares task | Both address unsupervised industrial anomaly localization without real labeled defects; this paper uses memory/reconstruction for textured surfaces while CDO optimizes feature discrepancy distributions. |
| [[2022 - Procedural Synthetic Training Data Generation for AI-Based Defect Detection]] | Contrasts with | Both use synthetic defects, but this paper uses them within unsupervised textured anomaly inspection while Schmedemann et al. train a supervised classifier with rendered data. |

### Backlinks Updated

- [[Unsupervised anomaly detection]] links this paper as the FMR-Net textured inspection example.
- [[Unsupervised anomaly localization]] links this paper as a localization/reconstruction example.
- [[FMR-Net]] links this paper as the source paper for the feature-memory rearrangement method.
- [[MVTec AD]] links this paper as an MVTec texture benchmark user.
- [[DAGM]], [[RSDDs]], and [[Printed product surface dataset]] link this paper as an evaluation user.
- [[Defect segmentation]] links this paper as a textured surface segmentation example.
- [[Synthetic data generation]] links this paper for synthetic defects used during unsupervised training.
- [[Edge intelligence]] links this paper as the edge-cloud manufacturing deployment example.

### Concept Notes Created Or Updated

| Concept note | Action | Explanation source |
|---|---|---|
| [[FMR-Net]] | Created | Processed paper source |
| [[Unsupervised anomaly detection]] | Created | Processed paper notes |
| [[Unsupervised anomaly localization]] | Created | Processed paper notes |
| [[MVTec AD]] | Created | Processed paper notes |
| [[Defect segmentation]] | Created | Processed paper notes |
| [[Synthetic data generation]] | Created | Processed paper notes |
| [[Edge intelligence]] | Created | Processed paper note |

## Questions

- How much does each synthetic defect strategy contribute relative to memory rearrangement?
- Are the printed product surface data and deployment code available?
- What failure modes occur under changing illumination or unseen texture families?
