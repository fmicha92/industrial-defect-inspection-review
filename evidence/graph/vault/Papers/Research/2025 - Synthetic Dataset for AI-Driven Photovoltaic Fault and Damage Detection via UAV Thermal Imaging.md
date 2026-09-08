---
title: "Synthetic Dataset for AI-Driven Photovoltaic Fault and Damage Detection via UAV Thermal Imaging"
paper_key: "doi:10.1109/eeae65901.2025.11273362"
doi: "10.1109/EEAE65901.2025.11273362"
url: "https://doi.org/10.1109/EEAE65901.2025.11273362"
authors:
  - "Panagiotis Christakakis"
  - "Periklis Dimou"
  - "Panagiotis Symeonidis"
  - "Dimosthenis Ioannidis"
  - "Dimitrios Tzovaras"
  - "Eleftheria Maria Pechlivani"
year: 2025
venue: "10th International Conference on Energy Efficiency and Agricultural Engineering"
paper_type: "research"
status: "processed"
topics:
  - "photovoltaic fault detection"
  - "UAV thermal imaging"
  - "synthetic data generation"
  - "object detection"
tasks:
  - "[[PV panel fault detection]]"
  - "[[Object detection]]"
domains:
  - "[[Solar cells and photovoltaic]]"
datasets:
  - "[[Thermal PV Panel Detection and Fault Detection Dataset for UAV-Based Inspection]]"
methods:
  - "[[YOLOv11]]"
  - "[[Infrared thermography]]"
  - "[[Synthetic data generation]]"
  - "[[Defect synthesis]]"
  - "[[Poisson defect image augmentation]]"
model_family:
  - "[[YOLOv11]]"
architectures:
  - "[[YOLOv11]]"
training_regime:
  - "[[Transfer learning]]"
metrics:
  - "[[Precision]]"
  - "[[Recall]]"
  - "[[mAP@0.50]]"
primary_metric: "[[mAP@0.50]]"
baselines:
  - "YOLOv11n"
  - "YOLOv11s"
  - "YOLOv11m"
  - "YOLOv11l"
  - "YOLOv11x"
benchmarks: "not reported"
code: "not reported"
data: "[[Thermal PV Panel Detection and Fault Detection Dataset for UAV-Based Inspection]]"
licenses: "CC BY 4.0"
related_concepts:
  - "[[Synthetic data generation]]"
  - "[[Defect synthesis]]"
related_methods:
  - "[[YOLOv11]]"
  - "[[Infrared thermography]]"
  - "[[Poisson defect image augmentation]]"
related_datasets:
  - "[[Thermal PV Panel Detection and Fault Detection Dataset for UAV-Based Inspection]]"
related_domains:
  - "[[Solar cells and photovoltaic]]"
related_tasks:
  - "[[PV panel fault detection]]"
  - "[[Object detection]]"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2025 - Christakakis - Synthetic Dataset for AI-Driven Photovoltaic Fault and Damage Detection via UAV Thermal Imaging.md"
extracted_text: "paper-inbox/90_processing/text/2025 - Christakakis - Synthetic Dataset for AI-Driven Photovoltaic Fault and Damage Detection via UAV Thermal Imaging.txt"
source_file: "paper-inbox/10_processed/Research/2025 - Christakakis - Synthetic Dataset for AI-Driven Photovoltaic Fault and Damage Detection via UAV Thermal Imaging.pdf"
processed_at: "2026-06-04"
---
# Synthetic Dataset for AI-Driven Photovoltaic Fault and Damage Detection via UAV Thermal Imaging

## Summary

The paper introduces a UAV thermal imaging dataset and a synthetic fault-generation pipeline for photovoltaic panel inspection. It uses DJI Mavic 3T thermal imagery from a PV farm in Sindos, Thessaloniki, generates synthetic fault masks with a multimodal large language model, blends them into real thermal panel images, and trains YOLOv11 detectors for panel localization and synthetic fault detection.

## Paper Type

Research paper with a dataset contribution. It introduces [[Thermal PV Panel Detection and Fault Detection Dataset for UAV-Based Inspection]], proposes a synthetic data generation pipeline, and evaluates YOLOv11 object detectors.

