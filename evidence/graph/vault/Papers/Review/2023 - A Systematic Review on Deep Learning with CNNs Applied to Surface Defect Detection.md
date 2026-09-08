---
title: "A Systematic Review on Deep Learning with CNNs Applied to Surface Defect Detection"
aliases:
  - "A Systematic Review on Deep Learning with CNNs Applied to Surface Defect Detection"
paper_key: "doi:10.3390/jimaging9100193"
paper_type: review
year: 2023
venue: "Journal of Imaging"
authors:
  - "Esteban Cumbajin"
  - "Nuno Rodrigues"
  - "Paulo Costa"
  - "Rolando Miragaia"
  - "Luis Frazao"
  - "Nuno Costa"
  - "Antonio Fernandez-Caballero"
  - "Jorge Carneiro"
  - "Leire H. Buruberri"
  - "Antonio Pereira"
status: processed
processed_at: 2026-05-21
topics:
  - industrial defect detection
  - systematic review
  - CNN-based visual inspection
tasks:
  - "[[Surface defect detection]]"
  - "[[Defect classification]]"
  - "[[Object detection]]"
  - "[[Defect segmentation]]"
domains:
  - "[[Industrial visual inspection]]"
datasets:
  - "not applicable"
methods:
  - "[[Deep convolutional neural network]]"
  - "[[Data augmentation]]"
model_family:
  - "[[Deep convolutional neural network]]"
learning_paradigms:
  - "[[Transfer learning]]"
metrics:
  - "not applicable"
primary_metric: "not applicable"
benchmarks:
  - "not applicable"
code: "not reported"
data: "restricted by research collaboration and data confidentiality statement"
doi: "10.3390/jimaging9100193"
arxiv: "not reported"
url: "https://doi.org/10.3390/jimaging9100193"
pdf: "not reported"
related_concepts:
  - "[[Surface defect detection]]"
  - "[[Industrial visual inspection]]"
related_methods:
  - "[[Deep convolutional neural network]]"
  - "[[Data augmentation]]"
related_datasets:
  - "not applicable"
related_domains:
  - "[[Industrial visual inspection]]"
related_tasks:
  - "[[Surface defect detection]]"
  - "[[Defect classification]]"
  - "[[Object detection]]"
  - "[[Defect segmentation]]"
source_file: "paper-inbox/10_processed/2023 - Cumbajin - A Systematic Review on Deep Learning with CNNs Applied to Surface Defect Detection.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2023 - Cumbajin - A Systematic Review on Deep Learning with CNNs Applied to Surface Defect Detection.md"
extracted_text: "paper-inbox/90_processing/text/2023 - Cumbajin - A Systematic Review on Deep Learning with CNNs Applied to Surface Defect Detection.txt"
artifact_status: "review data restricted per source"
tags:
  - paper
---

# A Systematic Review on Deep Learning with CNNs Applied to Surface Defect Detection

## Summary

This systematic review classifies supervised CNN-based image studies for [[Surface defect detection]] published from 2011 through 2021. The final corpus contains 59 primary studies after database search, duplicate removal, screening, and quality assessment. The review organizes the literature by surface type, problem type, network architecture, improvement technique, dataset origin and availability, camera type, and publication year.

The strongest aggregate findings are that metal surfaces dominate the reviewed literature, image classification is the most common task, custom CNN variants are more common than unchanged CNNs, and transfer learning plus data augmentation are the main performance-improvement techniques. The review also emphasizes a recurring reporting gap: many primary studies omit camera, lighting, image-size, and dataset-size details needed for practical industrial reuse.

## Paper Type

- Type: review.
- Why: The paper follows a systematic review protocol, uses PRISMA-style filtering, quality assessment, and research questions rather than introducing a new detector or dataset.

## Problem

- Task: review CNN-based [[Surface defect detection]].
- Scope: supervised learning studies using images of surface defects.
- Surfaces: metal, building/construction, ceramic, wood, and special surfaces.
- Problem types: [[Defect classification]], [[Object detection]], semantic segmentation, and instance segmentation.
- Motivation: surface defects affect industrial quality and costs, while CNN-based methods have become increasingly used for automated inspection.
- Exclusions: studies without empirical CNN analysis, non-surface-defect CNN uses, non-image datasets, abstract-only records, articles in press, and studies where image acquisition used signals or sensors instead of cameras.

## Contribution

- Provides a systematic taxonomy of CNN-based surface defect detection literature across surface types, task types, architectures, improvement techniques, dataset origin, camera source, and timeline.
- Quantifies major trends: metal surfaces appear in 62.71% of final studies, image classification in 49.15%, custom CNNs in 67.80%, transfer learning in 83.05%, and data augmentation in 59.32%.
- Identifies practical reproducibility gaps around image capture, lighting, image size, and dataset quantity reporting.

