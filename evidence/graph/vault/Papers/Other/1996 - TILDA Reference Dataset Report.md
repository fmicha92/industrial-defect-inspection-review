---
title: "TILDA Reference Dataset Report"
aliases:
  - "Ein Referenzdatensatz zur Evaluierung von Sichtpruefungsverfahren fuer Textiloberflaechen"
  - "TILDA-ein Referenzdatensatz zur Evaluierung von Sichtpruefungsverfahren fuer Textiloberflaechen"
paper_key: "sha256:01f65f1d75a4b6522335c0417886d64ee517acda2d4fc0934aa0142919b56f55"
citation_key: "schulz1996tilda"
paper_type: other
year: 1996
venue: "Interner Bericht 4/96"
authors:
  - "Hanns Schulz-Mirbach"
status: processed
processed_at: 2026-06-03
topics:
  - "textile texture database"
  - "visual inspection reference dataset"
tasks:
  - "[[Textile defect detection]]"
domains:
  - "[[Textile and fiber inspection]]"
datasets:
  - "[[TILDA]]"
methods:
  - "[[Reference dataset construction]]"
related_methods:
  - "[[Reference dataset construction]]"
metrics: []
primary_metric: "not applicable"
doi: "not reported"
arxiv: "not reported"
url: "https://lmb.informatik.uni-freiburg.de/resources/datasets/tilda.en.html"
pdf: "paper-inbox/10_processed/Other/1996 - Schulz-Mirbach - Ein Referenzdatensatz zur Evaluierung von Sichtpruefungsverfahren fuer Textiloberflaechen.pdf"
data_sources:
  - "TILDA textile texture database"
licenses: "not reported"
related_datasets:
  - "[[TILDA]]"
related_domains:
  - "[[Textile and fiber inspection]]"
related_tasks:
  - "[[Textile defect detection]]"
source_file: "paper-inbox/10_processed/Other/1996 - Schulz-Mirbach - Ein Referenzdatensatz zur Evaluierung von Sichtpruefungsverfahren fuer Textiloberflaechen.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/1996 - Schulz-Mirbach - Ein Referenzdatensatz zur Evaluierung von Sichtpruefungsverfahren fuer Textiloberflaechen.md"
extracted_text: "paper-inbox/90_processing/text/1996 - Schulz-Mirbach - Ein Referenzdatensatz zur Evaluierung von Sichtpruefungsverfahren fuer Textiloberflaechen.txt"
artifact_status: "German internal report; dataset reference documentation"
tags:
  - paper
---
# TILDA Reference Dataset Report

## Summary

This German internal report documents the structure of [[TILDA]], a reference dataset for evaluating visual inspection algorithms for textile surface defects. It describes the dataset's fabric classes, defect categories, image and text-file formats, directory layout, and naming convention.

Translated title: "A reference dataset for evaluating visual inspection methods for textile surfaces."

## Paper Type

- Type: other.
- Why: This is a German internal report and dataset documentation, not a conventional peer-reviewed research paper.

## Dataset Description

- Dataset: [[TILDA]].
- Purpose: evaluate algorithms for detecting fabric surface defects.
- Image type: monochrome grayscale images with 256 gray levels.
- Image format: TIFF.
- Resolution: 768 x 512 pixels.
- Reported size: 3,228 images, 2,828 text files with defect descriptions, and 1.27 GB.
- Additional material: 20 images from a commercially available catalog of fabric defects are included to help compare the dataset's defect classes with textile-industry standards.
- Defect descriptions: each defect image has an accompanying text file with a short description of the defect's location and size.

## Textile Classes

- Class 1: fabrics with very fine or no visible internal structure, such as unprinted viscose or silk.
- Class 2: fabrics with low-variance stochastic structure and no print, such as wool or jute.
- Class 3: fabrics with clearly visible periodic structure, such as printed diamond patterns or curtains.
- Class 4: printed fabrics without recognizable periodicity, such as viscose with flower prints of different sizes.

## Defect Classes

- e0: no fabric defect.
- e1: holes and cuts caused by mechanical damage.
- e2: oil stains and color defects.
- e3: thread defects, thread compactions, and missing individual threads.
- e4: foreign bodies on the fabric.
- e5: folds without mechanical damage.
- e6: changed illumination conditions.
- e7: affine distortions caused by camera tilt and changed camera distance from the test object.

## File Structure

- Image files follow `CREN.TIF`.
- `C`: fabric class number, 1 through 4.
- `R`: class representative number, 1 through 3; the report states that two representatives per class are present and directories for three representatives were prepared for possible expansion.
- `E`: defect class number, 0 through 7.
- `N`: image number, 1 through 50.
- Text files use the same naming convention with `.TXT`.

## Performance Metrics

- Not applicable. The report documents a reference dataset structure and does not report model scores, benchmark results, or evaluation metrics.

## Citation

Citation key: `schulz1996tilda`

```bibtex
@article{schulz1996tilda,
  title={Tilda-ein referenzdatensatz zur evaluierung von sichtpr{\"u}fungsverfahren f{\"u}r textiloberfl{\"a}chen},
  author={Schulz-Mirbach, H},
  journal={Interner Bericht},
  volume={4},
  pages={96},
  year={1996}
}
```

## Connections

### Graph Hubs

- Datasets: [[TILDA]]
- Tasks: [[Textile defect detection]]
- Domains: [[Textile and fiber inspection]]
- Methods: [[Reference dataset construction]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2025 - Artificial Intelligence Driving Innovation in Textile Defect Detection]] | Follow-up reading | The review lists TILDA among textile defect datasets and gives a compact sample/class summary. |
| [[2021 - Fabric Defect Detection in Textile Manufacturing A Survey of the State of the Art]] | Follow-up reading | The fabric defect detection survey mentions TILDA in its dataset and method tables. |

## Questions

- The host page reports 3,200 images, while the German report reports 3,228 images including additional catalog images; downstream comparisons should state which count they use.
- The license and redistribution terms are not reported on the host page or in the reference report.
