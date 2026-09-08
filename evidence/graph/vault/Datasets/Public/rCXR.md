---
title: "rCXR"
aliases:
  - "re-curated chest X-ray"
related_domain: "[[Medical imaging]]"
url: "not reported"
data_sources: "public NIH chest X-ray dataset"
introduced_by: "[[2022 - Natural Synthetic Anomalies for Self-Supervised Anomaly Detection and Localization]]"
---
# rCXR

## Definition

rCXR is the re-curated chest X-ray evaluation subset used by [[2022 - Natural Synthetic Anomalies for Self-Supervised Anomaly Detection and Localization]]. It filters a public NIH chest X-ray dataset to posteroanterior adult images and separates male and female patient subsets for binary normal/pathological detection.

## Dataset Details

- Source dataset: public NIH chest X-ray dataset.
- Male split: 1973 normal training images, 299 normal test images, and 139 abnormal test images.
- Female split: 1641 normal training images, 244 normal test images, and 123 abnormal test images.
- Input processing in the paper: grayscale 1024 x 1024 images resized to 256 x 256, lightly rotated, center-cropped to 230 x 230, and cropped to 224 x 224 for training/testing.
- Annotation detail: image-level normal/pathological labels are used; rough bounding boxes are available for less than 10% of the test set, so pixel-level metrics are not reported.
- Availability: public source dataset reported; exact host URL and license are not reported in the paper source.

## Used In These Papers

- [[2022 - Natural Synthetic Anomalies for Self-Supervised Anomaly Detection and Localization]] evaluates Natural Synthetic Anomalies on rCXR for binary disease detection.

## Source Anchors

- Introducing paper: [[2022 - Natural Synthetic Anomalies for Self-Supervised Anomaly Detection and Localization]].
- Hosting source: not reported.

## Related Concepts

- [[Medical imaging]]
- [[AU-ROC]]
- [[Self-supervised learning]]
