---
title: "GiPL: Generative augmented iterative Pseudo-Labeling for Cross-Domain Few-Shot Object Detection"
aliases:
  - "GiPL"
  - "GiPL-Grounding"
paper_key: "doi:10.48550/arxiv.2605.29539"
paper_type: research
year: 2026
venue: "arXiv"
authors:
  - "Jiacong Liu"
  - "Shu Luo"
  - "Yikai Qin"
  - "Yaze Zhao"
  - "Yongwei Jiang"
  - "Yixiong Zou"
status: processed
topics:
  - "cross-domain few-shot object detection"
  - "vision-language detection"
  - "pseudo-labeling"
  - "generative data augmentation"
tasks:
  - "[[Cross-domain few-shot object detection]]"
  - "[[Object detection]]"
  - "[[Car damage detection]]"
datasets:
  - "[[RUOD]]"
  - "[[CARPK]]"
  - "[[CarDD]]"
methods:
  - "[[GiPL]]"
  - "[[Pseudo-labeling]]"
  - "[[Qwen-Image generative augmentation]]"
  - "[[Data augmentation]]"
  - "[[Learned generative synthesis]]"
model_family:
  - "[[Vision-language object detection]]"
architectures:
  - "[[GroundingDINO]]"
  - "[[GLIP]]"
  - "Swin-B"
  - "Swin-L"
losses:
  - "contrastive alignment loss for GLIP background discussion"
optimizers:
  - "not reported"
training_regime:
  - "few-shot fine-tuning"
  - "iterative self-training"
  - "generative augmentation"
augmentation:
  - "[[Qwen-Image generative augmentation]]"
synthetic_data:
  - "domain-aligned multi-object generated images"
metrics:
  - "[[mAP@0.50]]"
primary_metric: "[[mAP@0.50]]"
metric_definitions:
  - "mAP@0.5: mean average precision at IoU threshold 0.5; higher is better."
baselines:
  - "[[GroundingDINO]]"
  - "[[GLIP]]"
  - "ETS"
benchmarks:
  - "2nd Cross-Domain Few-Shot Object Detection Challenge"
code: "CDiscover; URL not reported"
data: "RUOD, CARPK, and CarDD are used; source access details are not reported for RUOD or CARPK in this paper."
doi: "10.48550/arxiv.2605.29539"
arxiv: "2605.29539"
url: "https://arxiv.org/abs/2605.29539"
pdf: "https://arxiv.org/pdf/2605.29539"
related_papers:
  - "[[2023 - CarDD A New Dataset for Vision-Based Car Damage Detection]]"
related_concepts:
  - "[[Cross-domain few-shot object detection]]"
  - "[[Domain gap]]"
related_methods:
  - "[[GiPL]]"
  - "[[Pseudo-labeling]]"
  - "[[Qwen-Image generative augmentation]]"
  - "[[Data augmentation]]"
related_datasets:
  - "[[RUOD]]"
  - "[[CARPK]]"
  - "[[CarDD]]"
related_domains:
  - "[[Underwater object detection]]"
  - "[[Parking lot vehicle monitoring]]"
  - "[[Automotive damage assessment]]"
related_tasks:
  - "[[Cross-domain few-shot object detection]]"
  - "[[Object detection]]"
  - "[[Car damage detection]]"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2026 - Liu - GiPL Generative augmented iterative Pseudo-Labeling for Cross-Domain Few-Shot Object Detection.md"
extracted_text: "paper-inbox/90_processing/text/2026 - Liu - GiPL Generative augmented iterative Pseudo-Labeling for Cross-Domain Few-Shot Object Detection.txt"
source_file: "paper-inbox/10_processed/Research/2026 - Liu - GiPL Generative augmented iterative Pseudo-Labeling for Cross-Domain Few-Shot Object Detection.pdf"
note_created: 2026-06-15
processed_at: 2026-06-15
---
# GiPL: Generative augmented iterative Pseudo-Labeling for Cross-Domain Few-Shot Object Detection

## Summary

GiPL is a dataset-adaptive framework for [[Cross-domain few-shot object detection]]. It addresses two failure modes in few-shot target-domain fine-tuning of vision-language detectors: sparse support annotations that mark only one instance per image, and overfitting from extremely limited target-domain samples. The paper evaluates [[GLIP]] and [[GroundingDINO]] variants on [[RUOD]], [[CARPK]], and [[CarDD]] under 1-shot, 5-shot, and 10-shot protocols, reporting higher [[mAP@0.50]] than the selected baseline models in all listed settings.

## Paper Type

Research paper. It proposes a training framework and evaluates dataset-specific branches for cross-domain few-shot object detection.

## Problem

[[Cross-domain few-shot object detection]] adapts a detector to a target domain with only K labeled examples per novel class. The paper focuses on two target-domain bottlenecks:

- Sparse support labels: few-shot support sets may contain multiple objects but annotate only one instance, so correct extra detections are penalized as false positives during fine-tuning.
- Data scarcity and domain shift: fine-tuning large vision-language detectors on very few target samples can overfit and can even reduce performance below zero-shot behavior for some categories.

