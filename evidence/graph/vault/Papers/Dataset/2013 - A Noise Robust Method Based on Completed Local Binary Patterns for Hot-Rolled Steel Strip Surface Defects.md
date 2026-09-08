---
title: "A noise robust method based on completed local binary patterns for hot-rolled steel strip surface defects"
aliases:
  - "A Noise Robust Method Based on Completed Local Binary Patterns for Hot-Rolled Steel Strip Surface Defects"
paper_key: "doi:10.1016/j.apsusc.2013.09.002"
paper_type: "dataset"
year: 2013
venue: "Applied Surface Science"
authors:
  - "Kechen Song"
  - "Yunhui Yan"
doi: "10.1016/j.apsusc.2013.09.002"
url: "https://doi.org/10.1016/j.apsusc.2013.09.002"
pdf: "paper-inbox/10_processed/Dataset/2013 - Song - A Noise Robust Method Based on Completed Local Binary Patterns for Hot-Rolled Steel Strip Surface Defects.pdf"
source_file: "paper-inbox/10_processed/Dataset/2013 - Song - A Noise Robust Method Based on Completed Local Binary Patterns for Hot-Rolled Steel Strip Surface Defects.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2013 - Song - A Noise Robust Method Based on Completed Local Binary Patterns for Hot-Rolled Steel Strip Surface Defects.md"
extracted_text: "paper-inbox/90_processing/text/2013 - Song - A Noise Robust Method Based on Completed Local Binary Patterns for Hot-Rolled Steel Strip Surface Defects.txt"
status: "processed"
processed_at: "2026-06-05"
topics:
  - "steel strip surface defects"
  - "local binary patterns"
  - "noise-robust defect recognition"
tasks:
  - "[[Defect classification]]"
  - "[[Metallic surface defect detection]]"
domains:
  - "[[Metal inspection]]"
datasets:
  - "[[NEU-CLS]]"
methods:
  - "[[Adjacent evaluation completed local binary patterns]]"
  - "[[Feature extraction]]"
metrics:
  - "[[Accuracy]]"
primary_metric: "[[Accuracy]]"
model_family:
  - "local texture descriptors"
architectures:
  - "not applicable"
baselines:
  - "LBP"
  - "LTP"
  - "CLBP"
  - "nearest neighbor classifier"
  - "support vector machine"
data: "The paper constructs the Northeastern University (NEU) surface defect database."
code: "not reported"
artifact_status: "dataset constructed; code not reported; license not reported"
licenses: "not reported"
related_datasets:
  - "[[NEU-CLS]]"
related_domains:
  - "[[Metal inspection]]"
related_tasks:
  - "[[Defect classification]]"
  - "[[Metallic surface defect detection]]"
related_methods:
  - "[[Adjacent evaluation completed local binary patterns]]"
related_concepts:
  - "[[Feature extraction]]"
related_papers:
  - "[[2020 - An End-to-End Steel Surface Defect Detection Approach via Fusing Multiple Hierarchical Features]]"
---
# A noise robust method based on completed local binary patterns for hot-rolled steel strip surface defects

## Summary

Song and Yan introduce a hot-rolled steel strip defect recognition pipeline centered on [[Adjacent evaluation completed local binary patterns]], a noise-robust extension of completed local binary patterns. The paper also constructs the Northeastern University (NEU) surface defect database, a six-class grayscale surface-defect image dataset now commonly referred to as [[NEU-CLS]].

## Paper Type

Dataset-introducing research paper. The main technical contribution is a feature descriptor for steel surface defect recognition, and the experimental section introduces the NEU surface defect database used for classification evaluation.

## Problem

Automated surface inspection needs reliable defect classification under intra-class appearance variation, inter-class visual similarity, illumination changes, material grayscale differences, and sensor noise. The paper frames hot-rolled steel strip inspection as a visual-recognition problem after an acquisition and rapid-detection stage isolate defect regions.

## Contribution

- Introduces adjacent evaluation completed local binary patterns (AECLBPs), replacing the single neighbor-pixel threshold in CLBP with an adjacent evaluation window average to reduce noise sensitivity.
- Constructs the Northeastern University (NEU) surface defect database with 1,800 grayscale images across six steel strip surface defect categories.
- Evaluates AECLBP against LBP, LTP, and CLBP under clean and Gaussian-noise conditions with nearest-neighbor and SVM classifiers.

## Method

The inspection system described in the paper has image acquisition, rapid detection, feature extraction, and defect classification stages. Four area-scan CCD cameras and LED lighting capture grayscale steel-strip images; the original 1024 x 1024 images are downsampled to 200 x 200. A gray-projection algorithm removes defect-free images, and an area-search step locates defect regions.

AECLBP modifies completed local binary patterns by replacing each neighbor value with the mean value of a small adjacent evaluation window around that neighbor. The descriptor keeps sign, magnitude, and center components, producing AECLBP-Sign, AECLBP-Magnitude, AECLBP-Center, and combined AECLBP S/M/C histograms. Multi-scale descriptors concatenate histograms across different `(P, R)` sampling settings.

