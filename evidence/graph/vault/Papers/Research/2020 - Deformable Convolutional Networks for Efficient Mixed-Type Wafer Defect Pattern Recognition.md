---
title: "Deformable Convolutional Networks for Efficient Mixed-Type Wafer Defect Pattern Recognition"
aliases:
  - "Deformable Convolutional Networks for Efficient Mixed-Type Wafer Defect Pattern Recognition"
paper_key: "doi:10.1109/tsm.2020.3020985"
paper_type: research
year: 2020
venue: "IEEE Transactions on Semiconductor Manufacturing"
authors:
  - "Junliang Wang"
  - "Chuqiao Xu"
  - "Zhengliang Yang"
  - "Jie Zhang"
  - "Xiaoou Li"
status: processed
processed_at: 2026-05-22
topics:
  - "mixed-type wafer defects"
  - "deformable convolution"
  - "multi-label wafer map recognition"
tasks:
  - "[[Wafer map defect classification]]"
domains:
  - "[[Semiconductor and electronics]]"
datasets:
  - "[[MixedWM38]]"
methods:
  - "[[DC-Net]]"
  - "[[Deformable convolution]]"
  - "[[One-hot multi-label wafer defect decoding]]"
model_family:
  - "[[Deep convolutional neural network]]"
architectures:
  - "[[DC-Net]]"
metrics:
  - "[[Accuracy]]"
  - "[[Precision]]"
  - "[[Recall]]"
primary_metric: "[[Accuracy]]"
metric_definitions:
  - "Accuracy: (TP + TN) / (TP + TN + FP + FN)."
  - "Precision: TP / (TP + FP), used to measure false recognition."
  - "Recall: TP / (TP + FN), used to measure missing recognition."
baselines:
  - "Takeshi_CNN"
  - "Kiryong_CNN"
  - "BCNN"
  - "OH-CNN"
benchmarks:
  - "[[MixedWM38]]"
code: "reported available: https://github.com/Junliangwangdhu/WaferMap"
data: "MixedWM38 reported available at https://github.com/Junliangwangdhu/WaferMap"
doi: "10.1109/tsm.2020.3020985"
arxiv: "not reported"
url: "https://doi.org/10.1109/TSM.2020.3020985"
pdf: "paper-inbox/10_processed/Research/2020 - Wang - Deformable Convolutional Networks for Efficient Mixed-Type Wafer Defect Pattern Recognition.pdf"
related_concepts:
  - "[[Surface defect detection]]"
  - "[[Industrial visual inspection]]"
related_methods:
  - "[[DC-Net]]"
  - "[[Deformable convolution]]"
related_datasets:
  - "[[MixedWM38]]"
related_tasks:
  - "[[Wafer map defect classification]]"
source_file: "paper-inbox/10_processed/Research/2020 - Wang - Deformable Convolutional Networks for Efficient Mixed-Type Wafer Defect Pattern Recognition.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2020 - Wang - Deformable Convolutional Networks for Efficient Mixed-Type Wafer Defect Pattern Recognition.md"
extracted_text: "paper-inbox/90_processing/text/2020 - Wang - Deformable Convolutional Networks for Efficient Mixed-Type Wafer Defect Pattern Recognition.txt"
artifact_status: "code and MixedWM38 data reported available"
tags:
  - paper
---
# Deformable Convolutional Networks for Efficient Mixed-Type Wafer Defect Pattern Recognition

## Summary

Wang et al. propose [[DC-Net]] for mixed-type wafer defect pattern recognition, where several single defect patterns can occur on the same wafer map. The model combines deformable convolutional units with a multi-label one-hot output layer that decomposes mixed defects into their underlying basic defect patterns.

The paper evaluates DC-Net on [[MixedWM38]], a 38-class mixed wafer-map dataset with 38,000 wafer maps. DC-Net reports 93.2% average accuracy over C1-C38, 96.80% average accuracy over single-type classes C1-C9, and 92.12% average accuracy over mixed-type classes C10-C38.