## Method

- Search databases: Scopus, IEEE Xplore, ACM Digital Library, and Web of Science.
- Search date: 10 March 2022.
- Study window: 2011-2021, chosen around the post-AlexNet deep learning period.
- Search key: surface terms for ceramic, metal, wall, wood, and building combined with defect terms, quality-control/detection terms, and CNN/deep-learning terms.
- Selection flow: 253 records identified, 136 after duplicate filtering, 118 after title/document-type/download filtering, 71 after abstract/conclusion filtering, 62 after full analysis, and 59 after quality assessment.
- Quality assessment: nine QA questions scored yes = 1, partially = 0.5, no = 0; only medium-or-higher quality studies were retained.

## ML / DL Extraction

### Review Taxonomy

- Surface type: metal, building/construction, ceramic, wood, special.
- Problem type: image classification, object detection, semantic segmentation, instance segmentation.
- Architecture type: unchanged CNN versus custom CNN.
- Improvement technique: [[Transfer learning]], [[Data augmentation]], both, or no reported technique.
- Dataset origin: created by authors versus already existing.
- Camera/source type: industrial camera, nonindustrial camera, dataset camera, or no information.

### Model And Training

- Model family: [[Deep convolutional neural network]].
- Architectures found across the reviewed studies include AlexNet, GoogLeNet, ResNet, DenseNet, VGG, Inception, Xception, SSD, Faster R-CNN, Mask R-CNN, YOLO variants, RetinaNet, U-Net, FCN, R-CNN, and custom CNN variants.
- Supervision: all included primary studies use supervised learning.
- Training details: not applicable to the review itself; individual primary studies vary.

### Data

- Review corpus: 59 primary studies.
- Primary-study dataset origin: 46 created datasets (77.97%) and 13 already-existing datasets (22.03%).
- Dataset availability across all primary studies: 39 private (66.10%) and 20 public (33.90%).
- Created-dataset availability: 39 private and 7 public, reported as 86.67% private and 13.33% public.
- Public datasets named as recurring examples include Kaggle datasets, KITTI, SDNET2018, GDXray, NEU, ALCIDE, BS5-DET, CSU_STEEL, GC10-DET, KolektorSDD, and datasets created in two reviewed studies.
- Data availability for the review: restricted by research collaboration and data confidentiality statement.

### Evaluation

- This is a literature review, so performance metrics for a new model are not applicable.
- The review reports descriptive counts and percentages by taxonomy category.
- No statistical significance testing is reported.

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| not applicable | review synthesis | The paper does not evaluate a new model. | not applicable | not applicable | The review reports corpus counts and percentages rather than model-performance scores. |

## Evidence

### Corpus Construction

| Stage | Count | Notes |
|---|---:|---|
| Initial records | 253 | Search key applied to four digital libraries |
| After duplicate filtering | 136 | Duplicate records removed |
| After title/document/download filtering | 118 | Initial relevance and accessibility screening |
| After abstract/conclusion filtering | 71 | Excluded records outside the CNN surface-defect scope |
| After full analysis | 62 | Excluded 9 studies because acquisition did not use cameras |
| Final corpus | 59 | Three low-quality studies discarded by QA |

### Main Review Findings

| Research question | Result | Count | Percentage | Notes |
|---|---:|---:|---:|---|
| Surface type: metal | Most common surface | 37 | 62.71% | Metal reflections and glare are recurring difficulties |
| Surface type: building | Second most common | 11 | 18.64% | Includes bridges, pavement, roads, houses, dams, masonry, and concrete |
| Surface type: special | Less common but diverse | 6 | 10.17% | Includes paintings, mobile phone back glass, decorative sheets, commutators, and sealing surfaces |
| Surface type: ceramic | Few studies | 3 | 5.08% | Breaks, cracks, pinholes, dirt, pits, and spots are reported examples |
| Surface type: wood | Fewest studies | 2 | 3.39% | Wood texture makes augmentation useful |
| Problem type: classification | Most common problem type | 29 | 49.15% | Lowest computational cost among listed task types |
| Problem type: object detection | Second most common | 20 | 33.90% | Adds defect location information |
| Problem type: semantic segmentation | Less common | 7 | 11.86% | Higher computational and annotation cost |
| Problem type: instance segmentation | Least common | 3 | 5.08% | Highest detail but higher resource cost |
| Architecture: custom CNN | Dominant architecture category | 40 | 67.80% | Includes CNNs modified or created for the experiment |
| Architecture: unchanged CNN | Less common | 19 | 32.20% | Uses existing CNNs without structural customization |
| Technique: transfer learning | Most used technique | 49 | 83.05% | Often used because target datasets are small |
| Technique: data augmentation | Common technique | 36 | 59.32% | Used to address small or imbalanced datasets |

### Dataset And Camera Findings

