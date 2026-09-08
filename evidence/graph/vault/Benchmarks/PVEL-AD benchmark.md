---
title: "PVEL-AD benchmark"
aliases:
  - "PVEL-AD object detection benchmark"
dataset: "[[PVEL-AD]]"
tasks:
  - "[[Solar cell defect detection]]"
metrics:
  - "[[Average precision]]"
  - "[[mAP]]"
  - "[[FPS]]"
source_papers:
  - "[[2023 - PVEL-AD A Large-Scale Open-World Dataset for Photovoltaic Cell Anomaly Detection]]"
  - "[[2024 - Enhanced Photovoltaic Panel Defect Detection via Adaptive Complementary Fusion in YOLO-ACF]]"
---

# PVEL-AD Benchmark

## Definition

PVEL-AD benchmark is the object-detection evaluation setup introduced with [[PVEL-AD]] for photovoltaic-cell anomaly detection in electroluminescence images.

## Why It Matters

The benchmark gives later [[Solar cell defect detection]] methods a reference point on a large public PV EL dataset with box-wise annotations and long-tailed anomaly categories.

## Protocol

- Dataset: [[PVEL-AD]].
- Task: detect and localize photovoltaic-cell anomalies with bounding boxes.
- Baselines: Faster RPAN-CNN, YOLOv5-s/m/l, EfficientDet-D0/D1/D2/D3, and BAF-Detector.
- Metrics: [[Average precision]], [[mAP]], and [[FPS]].
- Compute: experiments are reported on a 24 GB RTX 3090 GPU.

## Reported Results

| Method / Setting | Metric | Reported value | Notes |
|---|---|---:|---|
| YOLOv5-l | mAP50:5:95 | 51.13% | Best overall mAP result stated in prose. |
| YOLOv5-s | FPS | 111.11 | Fastest detector stated in prose. |
| EfficientDet-D0 | Parameters / FPS | 3.9M / 83.33 FPS | Fewest parameters, but not fastest. |
| YOLOv5-l on linear crack | AP50 | 66.04% | Linear cracks are difficult because many are small and near cell edges. |
| BAF-Detector on black core | AP50 | 98.25% | Best black-core result stated in prose. |
| BAF-Detector on finger interruption | AP50 | 94.24% | Best finger-interruption result stated in prose. |
| EfficientDet-D3 on thick line | AP50 | 72.71% | Best thick-line result stated in prose. |
| YOLO-ACF selected subset | mAP50 / mAP50-95 | 92.6% / 62.1% | Reported by [[2024 - Enhanced Photovoltaic Panel Defect Detection via Adaptive Complementary Fusion in YOLO-ACF]] on nine defect classes plus normal. |
| YOLO-ACF selected subset | Recall / FPS | 92.3% / 147 FPS | Reported on Intel Xeon E5-2678 v3 and NVIDIA GTX 1080 Ti. |

## Limitations

- Exact numeric cells from the benchmark tables were not preserved in the available text extraction.
- No detector wins across every defect category and efficiency metric.
- Linear crack and thick line defects remain challenging under small scale and heterogeneous background interference.
- [[2024 - Enhanced Photovoltaic Panel Defect Detection via Adaptive Complementary Fusion in YOLO-ACF]] uses a selected PVEL-AD subset rather than every public defect type; the selected corner class has no validation instances and only two test instances.

## Related Concepts

- [[PVEL-AD]]
- [[Solar cell defect detection]]
- [[Average precision]]
- [[mAP]]
- [[FPS]]
- [[YOLOv5]]
- [[YOLO-ACF]]
