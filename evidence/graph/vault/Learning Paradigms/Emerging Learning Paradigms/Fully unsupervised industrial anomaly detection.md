---
title: "Fully unsupervised industrial anomaly detection"
aliases:
  - "FUIAD"
status: emerging
concept_type: learning_paradigm
candidate_parent: "Learning Paradigms/Unsupervised Learning"
source_papers:
  - "[[2024 - Real-IAD A Real-World Multi-View Dataset for Benchmarking Versatile Industrial Anomaly Detection]]"
evidence_count: 1
---
# Fully unsupervised industrial anomaly detection

## Definition

Fully unsupervised industrial anomaly detection is a noisy-training industrial anomaly detection setting where the training stream may include anomalous samples rather than guaranteed normal-only data. In the Real-IAD paper, the setting models production environments with high yield rates where abnormal products can still enter the training pool.

## Why It Matters

Normal-only industrial anomaly detection assumes clean training data. Real-IAD tests whether methods remain reliable when the anomalous training ratio increases to 0.1, 0.2, or 0.4.

## Used In These Papers

- [[2024 - Real-IAD A Real-World Multi-View Dataset for Benchmarking Versatile Industrial Anomaly Detection]] defines the FUIAD setting and reports that most evaluated methods degrade as anomalous training samples increase, while SoftPatch and PatchCore are relatively more robust.

## Related Concepts

- [[Unsupervised learning]]
- [[Unsupervised anomaly detection]]
- [[Industrial anomaly detection]]
- [[Real-IAD]]