The classifiers are a nearest-neighbor classifier using chi-square histogram distance and an RBF-kernel support vector machine implemented with LIBSVM. The paper reports cross-validation for SVM parameter selection.

## Dataset

The source-supported dataset name is the Northeastern University (NEU) surface defect database. The dataset contains 1,800 grayscale images at 200 x 200 resolution, with 300 samples for each defect class:

| Class | Abbreviation | Samples |
|---|---:|---:|
| Rolled-in scale | RS | 300 |
| Patches | Pa | 300 |
| Crazing | Cr | 300 |
| Pitted surface | PS | 300 |
| Inclusion | In | 300 |
| Scratches | Sc | 300 |

The paper reports that each sample was normalized to average intensity 128 and standard deviation 20 for the recognition experiments. For the main evaluation, 150 samples per class are randomly selected for training and the remaining 150 per class are used for testing; this random split is repeated 100 times.

## Evidence

The main clean-dataset experiment reports average recognition accuracy and standard deviation over 100 random partitions. AECLBP is the strongest descriptor in both classifier settings:

| Descriptor | NNC accuracy | SVM accuracy |
|---|---:|---:|
| LBP | 95.07 +/- 0.71 | 97.93 +/- 0.66 |
| LTP | 95.93 +/- 0.39 | 98.22 +/- 0.52 |
| CLBP | 96.91 +/- 0.24 | 98.28 +/- 0.51 |
| AECLBP | 97.93 +/- 0.21 | 98.93 +/- 0.63 |

The confusion-matrix experiment with NNC reports total recognition accuracy of 97.89%. Rolled-in scale is classified with 100% accuracy, while pitted surface and inclusion have more confusion than the other classes.

Under added Gaussian noise, AECLBP remains the best tested descriptor across SNR levels. With SVM, AECLBP reports 98.87 +/- 0.37 at 50 dB, 98.53 +/- 0.39 at 40 dB, 88.29 +/- 1.70 at 30 dB, and 37.09 +/- 2.15 at 20 dB.

## Performance Metrics

- [[Accuracy]]: higher is better; primary metric for defect recognition.
- Main result: AECLBP with SVM reports 98.93 +/- 0.63 accuracy on the NEU surface defect database.
- Robustness result: AECLBP with SVM reports the highest accuracy among tested descriptors at each reported Gaussian-noise SNR level.

## ML/DL Extraction

- Task formulation: six-class steel strip surface defect classification.
- Inputs: 200 x 200 grayscale defect-region images.
- Outputs: one of six defect classes: RS, Pa, Cr, PS, In, or Sc.
- Model family: hand-crafted local texture descriptor plus classical classifier.
- Architecture: not applicable; no neural network architecture is proposed.
- Objective/loss: not reported for SVM optimization beyond RBF-kernel SVM training.
- Optimizer: not reported.
- Training recipe: 150 images per class for training and 150 per class for testing, repeated across 100 random partitions.
- Preprocessing: intensity normalization to mean 128 and standard deviation 20.
- Augmentation: Gaussian-noise injection is used for robustness testing, not for training augmentation.
- Evaluation protocol: clean-data classification accuracy and Gaussian-noise robustness at 50, 40, 30, and 20 dB SNR.
- Compute/hardware: image acquisition uses LED lighting and four area-scan CCD cameras; training compute is not reported.
- Artifacts: dataset constructed; code, license, and download location are not reported in the paper text.

## Limitations

- The number of defect categories is relatively small.
- The paper evaluates recognition on the constructed NEU database but does not report cross-dataset generalization.
- Dataset licensing, maintenance, and public release details are not reported in the paper text.
- The method is evaluated with classical classifiers and hand-crafted descriptors; the paper identifies advanced classifiers as future work.

## Connections

### Graph Hubs

- Tasks: [[Defect classification]], [[Metallic surface defect detection]]
- Methods: [[Adjacent evaluation completed local binary patterns]], [[Feature extraction]]
- Datasets: [[NEU-CLS]]
- Domains: [[Metal inspection]]
- Metrics: [[Accuracy]]

### Shares dataset

- [[NEU-CLS]]: introduced in this paper as the Northeastern University (NEU) surface defect database.

### Shares task

- [[Defect classification]]: evaluates six-class hot-rolled steel strip surface defect recognition.
- [[Metallic surface defect detection]]: the acquisition and rapid-detection stages provide defect regions for metal surface recognition.

### Shares method

- [[Adjacent evaluation completed local binary patterns]]: proposed descriptor for noise-robust feature extraction.
- [[Feature extraction]]: the paper is a classical texture-feature extraction study for industrial visual inspection.

### Shares metric

- [[Accuracy]]: primary reported metric for clean and noisy defect recognition experiments.

### Application/domain

- [[Metal inspection]]: focuses on hot-rolled steel strip surface inspection.

### Follow-up reading

- [[2020 - An End-to-End Steel Surface Defect Detection Approach via Fusing Multiple Hierarchical Features]]: later work treats NEU-CLS as the original classification dataset and extends it into [[NEU-DET]] with detection annotations.

## Questions

- Where is the canonical maintained dataset release and what license applies to it?
- Are the exact random splits used in the paper recoverable, or do later NEU-CLS experiments define their own split protocols?