## Contribution

- Proposes [[GiPL]], a two-branch framework that selects either iterative pseudo-label self-training or generative augmentation depending on target-dataset failure mode.
- Uses [[Pseudo-labeling]] on [[CARPK]] to recover missing vehicle annotations and improve dense multi-object detection.
- Uses [[Qwen-Image generative augmentation]] on [[RUOD]] and [[CarDD]] to synthesize domain-aligned, multi-object annotated images for low-shot training.
- Reports a 192.7929 score and second place in the 2nd Cross-Domain Few-Shot Object Detection Challenge.

## Method

### Model Selection

- [[CARPK]]: [[GLIP]]-L with a Swin-L backbone for dense multi-object vehicle scenes.
- [[RUOD]] and [[CarDD]]: [[GroundingDINO]] with a Swin-B backbone for underwater objects and fine-grained car-damage localization.

### Branch 1: Iterative Pseudo-Labeling

For CARPK, GiPL follows a closed loop:

1. Fine-tune the detector on the few-shot annotations.
2. Run inference on target training/support images.
3. Filter predictions by score threshold.
4. Apply class-wise non-maximum suppression.
5. Convert retained boxes into COCO-style pseudo annotations.
6. Merge pseudo labels with original annotations and retrain.

The paper states that the best pseudo-label confidence threshold is 0.6. Lower thresholds admit lower-quality pseudo boxes, while higher thresholds keep too few boxes for effective supervision.

### Branch 2: Generative Augmentation

For RUOD and CarDD, GiPL uses [[Qwen-Image generative augmentation]] with Qwen-Image-2.0-pro. Given a support image and class prompt, the generator creates images that preserve target-domain style, background, and object characteristics while adding valid visual variation. The prompt asks the model to generate class objects and provide object-detection bounding boxes in a text file.

The paper also uses standard detection augmentations, but the exact standard augmentation settings are not reported.

## Evidence

### Datasets

| Dataset | Domain / target | Reported challenge | GiPL branch |
|---|---|---|---|
| [[RUOD]] | Underwater object detection | low contrast, color distortion, turbidity, domain shift | Qwen-based generative augmentation |
| [[CARPK]] | Drone-based parking-lot vehicle detection | high-density vehicles and sparse few-shot annotations | iterative pseudo-labeling |
| [[CarDD]] | Car damage detection | fine-grained dents, scratches, and damage localization | Qwen-based generative augmentation |

### Main Results

All values are [[mAP@0.50]]; higher is better.

| Shot | Baseline | RUOD | CARPK | CarDD | Avg. | GiPL Avg. improvement |
|---|---:|---:|---:|---:|---:|---:|
| 1-shot baseline | GroundingDINO | 31.5 | 49.0 | 34.2 | 38.2 |  |
| 1-shot GiPL | GiPL | 34.6 | 63.3 | 39.7 | 45.9 | +7.7 avg points |
| 5-shot baseline | GLIP | 35.8 | 42.0 | 43.8 | 40.5 |  |
| 5-shot GiPL | GiPL | 41.1 | 63.0 | 47.4 | 50.5 | +10.0 avg points |
| 10-shot baseline | GroundingDINO | 34.6 | 40.0 | 47.0 | 40.5 |  |
| 10-shot GiPL | GiPL | 42.1 | 61.3 | 48.3 | 50.6 | +10.1 avg points |

The introduction reports average performance gains of 7.63%, 9.97%, and 10.03% for 1-shot, 5-shot, and 10-shot settings; the table values correspond to about +7.7, +10.0, and +10.1 average mAP points.

### Generative Augmentation Ablation

Table 2 isolates Qwen-based augmentation on RUOD and CarDD with [[GroundingDINO]].

| Shot | Method | RUOD | CarDD | Avg. |
|---|---|---:|---:|---:|
| 1-shot | Zero-shot | 31.5 | 12.0 | 21.75 |
| 1-shot | + ETS | 30.8 | 34.2 | 32.50 |
| 1-shot | + Augmentation | 34.6 | 39.7 | 37.15 |
| 5-shot | Zero-shot | 31.5 | 12.0 | 21.75 |
| 5-shot | + ETS | 35.8 | 43.8 | 39.80 |
| 5-shot | + Augmentation | 41.1 | 47.4 | 44.25 |
| 10-shot | Zero-shot | 31.5 | 12.0 | 21.75 |
| 10-shot | + ETS | 34.6 | 47.0 | 40.80 |
| 10-shot | + Augmentation | 42.1 | 48.3 | 45.20 |

### Pseudo-Labeling Ablation

Table 3 isolates pseudo-labeling on CARPK with [[GLIP]].

| Shot | Method | CARPK mAP@0.50 |
|---|---|---:|
| 1-shot | Zero-shot | 50.7 |
| 1-shot | fine-tuned | 49.4 |
| 1-shot | Pseudo-Label | 63.3 |
| 5-shot | Zero-shot | 50.7 |
| 5-shot | fine-tuned | 42.5 |
| 5-shot | Pseudo-Label | 63.0 |
| 10-shot | Zero-shot | 50.7 |
| 10-shot | fine-tuned | 40.9 |
| 10-shot | Pseudo-Label | 61.3 |

