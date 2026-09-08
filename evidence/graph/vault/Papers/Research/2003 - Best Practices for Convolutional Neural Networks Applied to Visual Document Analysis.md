---
title: "Best Practices for Convolutional Neural Networks Applied to Visual Document Analysis"
aliases:
  - "Best Practices for CNNs Applied to Visual Document Analysis"
paper_key: "sha256:810398ec32975a2bc86f9e06a1e639967c540a49de1e4774f63c1e862a7fe0bb"
paper_type: research
year: 2003
venue: "ICDAR 2003"
authors:
  - "Patrice Y. Simard"
  - "Dave Steinkraus"
  - "John C. Platt"
status: processed
processed_at: 2026-06-02
topics:
  - convolutional neural networks
  - elastic distortions
  - handwritten digit recognition
tasks:
  - "[[Handwritten digit recognition]]"
  - "[[Document recognition]]"
datasets:
  - "[[MNIST]]"
domains:
  - "[[Document analysis]]"
methods:
  - "[[Deep convolutional neural network]]"
  - "[[Elastic distortion augmentation]]"
metrics:
  - "[[Error rate]]"
related_methods:
  - "[[Deep convolutional neural network]]"
  - "[[Elastic distortion augmentation]]"
doi: "not reported"
arxiv: "not reported"
url: "not reported"
pdf: "paper-inbox/10_processed/Research/2003 - Simard - Best Practices for Convolutional Neural Networks Applied to Visual Document Analysis.pdf"
source_file: "paper-inbox/10_processed/Research/2003 - Simard - Best Practices for Convolutional Neural Networks Applied to Visual Document Analysis.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2003 - Simard - Best Practices for Convolutional Neural Networks Applied to Visual Document Analysis.md"
extracted_text: "paper-inbox/90_processing/text/2003 - Simard - Best Practices for Convolutional Neural Networks Applied to Visual Document Analysis.txt"
artifact_status: "processed"
tags:
  - paper
  - document-recognition
---

# Best Practices for Convolutional Neural Networks Applied to Visual Document Analysis

## Summary

Simard, Steinkraus, and Platt argue that visual document CNN performance depends strongly on training-set expansion through realistic distortions. On [[MNIST]], a simple convolutional network with [[Elastic distortion augmentation]] reaches 0.4% test error, reported as the best known result at the time.

## Paper Type

Research paper. It evaluates training practices for convolutional networks in visual document analysis.

## Problem

MNIST has too few examples for a learner to infer all relevant handwriting deformations. The paper studies which augmentations and convolutional design choices improve digit recognition.

## Contribution

- Shows that elastic distortions are more effective than affine distortions for MNIST handwritten digit recognition.
- Shows that a simple CNN benefits strongly from elastic distortion augmentation.
- Reports 0.4% MNIST test error for a simple CNN trained with cross-entropy and elastic distortions.

## Method

Elastic distortion augmentation samples random displacement fields, smooths them with a Gaussian kernel, normalizes them, scales them by alpha 8, and warps images through bilinear interpolation. The CNN uses convolution/subsampling stages followed by fully connected layers. The paper deliberately avoids many extra refinements such as momentum, weight decay, padding, and architecture-specific learning rates.

## Evidence

The paper trains on the first 50,000 MNIST training images and uses the remaining 10,000 for validation. Reported MNIST test errors include 1.6% for a two-layer MLP without distortion, 0.7% for a two-layer MLP with cross-entropy and elastic distortions, 0.6% for a simple CNN with affine distortions, and 0.4% for a simple CNN with elastic distortions.

## ML/DL Extraction

- Dataset: [[MNIST]].
- Task: [[Handwritten digit recognition]].
- Architecture: two convolution/subsampling stages and two fully connected layers.
- Training: learning rate starts at 0.005 and is multiplied by 0.3 every 100 epochs; small random weight initialization with standard deviation 0.05.
- Losses evaluated: cross-entropy and mean squared error.
- Metric: [[Error rate]] on MNIST test set.

## Limitations

- The evidence is primarily MNIST-focused.
- The paper argues for broader document-analysis relevance, but it does not evaluate a broad suite of modern document-recognition datasets.
- The conclusions are tied to the architectures and optimization setup tested in the paper.

## Connections

### Graph Hubs

- Tasks: [[Handwritten digit recognition]], [[Document recognition]]
- Datasets: [[MNIST]]
- Domains: [[Document analysis]]
- Methods: [[Deep convolutional neural network]], [[Elastic distortion augmentation]]
- Metrics: [[Error rate]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[1998 - Gradient-Based Learning Applied to Document Recognition]] | Builds on | Both study CNNs for document recognition; this paper isolates training augmentation practices after LeNet-style CNNs had already shown strong MNIST performance. |

## Questions

- Which distortion parameters transfer from MNIST to other handwritten or printed document-recognition tasks?