| Category | Count | Percentage | Notes |
|---|---:|---:|---|
| Created datasets | 46 | 77.97% | Most experiments require new image capture because public datasets often do not match the target surface |
| Already-existing datasets | 13 | 22.03% | Used for comparisons and method validation |
| Private datasets | 39 | 66.10% | Industry constraints commonly prevent release |
| Public datasets | 20 | 33.90% | NEU is reported as a frequently used surface-defect dataset |
| Industrial cameras | 26 | 44.07% | Most common camera type; often requires controlled lighting and lenses |
| Nonindustrial cameras | 15 | 25.42% | Includes smartphone, USB, drone, and common-use cameras |
| Dataset images only | 9 | 15.25% | No new camera acquisition in those studies |
| Camera type not specified | 9 | 15.25% | Limits practical industrial reuse |

### Timeline

| Year | Studies | Percentage |
|---|---:|---:|
| 2017 | 2 | 3.39% |
| 2018 | 6 | 10.17% |
| 2019 | 11 | 18.64% |
| 2020 | 18 | 30.51% |
| 2021 | 22 | 37.29% |

## Review / Survey Details

- Inclusion criteria: empirical CNN studies for surface defect detection, supervised learning for surface defect detection, studies combining CNNs with other ML techniques, review studies/conference papers/articles, 2011-2021 publication range, English language, and final published versions.
- Exclusion criteria: no empirical CNN results, CNNs outside surface defect detection, non-image datasets, abstract-only sources, and articles in press.
- Quality ranks among assessed studies: 6 very high, 35 high, 18 medium, 2 low, and 1 very low.
- Retention rule: medium-or-higher studies were retained; three low-quality studies were discarded.
- Main lesson: at least one of transfer learning or data augmentation appears in 93.22% of reviewed studies.

## Limitations

- The review reports difficulty finding image capture, lighting, image-size, and dataset-size information in the primary studies.
- Around half of reviewed studies do not provide sufficient information about cameras, lighting, or image size for practical industrial replication.
- Dataset confidentiality is a major constraint; many created datasets are private.
- The review is limited to supervised CNN-based image studies and excludes unsupervised, self-supervised, semi-supervised, reinforcement learning, and non-camera signal/sensor studies.
- The source corpus ends at 2021 because the search was performed on 10 March 2022.

## Reproducibility

- Code: not reported.
- Review data: restricted by research collaboration and data confidentiality statement.
- Search protocol: search key, databases, filtering stages, and inclusion/exclusion criteria are reported.
- Study-quality scoring: nine QA questions and final quality-score appendix are reported.
- Environment: not applicable.
- Checkpoints/models: not applicable.

## Connections

### Graph Hubs

- Tasks: [[Surface defect detection]], [[Defect classification]], [[Object detection]], [[Defect segmentation]]
- Methods: [[Deep convolutional neural network]], [[Data augmentation]]
- Learning paradigms: [[Transfer learning]]
- Domains: [[Industrial visual inspection]]
- Datasets: not applicable
- Metrics: not applicable

### Builds On

- [[Deep convolutional neural network]]: the review surveys CNN-based approaches for image-based surface defect detection.

### Contrasts With

- [[2024 - A Systematic Review of Deep Learning Approaches for Surface Defect Detection in Industrial Applications]]: both review industrial surface defect detection, while this review is specifically scoped to supervised CNN image studies through 2021.
- [[2023 - Deep CNN-Based Visual Defect Detection Survey of Current Literature]]: both survey CNN visual defect detection, but this paper uses a systematic protocol with explicit surface-type and dataset/camera taxonomies.

### Shares Dataset

- not applicable

### Shares Task

- [[Surface defect detection]]: the review’s full corpus is organized around this task.
- [[Defect classification]]: classification is the most frequent problem type in the review.
- [[Object detection]]: the review treats object detection as a separate surface-defect problem type.
- [[Defect segmentation]]: semantic and instance segmentation are included as higher-detail problem types.

### Shares Method

- [[Deep convolutional neural network]]: CNNs are the review’s method-family boundary.
- [[Data augmentation]]: data augmentation is one of the two main improvement techniques quantified by the review.
- [[Transfer learning]]: transfer learning is the most used improvement technique in the final corpus.

### Application / Domain

- [[Industrial visual inspection]]: the review focuses on camera-based visual quality inspection across industrial surface types.

### Follow-Up Reading

- [[2024 - A Systematic Review of Deep Learning Approaches for Surface Defect Detection in Industrial Applications]]
- [[2023 - Deep CNN-Based Visual Defect Detection Survey of Current Literature]]

## Questions

- Which excluded non-supervised or non-camera defect-detection studies should be reviewed separately for anomaly-detection coverage?
- Which public datasets among the review’s named examples should be represented as standalone dataset notes if they recur in processed papers?
