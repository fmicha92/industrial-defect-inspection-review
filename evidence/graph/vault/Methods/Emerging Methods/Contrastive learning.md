---
title: "Contrastive learning"
aliases:
  - "Contrastive representation learning"
status: emerging
concept_type: method
candidate_parent: "Methods/Emerging Methods"
source_papers:
  - "[[2025 - ToCoAD Two-Stage Contrastive Learning for Industrial Anomaly Detection]]"
evidence_count: 1
tags:
  - method
---

# Contrastive learning

## Definition

Contrastive learning trains representations by comparing related and unrelated samples so that useful positives become closer in feature space and negatives become farther apart.

## Why It Matters

In industrial anomaly detection, contrastive learning can adapt a pretrained feature extractor to target-domain normal and synthetic-anomaly features without requiring real defective training samples.

## Used In These Papers

- [[2025 - ToCoAD Two-Stage Contrastive Learning for Industrial Anomaly Detection]] uses negative-guided contrastive learning to fine-tune an anomaly feature extractor after training a discriminative network on synthetic anomalies.

## Related Concepts

- [[Self-supervised learning]]
- [[Industrial anomaly detection]]
- [[Defect synthesis]]

