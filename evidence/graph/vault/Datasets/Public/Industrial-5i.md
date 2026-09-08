---
title: "Industrial-5i"
aliases:
  - "Industrial 5i"
  - "A Data Set For Few-Shot Segmentation on Industrial Surface Defect Detation"
doi: "10.57760/sciencedb.06908"
url: "https://www.scidb.cn/en/detail?dataSetId=e1c585f563ff47c58bbacd832bac12ba"
data_sources:
  - "Science Data Bank"
related_domain: "[[Multi-industry anomaly detection]]"
introduced_by: "[[2023 - Few-shot semantic segmentation for industrial defect recognition]]"
licenses: "CC BY-NC-SA 4.0"
availability: "public"
version: "V1"
published: "2022-12-21"
size_bytes: 2536638625
status: "stable"
concept_type: "dataset"
related_tasks:
  - "[[Defect segmentation]]"
  - "[[Industrial anomaly detection]]"
related_benchmarks:
  - "[[Industrial-5i few-shot segmentation benchmark]]"
---

# Industrial-5i

## Definition

Industrial-5i is a public few-shot segmentation dataset for industrial surface-defect recognition. It contains 20 product categories assembled from MVTec AD, KolektorSDD, Magnetic Tile Defect, RSDDs, and BSData. Each product has normal samples without defects and abnormal samples with pixel-level binary masks.

## Why It Matters

Industrial-5i turns several industrial defect datasets into a shared k-shot segmentation benchmark. It supports evaluation of models that must segment defects on new product categories from only a few normal support examples.

## Dataset Details

- Hosting source: [Science Data Bank](https://www.scidb.cn/en/detail?dataSetId=e1c585f563ff47c58bbacd832bac12ba).
- DOI: [10.57760/sciencedb.06908](https://doi.org/10.57760/sciencedb.06908).
- Access: public.
- License: [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).
- Version: V1.
- Published: 2022-12-21.
- Size: 2,536,638,625 bytes.
- Creator: Xiangwen Shi.
- Keywords: few-shot segmentation, industrial surface defect, image segmentation.
- Source datasets: [[MVTec AD]], [[KolektorSDD]], [[KolektorSDD2]], [[Magnetic Tile Defects]], [[RSDDs]], and [[BSData]].

## Product Folds

| Fold | Product | Normal | Abnormal |
|---|---:|---:|---:|
| 0 | Wood | 266 | 60 |
| 0 | Pill | 293 | 141 |
| 0 | BSD | 362 | 426 |
| 0 | Railway | 105 | 94 |
| 0 | Toothbrush | 72 | 30 |
| 1 | Leather | 277 | 92 |
| 1 | Mutou | 867 | 1838 |
| 1 | Metal-Nut | 242 | 70 |
| 1 | Kolektor-SDD2 | 6235 | 436 |
| 1 | Bottle | 229 | 63 |
| 2 | Carpet | 308 | 89 |
| 2 | Hazelnut | 431 | 70 |
| 2 | Phone | 39 | 100 |
| 2 | Tile | 263 | 84 |
| 2 | Grid | 285 | 57 |
| 3 | Magnetic-Tile | 952 | 392 |
| 3 | Capsule | 242 | 109 |
| 3 | Cable | 282 | 92 |
| 3 | Kolektor-SDD | 746 | 52 |
| 3 | Zipper | 272 | 119 |

## Benchmark Protocol

[[2023 - Few-shot semantic segmentation for industrial defect recognition]] uses four-fold cross-validation: one fold is held out for testing and the remaining product categories are used for training. Each episode samples K normal support images and one abnormal query image with a binary mask. The paper reports [[mIoU]] and [[FB-IoU]] and randomly samples 1000 episodes in each test fold.

## Citation

```bibtex
@data{ e1c585f563ff47c58bbacd832bac12ba,
  title        = {{A Data Set For Few-Shot Segmentation on Industrial Surface Defect Detation}},
  author       = {{Xiangwen Shi}},
  year         = {{2022}},
  month        = {{December}},
  publisher    = {{Science Data Bank}},
  doi          = {{10.57760/sciencedb.06908}},
  url          = {{https://doi.org/10.57760/sciencedb.06908}},
  version      = {{V1}}
}
```

## Used In These Papers

- [[2023 - Few-shot semantic segmentation for industrial defect recognition]] introduces Industrial-5i and evaluates few-shot defect segmentation on its four folds.

## Source Anchors

- Dataset host: [ScienceDB dataset page](https://www.scidb.cn/en/detail?dataSetId=e1c585f563ff47c58bbacd832bac12ba).
- Dataset DOI: [10.57760/sciencedb.06908](https://doi.org/10.57760/sciencedb.06908).
- Introducing paper: [[2023 - Few-shot semantic segmentation for industrial defect recognition]].

## Related Concepts

- [[Industrial-5i few-shot segmentation benchmark]]
- [[Industrial anomaly detection]]
- [[Defect segmentation]]
- [[Multi-industry anomaly detection]]
- [[Few-shot anomaly detection]]