## Problem

Manual PV inspections and handheld thermal surveys do not scale well to large solar farms. UAV thermal imagery can cover large areas, but labeled real-world PV fault datasets are scarce, especially for faults such as cracks, hotspots, delamination, snail trails, dust, and damage.

## Contribution

- Captures UAV thermal imagery over a 9,100 square meter PV farm in Thessaloniki, Greece.
- Refines 713 captured thermal images into 353 non-overlapping thermal images with 26,678 annotated PV panels.
- Generates 65 synthetic fault and damage masks using Janus-4o and composites them onto real thermal panel backgrounds.
- Produces a synthetic fault dataset with 638 instances across six fault types.
- Trains YOLOv11 variants for panel detection and synthetic PV fault detection, reporting 95.1% mAP50 for panel detection and 76.9% mAP50 for synthetic fault classification.

## Method

### UAV thermal imaging

The UAV flight used a DJI Mavic 3T at 22-25 meters altitude with a gridded flight path and approximately 3 cm/pixel ground sampling distance. The thermal sensor has 640 x 512 resolution, a 40 mm equivalent focal length, longwave infrared operation at 8-14 micrometers, and temperature measurement accuracy of plus or minus 2 degrees Celsius. The flight was conducted around midday in February 2025 under clear sunny conditions with ambient temperatures from 12 to 14 degrees Celsius.

The authors collected 713 thermal images and the same number of RGB images. Overlapping frames were removed to reduce redundancy and overfitting risk, leaving 353 non-overlapping thermal images. All 713 original images were annotated in Roboflow to preserve metadata, but RGB images were excluded from the reported analysis because the paper treats thermal imaging as the preferred modality for PV fault evidence.

### Synthetic fault generation

The synthetic pipeline uses real intact thermal panels as backgrounds and generated fault instances as pasted objects. Real-world fault examples are used as prompts for Janus-4o, which generates grayscale PNG fault masks with transparent backgrounds. The object set includes 65 unique masks spanning damage, cracks, snail trails, dust, delamination, and hotspots.

Fault instances are geometrically and visually augmented through random resizing, horizontal and vertical flipping, rotation, brightness adjustment, and contrast adjustment. Fault placement uses PV panel bounding boxes so pasted defects remain inside annotated panels. Poisson image blending is used to reduce edge artifacts. Each non-overlapping thermal image has a 50% probability of being altered, and selected images receive faults on a sparse subset of panels.

### Object detection

The paper trains YOLOv11n, YOLOv11s, YOLOv11m, YOLOv11l, and YOLOv11x for panel detection on the real thermal dataset. It then trains YOLOv11m, YOLOv11l, and YOLOv11x on the synthetic fault dataset. Models use transfer learning from COCO-pretrained weights, 100 training epochs, early stopping after 15 stagnant validation-loss epochs, 640 x 640 input resolution, and batch size 4. Training uses SGD with learning rate 0.01, momentum 0.85, and weight decay 0.0005.

## Evidence

### Dataset

- Host dataset: [[Thermal PV Panel Detection and Fault Detection Dataset for UAV-Based Inspection]].
- Captured site: PV farm in Sindos, Thessaloniki.
- Captured set: 713 thermal images and 713 RGB images.
- Refined set: 353 non-overlapping 640 x 512 thermal images.
- Panel annotations after refinement: 26,678.
- Zenodo split: 235 training images with 18,487 panel annotations, 83 validation images with 5,828 panel annotations, and 35 test images with 2,363 panel annotations.
- Synthetic fault instances: damage 102, crack 114, snail trail 98, dust 109, delamination 105, and hotspots 110.

### Panel detection results

| Model | Precision | Recall | mAP50 |
|---|---:|---:|---:|
| YOLOv11n | 0.992 | 0.895 | 0.914 |
| YOLOv11s | 0.992 | 0.899 | 0.944 |
| YOLOv11m | 0.994 | 0.899 | 0.947 |
| YOLOv11l | 0.993 | 0.899 | 0.951 |
| YOLOv11x | 0.993 | 0.900 | 0.946 |

