---
title: "Gradient-Based Learning Applied to Document Recognition"
aliases:
  - "LeNet-5 paper"
paper_key: "doi:10.1109/5.726791"
paper_type: research
year: 1998
venue: "Proceedings of the IEEE"
authors:
  - "Yann LeCun"
  - "Leon Bottou"
  - "Yoshua Bengio"
  - "Patrick Haffner"
status: processed
processed_at: 2026-06-02
topics:
  - convolutional neural networks
  - LeNet-5
  - graph transformer networks
  - document recognition
tasks:
  - "[[Handwritten digit recognition]]"
  - "[[Document recognition]]"
  - "[[Optical character recognition]]"
datasets:
  - "[[MNIST]]"
domains:
  - "[[Document analysis]]"
methods:
  - "[[LeNet-5]]"
  - "[[Deep convolutional neural network]]"
  - "[[Graph transformer network]]"
metrics:
  - "[[Error rate]]"
related_methods:
  - "[[LeNet-5]]"
  - "[[Graph transformer network]]"
doi: "10.1109/5.726791"
arxiv: "not reported"
url: "http://www.research.att.com/~yann/ocr/mnist"
pdf: "paper-inbox/10_processed/Research/1998 - LeCun - Gradient-Based Learning Applied to Document Recognition.pdf"
source_file: "paper-inbox/10_processed/Research/1998 - LeCun - Gradient-Based Learning Applied to Document Recognition.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/1998 - LeCun - Gradient-Based Learning Applied to Document Recognition.md"
extracted_text: "paper-inbox/90_processing/text/1998 - LeCun - Gradient-Based Learning Applied to Document Recognition.txt"
artifact_status: "processed"
tags:
  - paper
  - document-recognition
  - convolutional-neural-networks
---

# Gradient-Based Learning Applied to Document Recognition

## Summary

LeCun et al. present gradient-based document-recognition systems built around convolutional neural networks and trainable graph-transformer architectures. The paper describes [[LeNet-5]] for handwritten digit recognition on [[MNIST]] and graph transformer networks for globally trained document-recognition pipelines, including check-reading systems.

## Paper Type

Research paper. It combines model architecture, benchmark evidence, and systems-level document-recognition design.

## Problem

Document recognition requires local visual invariance, sequence or field structure, and globally consistent decisions. Hand-engineered systems and independently trained modules can fail to optimize the full recognition objective.

## Contribution

- Presents LeNet-5, a convolutional neural network with local receptive fields, shared weights, subsampling, and learned document-image features.
- Shows strong MNIST handwritten-digit performance against classical machine-learning baselines.
- Introduces graph transformer networks as a way to train multimodule recognition systems globally over graph-structured outputs.
- Reports deployed check-reading performance in NCR systems.

## Method

LeNet-5 takes 32x32 centered character images and processes them through convolution, subsampling, convolution, subsampling, fully connected layers, and an RBF output layer. The paper also describes graph transformer networks that transform directed graphs with numerical arc values, allowing gradient-based training through recognition pipelines that include segmentation, character recognition, and linguistic constraints.

## Evidence

MNIST is described as a 60,000-image training set and 10,000-image test set. LeNet-5 reaches 0.95% test error without deformations after about 10 passes and 0.8% test error when trained with 540,000 distorted patterns plus the 60,000 originals. The paper reports LeNet-style CNNs outperforming nearest-neighbor, PCA, RBF, linear classifier, and several SVM configurations in the reported table.

For check reading, a business-check amount reader reports 82% correctly recognized, 1% errors, and 17% rejects on 646 machine-printed business checks; the previous system reports 68% correct, 1% errors, and 31% rejects. The paper states that the system was fielded in NCR check-reading systems and used on millions of checks.

## ML/DL Extraction

- Architecture: [[LeNet-5]] with about 60,000 trainable free parameters and 345,308 connections due to weight sharing.
- Input: normalized handwritten characters centered in 32x32 images.
- Core inductive biases: local receptive fields, shared weights, and subsampling.
- Structured-recognition method: [[Graph transformer network]].
- Dataset: [[MNIST]].
- Metric: [[Error rate]].

## Limitations

- The strongest benchmark evidence is document-specific and centered on handwritten digit recognition.
- Some deployed systems combine trainable modules with task-specific graph structure and constraints.
- The paper predates modern large-scale document benchmarks and architectures.

## Connections

### Graph Hubs

- Tasks: [[Handwritten digit recognition]], [[Document recognition]], [[Optical character recognition]]
- Datasets: [[MNIST]]
- Domains: [[Document analysis]]
- Methods: [[LeNet-5]], [[Deep convolutional neural network]], [[Graph transformer network]]
- Metrics: [[Error rate]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2003 - Best Practices for Convolutional Neural Networks Applied to Visual Document Analysis]] | Follow-up reading | Simard et al. revisit CNN training practices for visual document analysis and improve MNIST error using elastic distortions. |

## Questions

- How should graph-transformer-style global training be compared to modern differentiable structured prediction pipelines?