The pseudo-labeling branch reverses the degradation from vanilla fine-tuning on CARPK, where sparse annotations cause valid vehicle detections to be treated as background.

### Performance Metrics

| Metric | Definition / context | Direction | Primary |
|---|---|---|---|
| [[mAP@0.50]] | mean average precision at IoU threshold 0.5 for object detection | higher is better | yes |

## ML/DL Extraction

- Task formulation: N-way K-shot cross-domain object detection, with support set labels and query-set evaluation.
- Inputs: target-domain support images, text category prompts, and bounding-box annotations.
- Outputs: object categories and bounding boxes.
- Model family: vision-language object detection with grounded text-image alignment.
- Architectures: [[GLIP]]-L with Swin-L for CARPK; [[GroundingDINO]] with Swin-B for RUOD and CarDD.
- Objective/loss: GLIP background discussion mentions contrastive alignment loss; GiPL-specific training losses are not reported beyond fine-tuning/self-training.
- Optimizer: not reported.
- Training recipe: CARPK uses 200 epochs, learning rate 5e-5, batch size 2; RUOD and CarDD use 50 epochs, batch size 4, one NVIDIA A6000 GPU.
- Augmentation: Qwen-Image-2.0-pro generates semantically consistent, domain-aligned, multi-object images with bounding boxes for RUOD and CarDD; standard detection augmentations are also used but not detailed.
- Inference: standard single-model inference without test-time augmentation; non-maximum suppression removes highly overlapped predictions.
- Code/artifacts: the paper states code is available at CDiscover; URL is not reported in the available source.

## Limitations

- The paper does not report optimizer, exact loss functions, seeds, or full hyperparameter schedules.
- The generative augmentation branch depends on Qwen-Image-2.0-pro, but the paper does not quantify generation cost, filtering criteria, or failure cases for malformed boxes.
- Dataset availability details are not reported for RUOD or CARPK in the paper.
- The framework uses different branches for different datasets, so the results do not show whether both branches combined improve each dataset.
- The evaluation is limited to three challenge datasets and mAP@0.5; stricter localization metrics are not reported.

## Connections

### Builds on

- [[GLIP]] - used as the detector for dense CARPK vehicle scenes.
- [[GroundingDINO]] - used for RUOD and CarDD target-domain detection.
- [[Pseudo-labeling]] - adapted into an iterative object-detection self-training loop.
- [[Learned generative synthesis]] - Qwen-generated images provide the synthetic augmentation branch.

### Shares dataset

- [[CarDD]] - reused as the car-damage target dataset; the paper evaluates 1/5/10-shot object detection on it.
- [[RUOD]] - reused as the underwater target dataset.
- [[CARPK]] - reused as the dense parking-lot vehicle target dataset.

### Shares task

- [[Cross-domain few-shot object detection]] - GiPL targets cross-domain detector adaptation under 1/5/10-shot settings.
- [[Object detection]] - all experiments evaluate bounding-box detection.
- [[Car damage detection]] - CarDD experiments localize fine-grained car damage.

### Shares method

- [[Qwen-Image generative augmentation]] - creates domain-aligned annotated images for scarce support sets.
- [[Data augmentation]] - GiPL uses generated and standard detection augmentations to reduce overfitting.

### Shares metric

- [[mAP@0.50]] - the primary reported evaluation metric.

### Application/domain

- [[Underwater object detection]] - RUOD domain.
- [[Parking lot vehicle monitoring]] - CARPK domain.
- [[Automotive damage assessment]] - CarDD domain.

### Graph Hubs

- Tasks: [[Cross-domain few-shot object detection]], [[Object detection]], [[Car damage detection]]
- Methods: [[GiPL]], [[Pseudo-labeling]], [[Qwen-Image generative augmentation]], [[Data augmentation]], [[Learned generative synthesis]]
- Models: [[GroundingDINO]], [[GLIP]], [[Vision-language object detection]]
- Datasets: [[RUOD]], [[CARPK]], [[CarDD]]
- Domains: [[Underwater object detection]], [[Parking lot vehicle monitoring]], [[Automotive damage assessment]]
- Metrics: [[mAP@0.50]]

## Questions

- What exact CDiscover URL, code license, and released scripts correspond to the paper?
- How many generated images are added per support image for RUOD and CarDD?
- What filtering, human checking, or automatic validation is applied to generated bounding boxes?
- Would combining pseudo-labeling and Qwen augmentation improve each dataset, or do the branches interfere?
- How does GiPL perform under stricter COCO-style mAP across IoU thresholds?

## Source Anchors

- arXiv: https://arxiv.org/abs/2605.29539
- PDF: https://arxiv.org/pdf/2605.29539
- Local analysis input: `paper-inbox/90_processing/analysis-inputs/2026 - Liu - GiPL Generative augmented iterative Pseudo-Labeling for Cross-Domain Few-Shot Object Detection.md`
