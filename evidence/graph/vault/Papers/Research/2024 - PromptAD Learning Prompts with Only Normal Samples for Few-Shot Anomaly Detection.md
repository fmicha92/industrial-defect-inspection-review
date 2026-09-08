---
title: "PromptAD: Learning Prompts with Only Normal Samples for Few-Shot Anomaly Detection"
aliases:
  - "PromptAD"
paper_key: "doi:10.1109/cvpr52733.2024.01594"
paper_type: research
year: 2024
venue: "CVPR 2024"
authors:
  - "Xiaofan Li"
  - "Zhizhong Zhang"
  - "Xin Tan"
  - "Chengwei Chen"
  - "Yanyun Qu"
  - "Yuan Xie"
  - "Lizhuang Ma"
status: processed
processed_at: 2026-05-22
topics:
  - "few-shot anomaly detection"
  - "prompt learning"
  - "vision-language models"
tasks:
  - "[[Industrial anomaly detection]]"
  - "[[Defect segmentation]]"
domains:
  - "[[Multi-industry anomaly detection]]"
datasets:
  - "[[MVTec AD]]"
  - "[[VisA]]"
methods:
  - "[[PromptAD]]"
  - "[[Few-shot anomaly detection]]"
  - "[[Vision-language prompt learning]]"
model_family:
  - "vision-language model"
  - "CLIP-style model"
metrics:
  - "[[AU-ROC]]"
  - "[[Average precision]]"
primary_metric: "[[AU-ROC]]"
baselines:
  - "WinCLIP"
  - "many-class prompt learning baseline"
code: "reported available: https://github.com/FuNz0/PromptAD.git"
data: "[[MVTec AD]], [[VisA]]"
doi: "10.1109/CVPR52733.2024.01594"
arxiv: "not reported"
url: "https://doi.org/10.1109/CVPR52733.2024.01594"
pdf: "paper-inbox/10_processed/Research/2024 - Li - PromptAD Learning Prompts with Only Normal Samples for Few-Shot Anomaly Detection.pdf"
source_file: "paper-inbox/10_processed/Research/2024 - Li - PromptAD Learning Prompts with Only Normal Samples for Few-Shot Anomaly Detection.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2024 - Li - PromptAD Learning Prompts with Only Normal Samples for Few-Shot Anomaly Detection.md"
extracted_text: "paper-inbox/90_processing/text/2024 - Li - PromptAD Learning Prompts with Only Normal Samples for Few-Shot Anomaly Detection.txt"
artifact_status: "code reported available"
tags:
  - "paper"
  - "few-shot-anomaly-detection"
  - "prompt-learning"
---

# PromptAD: Learning Prompts with Only Normal Samples for Few-Shot Anomaly Detection

## Summary

- PromptAD adapts prompt learning to one-class few-shot anomaly detection using only normal images.
- It uses semantic concatenation to create anomaly prompts from normal prompts and explicit anomaly margin to separate normal and anomaly prompt features.
- The paper reports first-place image-level or pixel-level results in 11 of 12 few-shot settings on MVTec and VisA.

## Contribution

- Claimed: conventional many-class prompt learning fails in one-class anomaly detection, motivating one-class prompt learning.
- Claimed: semantic concatenation creates negative prompt supervision without anomaly images.
- Shown: PromptAD reaches 91.3% image-level and 92.5% pixel-level anomaly detection in the example comparison while using far fewer prompts than WinCLIP.

## Method

- Learnable normal prompts are concatenated with manual or learnable anomaly suffixes to form negative anomaly prompts.
- Explicit anomaly margin controls the distance between normal image features, normal prompt features, and anomaly prompt features.
- The method is built for few-shot industrial anomaly detection with normal samples only.

## Evidence

- The abstract reports first place in 11/12 few-shot settings on MVTec and VisA.
- The introduction reports 91.3% image-level and 92.5% pixel-level anomaly detection in a one-shot comparison figure.
- Code is reported at the project GitHub URL.

## Limitations

- The method relies on a pretrained vision-language model and prompt semantics; behavior on non-object-centric industrial data is not reported in the extracted source.
- Only normal samples are used for prompt learning, so anomaly prompt quality is synthetic/text-derived.

## Connections

### Graph Hubs

- Tasks: [[Industrial anomaly detection]], [[Defect segmentation]]
- Methods: [[PromptAD]], [[Few-shot anomaly detection]], [[Vision-language prompt learning]]
- Datasets: [[MVTec AD]], [[VisA]]
- Domains: [[Multi-industry anomaly detection]]
- Metrics: [[AU-ROC]], [[Average precision]]

### Related Papers and Concepts

| Target | Relationship | Rationale |
|---|---|---|
| [[MVTec AD]] | Shares dataset | PromptAD evaluates few-shot anomaly detection on MVTec. |
| [[VisA]] | Shares dataset | PromptAD evaluates few-shot anomaly detection on VisA. |
| [[2025 - SeaS Few-Shot Industrial Anomaly Image Generation with Separation and Sharing Fine-Tuning]] | Shares task | Both address few-shot industrial anomaly detection, but PromptAD uses prompt learning rather than image generation. |

## Questions

- Which prompt suffixes drive the largest performance gains?
- How sensitive is explicit anomaly margin to the hyperparameter across categories?