YOLOv11l is the best panel detector by mAP50 at 0.951.

### Synthetic fault detection results

| Model | Damage | Crack | Snail trail | Dust | Delamination | Hotspots | All mAP50 |
|---|---:|---:|---:|---:|---:|---:|---:|
| YOLOv11m | 0.784 | 0.710 | 0.631 | 0.827 | 0.719 | 0.832 | 0.750 |
| YOLOv11l | 0.803 | 0.721 | 0.644 | 0.841 | 0.724 | 0.854 | 0.764 |
| YOLOv11x | 0.807 | 0.728 | 0.649 | 0.850 | 0.722 | 0.859 | 0.769 |

YOLOv11x is the best synthetic fault detector by overall mAP50 at 0.769.

## ML/DL Extraction

- Task formulation: object detection for PV panels and synthetic PV fault categories.
- Input: UAV thermal images.
- Output: bounding boxes and class labels.
- Architecture: YOLOv11 variants.
- Pretraining: COCO-pretrained weights.
- Training recipe: 100 epochs, early stopping after 15 validation-loss stalls, SGD, learning rate 0.01, momentum 0.85, weight decay 0.0005, batch size 4.
- Data synthesis: MLLM-generated fault masks, geometric and visual augmentation, panel-box-constrained placement, and Poisson image blending.
- Evaluation metrics: precision, recall, and mAP50.
- Hardware: Intel Core i9-14900F CPU, 128 GB RAM, and NVIDIA RTX 4090 GPU with 24 GB VRAM.
- Data: Zenodo DOI `10.5281/zenodo.16420123`.
- Code: not reported.

## Limitations

- The inspected solar farm contained no visible defects except seven thermal images with hotspots, so most fault labels come from synthetic overlays rather than real fault annotations.
- RGB images were collected but excluded from the analysis.
- The paper does not report evaluation on an independent real fault test set.
- The synthetic fault dataset is validated through YOLOv11 training, but the paper does not quantify domain gap to real PV faults beyond the limited hotspot cases.
- Zenodo metadata has a small count inconsistency: the prose says 351 processed images, while the split table totals 353 images.

## Connections

### Graph Hubs

- Tasks: [[PV panel fault detection]], [[Object detection]]
- Methods: [[YOLOv11]], [[Infrared thermography]], [[Synthetic data generation]], [[Defect synthesis]], [[Poisson defect image augmentation]], [[Transfer learning]]
- Datasets: [[Thermal PV Panel Detection and Fault Detection Dataset for UAV-Based Inspection]]
- Domains: [[Solar cells and photovoltaic]]
- Metrics: [[Precision]], [[Recall]], [[mAP@0.50]]

### Shares dataset

- [[Thermal PV Panel Detection and Fault Detection Dataset for UAV-Based Inspection]] - the paper introduces and evaluates this Zenodo dataset.

### Shares task

- [[PV panel fault detection]] - the paper detects PV panel fault and damage categories in UAV thermal images.
- [[Object detection]] - both panel detection and fault detection are framed as bounding-box object detection.

### Shares method

- [[YOLOv11]] - the detector family used for panel and synthetic fault detection.
- [[Infrared thermography]] - the sensing modality for UAV inspection.
- [[Synthetic data generation]] and [[Defect synthesis]] - the paper creates synthetic PV faults to overcome scarce real defects.
- [[Poisson defect image augmentation]] - generated faults are blended into real thermal backgrounds with Poisson image blending.
- [[Transfer learning]] - YOLOv11 models are initialized with COCO-pretrained weights.

### Shares metric

- [[Precision]], [[Recall]], and [[mAP@0.50]] - used to evaluate object detection performance.

### Application/domain

- [[Solar cells and photovoltaic]] - the work targets PV farm inspection and maintenance.

## Questions

- How do models trained on the synthetic fault labels perform on real PV fault images beyond hotspots?
- Can RGB and thermal imagery be fused to reduce ambiguity between fault causes?
- Which split convention should be used if Zenodo prose and split-table image counts remain inconsistent?