## Paper Type

- Type: research.
- Why: The paper contributes a neural architecture and evaluates it against CNN baselines for mixed-type wafer-map defect recognition.

## Problem

- Task: [[Wafer map defect classification]].
- Setting: semiconductor wafer manufacturing systems where wafer test results are stored as wafer maps.
- Inputs: wafer maps containing normal, single-type, or mixed-type defect patterns.
- Outputs: one-hot predictions of the basic single-defect patterns present in the wafer map.
- Motivation: mixed-type defects vary by type, position, angle, and number of component defects, making standard single-label recognition brittle.
- Assumptions: mixed-type defects can be decomposed into combinations of eight basic single defect patterns.

## Contribution

- Claimed: deformable convolution helps sample relevant defect dies while suppressing irrelevant wafer-map regions and noise.
- Shown: one-hot multi-label output reduces the feature space by decomposing mixed classes into basic defect components.
- Shown: DC-Net outperforms Takeshi_CNN, Kiryong_CNN, BCNN, and OH-CNN on MixedWM38.

## Method

DC-Net uses deformable convolutional units to learn sampling offsets over wafer-map features. The deformable units concentrate sampling around defect regions rather than fixed rectangular grids, which is useful when mixed defects overlap or rotate. The output layer uses sigmoid-activated one-hot membership probabilities for eight basic defect categories and a threshold of 0.5 to decide whether each basic defect is present.

## Evidence

### Experimental Setup

- Dataset: [[MixedWM38]].
- Dataset size: 38,000 wafer maps, with 1,000 maps for each of 38 categories.
- Class structure: one normal type, eight single-defect types, 13 two-defect mixed types, 12 three-defect mixed types, and four four-defect mixed types.
- Split: 80% training and 20% validation per category.
- Environment: Python, TensorFlow 1.0, CUDA 8.0, Linux, Intel Xeon E5-2630 v4 CPU, and GeForce RTX 2080 Ti.
- Baselines: Takeshi_CNN, Kiryong_CNN, BCNN, and OH-CNN.

### Main Results

| Result | Dataset / Classes | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| Overall DC-Net accuracy | [[MixedWM38]] C1-C38 | [[Accuracy]] | higher | Takeshi_CNN and Kiryong_CNN lower | 93.2% | 20.68 percentage points higher than Takeshi_CNN and 27.91 percentage points higher than Kiryong_CNN. |
| Single-type DPR | C1-C9 | [[Accuracy]] | higher | Takeshi_CNN and Kiryong_CNN lower | 96.80% | 9.51 points higher than Takeshi_CNN and 31.29 points higher than Kiryong_CNN. |
| Mixed-type DPR | C10-C38 | [[Accuracy]] | higher | Takeshi_CNN and Kiryong_CNN lower | 92.12% | 24.19 points higher than Takeshi_CNN and 26.90 points higher than Kiryong_CNN. |
| Normal wafer class | C1 | [[Accuracy]] | higher | comparison value not stated in extracted text | 99.7% | The paper emphasizes this as important for industrial practice. |
| Ablation comparison | C1-C38 | [[Accuracy]] | higher | OH-CNN 76%; BCNN lower | DC-Net about 93% | OH-CNN is 22 points higher than BCNN; DC-Net improves further through deformable convolution. |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[Accuracy]] | Overall, single-type, and mixed-type wafer DPR | (TP + TN) / (TP + TN + FP + FN) | Higher is better | yes | Headline values are 93.2%, 96.80%, and 92.12%. |
| [[Precision]] | False-recognition analysis | TP / (TP + FP) | Higher is better | no | Average precision and recall are described as very close to 1; all C1-C38 values are above 0.9 except scratch C8 precision. |
| [[Recall]] | Missing-recognition analysis | TP / (TP + FN) | Higher is better | no | Used to evaluate missed wafer defects; exact table values are not preserved in the extracted text. |

