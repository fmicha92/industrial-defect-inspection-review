---
title: "Lusitano benchmark"
aliases:
  - "Lusitano anomaly detection benchmark"
  - "Lusitano fabric defect benchmark"
tags:
  - benchmark
  - dataset
  - textile-inspection
---

# Lusitano Benchmark

## Definition

Lusitano benchmark is the one-class fabric anomaly detection evaluation introduced with [[Lusitano]]. It trains anomaly detection methods on normal fabric images and evaluates them on a held-out test set containing normal and defective textile images.

## Why It Matters

The benchmark targets industrial conditions where real defects are rare and diverse. It evaluates whether one-class methods trained only on normal fabrics can detect subtle factory defects.

## Used In These Papers

- [[2024 - A Novel Dataset for Fabric Defect Detection Bridging Gaps in Anomaly Detection]] introduces the benchmark and reports [[RD4AD]] outperforming [[DBFAD]].

## Benchmark Protocol

- Dataset: [[Lusitano]].
- Task: [[Textile defect detection]], [[Industrial anomaly detection]].
- Training data: normal images only.
- Training subsets: 1k, 2k, 4k, 8k, 16k, and 32k normal images.
- Test data: 1038 normal and 1646 defect images.
- Preprocessing: center crop to 2000 x 1000 pixels; model input image size 256 x 256.
- Methods: [[DBFAD]], [[RD4AD]].
- Metrics: [[AU-ROC]], [[mAP]].
- Hardware: NVIDIA RTX A6000.

## Reported Results

| Method | Training size | AU-ROC / AUC | mAP | Notes |
|---|---:|---:|---:|---|
| [[DBFAD]] | 1k | 0.7573 | 0.8162 | Lowest DBFAD training size. |
| [[DBFAD]] | 32k | 0.7814 | 0.8429 | Best DBFAD result in Table 3. |
| [[RD4AD]] | 1k | 0.8231 | 0.8773 | RD4AD starts above DBFAD at the same training size. |
| [[RD4AD]] | 32k | 0.8860 | 0.9390 | Best reported result in Table 3. |

## Related Concepts

- [[Lusitano]]
- [[Textile defect detection]]
- [[Industrial anomaly detection]]
- [[Unsupervised anomaly detection]]
- [[AU-ROC]]
- [[mAP]]
