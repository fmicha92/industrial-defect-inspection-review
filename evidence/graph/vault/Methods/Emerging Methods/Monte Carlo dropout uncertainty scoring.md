---
title: "Monte Carlo dropout uncertainty scoring"
aliases:
  - "MC dropout uncertainty scoring"
  - "Monte Carlo Dropout uncertainty"
status: emerging
concept_type: method
candidate_parent: "Methods/Models/Anomaly Detection Models"
source_papers:
  - "[[2021 - Self-Supervised Learning for Anomaly Detection With Dynamic Local Augmentation]]"
evidence_count: 1
tags:
  - emerging-method
---
# Monte Carlo Dropout Uncertainty Scoring

## Definition

Monte Carlo dropout uncertainty scoring estimates pixel-level predictive uncertainty by keeping dropout active at test time and measuring variance across multiple forward passes. In [[2021 - Self-Supervised Learning for Anomaly Detection With Dynamic Local Augmentation]], uncertainty maps are computed for ResNet feature stages and compared against average training-image uncertainty maps.

## Why It Matters

The method gives a normal-only anomaly detector an additional signal for abnormal regions whose feature representations are uncertain rather than merely different from the normal training average.

## Used In These Papers

- [[2021 - Self-Supervised Learning for Anomaly Detection With Dynamic Local Augmentation]] combines MC-dropout uncertainty with regression-error scoring for pixel-wise MVTec AD anomaly localization.

## Related Concepts

- [[Dynamic Local Augmentation]]
- [[Regression-error anomaly scoring]]
- [[Industrial anomaly detection]]
- [[AU-ROC]]