## ML / DL Extraction

### Task Formulation

- Input modality: wafer maps.
- Output target: multi-label membership over eight basic defect patterns.
- Supervision: labeled normal, single-type, and mixed-type wafer maps.
- Objective: recognize mixed wafer defect patterns by decomposing them into basic defect components.

### Model And Training

- Model family: [[Deep convolutional neural network]].
- Architecture: [[DC-Net]] with deformable convolutional layers and one-hot multi-label output.
- Activation: sigmoid in the final multi-label output layer.
- Decision threshold: 0.5 for basic defect membership.
- Loss: multi-label training loss is described, but exact extracted formula details are not preserved in this note.
- Optimizer: not reported in the extracted text.
- Seeds: not reported.
- Training compute: GeForce RTX 2080 Ti environment reported.

### Data

- Dataset: [[MixedWM38]].
- Data source: 38 frequently occurring mixed-type defect patterns found from a real semiconductor wafer manufacturing system, supplemented by simulation where some mixed types had insufficient samples.
- Dataset size: 38,000 wafer maps.
- Splits: 80% training, 20% validation.
- Public availability: GitHub URL reported.
- License: not reported.

### Evaluation

- Protocol: compare DC-Net with prior CNN methods and ablation variants on validation splits from MixedWM38.
- Used performance metrics: [[Accuracy]], [[Precision]], [[Recall]].
- Failure cases: scratch C8 has lower precision, especially because C19 edge-loc plus scratch can be misrecognized as scratch when edge-loc is weak and filtered as noise.
- Interpretability: sampling-strength visualizations show red focus around defect locations and blue suppression in less relevant normal regions.

## Dataset / Benchmark Details

- Benchmark: [[MixedWM38]].
- Categories: 38 total.
- Single-type categories: normal plus eight single defects.
- Mixed-type categories: 13 two-defect, 12 three-defect, and four four-defect patterns.
- Samples: 1,000 wafer maps per category.
- Access: reported at `https://github.com/Junliangwangdhu/WaferMap`.
- License: not reported.

## Limitations

- Some MixedWM38 patterns are simulated because real samples for some mixed defects are insufficient.
- Precision for scratch C8 is weaker than other classes.
- The paper reports validation-set performance; external production transfer beyond MixedWM38 is not established in the extracted text.

## Reproducibility

- Code: reported available at `https://github.com/Junliangwangdhu/WaferMap`.
- Data: MixedWM38 reported available at the same GitHub URL.
- Environment: Python, TensorFlow 1.0, CUDA 8.0, Linux, Intel Xeon E5-2630 v4, GeForce RTX 2080 Ti.
- Random seeds: not reported.
- Checkpoints / models: not reported.

## Connections

### Graph Hubs

- Tasks: [[Wafer map defect classification]]
- Methods: [[DC-Net]], [[Deformable convolution]], [[One-hot multi-label wafer defect decoding]]
- Datasets: [[MixedWM38]]
- Benchmarks: [[MixedWM38]]
- Domains: [[Semiconductor and electronics]]
- Metrics: [[Accuracy]], [[Precision]], [[Recall]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2015 - Wafer Map Failure Pattern Recognition and Similarity Ranking for Large-Scale Data Sets]] | Shares task family | Both address wafer-map defect pattern recognition, but this paper targets mixed-type multi-label patterns rather than the WM-811K single-label setting. |
| [[2020 - A Light-Weight Neural Network for Wafer Map Classification Based on Data Augmentation]] | Shares task | Both use neural networks for wafer-map defect classification; Tsai and Lee focus on lightweight/small-data classification, while this paper focuses on mixed-type decomposition. |

## Questions

- What license applies to MixedWM38 and the released code?
- How much of each mixed-type category is simulated versus collected from real wafer manufacturing?
- How does DC-Net perform on external wafer-map datasets without the MixedWM38 simulation process?
