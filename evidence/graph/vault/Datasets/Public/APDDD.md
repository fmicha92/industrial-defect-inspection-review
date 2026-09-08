---
title: "APDDD"
aliases:
  - "Aluminum Profile Surface Defect Detection Dataset"
  - "Aluminum Profile Surface Detection Database"
related_domain: "[[Metal inspection]]"
url: "https://tianchi.aliyun.com/dataset/148297"
data_sources:
  - "Alibaba Cloud Tianchi"
  - "2018 Guangdong Industrial Intelligent Manufacturing Big Data Innovation Competition"
introduced_by: "not reported"
related_papers:
  - "[[2025 - You Only Look Once-Aluminum]]"
  - "[[2024 - Surface Defect Detection of Hot Rolled Steel Based on Multi-Scale Feature Fusion and Attention Mechanism Residual Block]]"
---
# APDDD

## Definition

APDDD is an aluminum profile surface defect detection dataset from the Aliyun Tianchi competition. The 2025 YOLO-AL paper describes it as the Aluminum Profile Surface Detection Database and reports 3719 images, 5279 labeled boxes, 640 x 640 image resolution, and 10 aluminum surface defect categories.

## Dataset Details

- Defect categories: non-conductive, scratch, corner-leaky-bottom, orange-peel, leaky-bottom, jet-stream, paint-bubble, pitting, variegated-color, and dirty-spots.
- Image resolution: 640 x 640.
- Size reported by [[2025 - You Only Look Once-Aluminum]]: 3719 images and 5279 labeled frames.
- Split reported by [[2025 - You Only Look Once-Aluminum]]: training, validation, and testing sets in a 7:1.5:1.5 ratio.
- Availability: public host recorded at Alibaba Cloud Tianchi; the 2025 paper's own data availability statement says supporting data are available from the corresponding author upon request.

## Why It Matters

It provides an aluminum-profile benchmark for [[Metallic surface defect detection]] with multiple surface defect types, bounding-box annotations, and small or low-resolution defect cases. It is useful for testing whether metal surface defect detectors transfer beyond steel-strip datasets such as [[NEU-DET]] and [[GC10-DET]].

## Used In These Papers

- [[2024 - Surface Defect Detection of Hot Rolled Steel Based on Multi-Scale Feature Fusion and Attention Mechanism Residual Block]] reports 59.2% mAP on APDDD.
- [[2024 - Feature Optimization-Guided High-Precision and Real-Time Metal Surface Defect Detection Network]] evaluates FOHR Net on APDDD and reports 65.9% [[mAP]] for aluminum profile defect detection.
- [[2025 - You Only Look Once-Aluminum]] trains and evaluates [[YOLO-AL]] on APDDD, reporting 86.5% precision, 77.8% recall, and 81.5% [[mAP@0.50]].

## Source Anchors

- Hosting source: https://tianchi.aliyun.com/dataset/148297.
- Dataset metadata page: https://www.selectdataset.com/dataset/14076c829d181f73ccbf21602e565a93.
- Source lineage: APDDD is described as a defect-detection reconstruction of the 2018 Guangdong Industrial Intelligent Manufacturing Big Data Innovation Competition aluminum-profile surface-defect recognition data.
- Introducing paper: not reported in the processed sources.
- Detailed dataset description paper: [[2025 - You Only Look Once-Aluminum]].
- Usage paper: [[2024 - Surface Defect Detection of Hot Rolled Steel Based on Multi-Scale Feature Fusion and Attention Mechanism Residual Block]] reports APDDD evaluation results.

## Related Concepts

- [[Metallic surface defect detection]]
- [[Object detection]]
- [[Metal inspection]]
- [[YOLO-AL]]
- [[NEU-DET]]
- [[GC10-DET]]
