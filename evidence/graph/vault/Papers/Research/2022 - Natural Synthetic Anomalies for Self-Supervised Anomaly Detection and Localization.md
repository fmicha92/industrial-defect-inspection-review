---
title: "Natural Synthetic Anomalies for Self-Supervised Anomaly Detection and Localization"
aliases:
  - "Natural Synthetic Anomalies for Self-Supervised Anomaly Detection and Localization"
  - "NSA"
paper_key: "arxiv:2109.15222"
paper_type: research
year: 2022
venue: "arXiv"
authors:
  - "Hannah M. Schlueter"
  - "Jeremy Tan"
  - "Benjamin Hou"
  - "Bernhard Kainz"
status: processed
processed_at: 2026-05-23
topics:
  - "self-supervised anomaly detection"
  - "synthetic anomalies"
  - "anomaly localization"
tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
domains:
  - "[[Multi-industry anomaly detection]]"
  - "[[Medical imaging]]"
datasets:
  - "[[MVTec AD]]"
  - "[[rCXR]]"
methods:
  - "[[Natural Synthetic Anomalies]]"
  - "[[Self-supervised learning]]"
  - "[[Data augmentation]]"
model_family:
  - "encoder-decoder"
architectures:
  - "ResNet-18 encoder"
metrics:
  - "[[AU-ROC]]"
primary_metric: "[[AU-ROC]]"
baselines:
  - "FPI"
  - "PII"
  - "CutPaste"
  - "DRAEM"
code: "reported available: https://github.com/hmsch/natural-synthetic-anomalies"
data: "uses MVTec AD and a curated public NIH chest X-ray subset"
doi: "not reported"
arxiv: "2109.15222"
url: "https://arxiv.org/abs/2109.15222"
pdf: "paper-inbox/10_processed/Research/2022 - Schlueter - Natural Synthetic Anomalies for Self-Supervised Anomaly Detection and Localization.pdf"
source_file: "paper-inbox/10_processed/Research/2022 - Schlueter - Natural Synthetic Anomalies for Self-Supervised Anomaly Detection and Localization.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2022 - Schlueter - Natural Synthetic Anomalies for Self-Supervised Anomaly Detection and Localization.md"
extracted_text: "paper-inbox/90_processing/text/2022 - Schlueter - Natural Synthetic Anomalies for Self-Supervised Anomaly Detection and Localization.txt"
artifact_status: "code reported available"
tags:
  - paper
---

# Natural Synthetic Anomalies for Self-Supervised Anomaly Detection and Localization

## Summary

Natural Synthetic Anomalies (NSA) is a self-supervised anomaly detection and localization task that trains an end-to-end model using only normal training images. It creates synthetic anomalies by seamlessly blending resized patches from separate normal images with Poisson image editing, then trains a model to localize the resulting pixel-level anomaly signal.

The paper evaluates NSA on [[MVTec AD]] and a re-curated chest X-ray subset, [[rCXR]]. On MVTec AD, NSA (logistic) reports 97.2 image-level AUROC and 96.3 pixel-level AUROC, outperforming methods that learn without additional datasets while remaining smaller than DRAEM.

## Paper Type

- Type: research.
- Why: introduces a self-supervised synthetic anomaly task and evaluates detection and localization performance against self-supervised and synthetic-anomaly baselines.

## Problem

- Task: [[Industrial anomaly detection]], [[Defect segmentation]], and binary medical anomaly classification.
- Setting: normal-only training for unknown anomaly detection.
- Inputs: normal images from MVTec AD or rCXR during training.
- Outputs: pixel-level anomaly maps; image-level scores are computed from pixel scores for MVTec AD.
- Motivation: synthetic anomaly training can avoid dependence on real anomalous labels, ImageNet pretraining, or large auxiliary datasets.

## Contribution

- Introduces NSA, which creates more natural synthetic anomalies with Poisson blending and more diverse anomalies by shifting, resizing, and sampling patch shapes from a Gamma distribution.
- Uses object/background constraints so pasted patches overlap relevant object regions rather than floating in plain backgrounds.
- Defines binary, continuous, and logistic pixel labels from the intensity difference caused by blending.
- Shows strong MVTec AD results without ImageNet pretraining or external anomaly texture data.
- Demonstrates transfer of the self-supervised task to medical imaging through rCXR disease detection.

## Method

- Select a random rectangular patch from a source normal image.
- Resize the patch and choose a different destination location in another normal image.
- Seamlessly blend the patch into the destination image with Poisson image editing implemented through OpenCV seamless cloning.
- Optionally add multiple patches to one image.
- Create pixel-wise labels from the difference between the blended sample and the original destination image.
- Train an encoder-decoder to predict the anomaly label map.

## Model And Training

