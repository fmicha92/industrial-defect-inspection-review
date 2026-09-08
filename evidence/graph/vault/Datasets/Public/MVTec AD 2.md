---
title: "MVTec AD 2"
aliases:
  - "MVTec AD 2 Dataset"
related_domain: "[[Multi-industry anomaly detection]]"
url: "https://www.mvtec.com/research-teaching/datasets/mvtec-ad-2"
data_sources: "MVTec"
introduced_by: "[[2025 - The MVTec AD 2 Dataset Advanced Scenarios for Unsupervised Anomaly Detection]]"
related_papers:
  - "[[2025 - The MVTec AD 2 Dataset Advanced Scenarios for Unsupervised Anomaly Detection]]"
availability: "public"
access: "image data downloadable from MVTec; private-test ground truth available only through MVTec benchmark server"
licenses:
  - "CC BY-NC-SA 4.0"
---
# MVTec AD 2

## Definition

MVTec AD 2 is a public industrial anomaly detection benchmark with 8,004 high-resolution images across eight advanced 2D inspection scenarios. It targets cases that are weakly covered by earlier datasets, including transparent and overlapping objects, dark-field and back-light illumination, high normal-data variability, extremely small defects, defects at image borders, and lighting-condition distribution shifts.

## Why It Matters

It extends the MVTec anomaly-detection benchmark family toward harder industrial scenarios where current methods remain well below saturated performance. The dataset also supports standardized evaluation through a public benchmark server with non-public private-test ground truth.

## Dataset Details

- Total images: 8,004 high-resolution images.
- Scenarios: Can, Fabric, Fruit Jelly, Rice, Sheet Metal, Vial, Wall Plugs, and Walnuts.
- Data type: 2D visual inspection images; Sheet Metal, Vial, and Wall Plugs include single-channel gray-value images.
- Industrial challenges: overlapping bulk goods, transparent objects, reflective metal, textured surfaces with high normal variability, low-contrast or tiny defects, defects at borders, and lighting shifts.
- Splits: training and validation contain only anomaly-free images.
- Test design: `TESTpub` has public images and segmentation ground truth for local testing; `TESTpriv` and `TESTpriv,mix` expose image data while pixel-precise ground truth is held by the evaluation server.
- Lighting: every scenario has at least four lighting conditions; `TESTpriv,mix` includes seen and unseen lighting conditions for distribution-shift evaluation.
- Evaluation: primary localization focus is [[AU-PRO]], with the paper emphasizing lower false-positive integration bounds such as AU-PRO0.05; the benchmark server also supports thresholded anomaly maps.
- Availability: image data are public through MVTec; private-test ground truth is evaluated through https://benchmark.mvtec.com/.
- License: CC BY-NC-SA 4.0; commercial use is not allowed under the MVTec terms.

## Used In These Papers

- [[2025 - The MVTec AD 2 Dataset Advanced Scenarios for Unsupervised Anomaly Detection]] introduces MVTec AD 2 and evaluates unsupervised anomaly detection scenarios.

## Source Anchors

- Hosting source: https://www.mvtec.com/research-teaching/datasets/mvtec-ad-2.
- Evaluation server: https://benchmark.mvtec.com/.
- Introducing paper: [[2025 - The MVTec AD 2 Dataset Advanced Scenarios for Unsupervised Anomaly Detection]].
- Access terms: CC BY-NC-SA 4.0, noncommercial; private-test labels are server-held.

## Related Concepts

- [[Multi-industry anomaly detection]]
- [[MVTec AD]]
- [[Unsupervised anomaly detection]]
- [[AU-ROC]]
- [[AU-PRO]]