- Architecture: ResNet-18 without classification layers as encoder, two 1x1 bottleneck convolutions, and a simpler ResNet-based decoder.
- Activation/loss: sigmoid with binary cross-entropy for bounded binary and logistic labels; ReLU with mean squared error for unbounded continuous labels.
- Optimizer: Adam.
- Batch size: 64.
- Learning rate: cosine annealing from 1e-3 to 1e-6.
- Epochs: 320 for most MVTec AD classes; 560 for hazelnut, metal nut, and screw; 240 for rCXR.
- Implementation: PyTorch 1.8.1; examples generated in parallel with 8 CPU processes; trained on an Nvidia GeForce GTX 1080 GPU.

## Evidence

### Experimental Setup

- [[MVTec AD]]: normal training data plus normal and anomalous test data for 10 object and 5 texture classes.
- [[rCXR]]: a further curated subset of a public NIH chest X-ray dataset, restricted to posteroanterior adult images and separated by gender.
- Metrics: image-level and pixel-level [[AU-ROC]].
- Baselines: FPI, PII, CutPaste end-to-end, CutPaste 3-way, and DRAEM.

### Main Results

| Dataset / task | Method | Metric | Result | Notes |
|---|---|---|---:|---|
| MVTec AD image-level detection | NSA (logistic) | AUROC | 97.2 +/- 0.3 | best NSA variant; no additional dataset |
| MVTec AD pixel-level localization | NSA (logistic) | AUROC | 96.3 +/- 0.4 | comparable to CutPaste 3-way and below DRAEM overall |
| rCXR male image-level detection | NSA binary / continuous / logistic | AUROC | 94.0 / 93.4 / 94.0 | all outperform FPI, PII, and CutPaste end-to-end |
| rCXR female image-level detection | NSA binary / continuous / logistic | AUROC | 94.3 / 93.0 / 94.0 | all outperform FPI, PII, and CutPaste end-to-end |

### Comparisons

- On MVTec AD image-level detection, NSA (logistic) outperforms CutPaste (3-way) by 2.0 AUROC points and a 5-model CutPaste ensemble reported at 96.1 AUROC.
- DRAEM reports 98.0 image-level AUROC and 97.3 pixel-level AUROC, but uses additional DTD texture data and a much larger two-component model.
- NSA models have around 11 million parameters; DRAEM's two components add up to over 97 million parameters in the paper's comparison.

## Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[AU-ROC]] | image-level detection and pixel-level localization | area under the receiver operating characteristic curve | higher | yes | reported for MVTec AD and rCXR |

## Dataset / Benchmark Details

- MVTec AD contains normal training data and normal/anomalous test data across 10 object and 5 texture classes.
- MVTec AD object images are resized to 256 x 256, lightly rotated for selected classes, center-cropped to 230 x 230, and randomly cropped to 224 x 224 before self-supervised example creation.
- Texture classes use random 256 x 256 crops of 264 x 264 images for training.
- rCXR male split: 1973 normal training images, 299 normal test images, and 139 abnormal test images.
- rCXR female split: 1641 normal training images, 244 normal test images, and 123 abnormal test images.

## Limitations

- The model can fail on very small defects and can produce false positives, false negatives, or overly large localization regions.
- For the transistor class, missing or misplaced components can be detected but the predicted localization may not match broad human annotations.
- Since no real anomalies are seen during training, statistically unlikely normal variation may be flagged as abnormal and subtle real anomalies unlike the synthetic task may be missed.
- The authors state predictions should not be used alone for decision making.
- Future work includes uncertainty quantification and exploiting known anomaly classes for critical applications.

## Reproducibility

- Code: https://github.com/hmsch/natural-synthetic-anomalies.
- Data: MVTec AD and the public NIH chest X-ray source are named; rCXR is a curated subset defined by filtering criteria in the paper.
- Training recipe: architecture, optimizer, learning-rate schedule, epochs, crops, and implementation stack are reported.

## Connections

### Graph Hubs

- Tasks: [[Industrial anomaly detection]], [[Defect segmentation]]
- Methods: [[Natural Synthetic Anomalies]], [[Self-supervised learning]], [[Data augmentation]]
- Datasets: [[MVTec AD]], [[rCXR]]
- Domains: [[Multi-industry anomaly detection]], [[Medical imaging]]
- Metrics: [[AU-ROC]]

### Related Papers and Concepts

| Target | Relationship | Rationale |
|---|---|---|
| [[MVTec AD]] | Benchmark dataset | NSA is evaluated on MVTec AD for image-level detection and pixel-level localization. |
| [[rCXR]] | Evaluation dataset | NSA is evaluated on a curated public chest X-ray subset for binary abnormality detection. |
| [[Self-supervised learning]] | Learning paradigm | NSA creates a proxy localization task from normal data. |
| [[2021 - Self-Supervised Learning for Anomaly Detection With Dynamic Local Augmentation]] | Related task | Both use normal-only self-supervised anomaly localization on MVTec AD. |

## Questions

- How sensitive is NSA to the patch-shape and object-overlap hyperparameters?
- Would uncertainty estimates reduce the risk of using NSA predictions in quality-control triage?
- How well does NSA perform on industrial datasets with anomalies unlike patch-based local texture changes?
