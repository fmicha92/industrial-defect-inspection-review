---
title: "A-SEE-Q"
aliases:
  - "Augmented SEE-Q"
availability: "reported public in 2021 paper; current GitHub repository unavailable as of 2026-06-06"
status: stable
concept_type: dataset
related_domain: "[[Automotive manufacturing]]"
url: "https://github.com/RicardoSPeres/simulation-synth-adhesive"
repository_url: "https://github.com/RicardoSPeres/simulation-synth-adhesive"
supplemental_results_url: "https://ricardosperes.github.io/simulation-synth-adhesive/"
related_gan_dataset: "[[Structural Adhesive Defects Dataset]]"
related_gan_dataset_repository: "https://github.com/RicardoSPeres/GAN_Synth_Adhesive"
related_gan_dataset_release: "https://github.com/RicardoSPeres/GAN_Synth_Adhesive/releases/tag/v1.0"
data_sources:
  - "GitHub repository reported by paper"
  - "GitHub Pages supplemental results site"
  - "Related GAN structural adhesive dataset release"
host_status: "repository returns 404; supplemental results page returns 200"
host_verified_at: 2026-06-06
introduced_by: "[[2021 - Simulation-Based Data Augmentation for Quality Inspection of Structural Adhesive]]"
---
# A-SEE-Q

## Definition

A-SEE-Q is the simulation-augmented adhesive bead defect dataset used in [[2021 - Simulation-Based Data Augmentation for Quality Inspection of Structural Adhesive]]. It contains 4000 synthetic images generated in CoppeliaSim with automatically generated YOLO-format bounding-box annotations. The paper reports the associated artifacts as public, but the recorded GitHub repository was unavailable during the 2026-06-06 host audit.

## Why It Matters

It supports experiments on whether simulation-generated defect images can improve object detection when real structural adhesive defect images are scarce.

## Dataset Details

- Source process: structural adhesive bead application in an automotive production-cell setting.
- Synthetic image count: 4000.
- Defect classes: discontinuity and excess adhesive.
- Annotation format: YOLO bounding boxes with object class, center coordinates, width, and height.
- Generation: simulation can produce up to three defects per part and computes defect location and length along the bead path.
- Availability: the paper reports data, simulation, model configurations, and weights as publicly available at https://github.com/RicardoSPeres/simulation-synth-adhesive.
- Current host status: the GitHub repository URL returned 404 through both the web endpoint and GitHub API on 2026-06-06.
- Supplemental source: https://ricardosperes.github.io/simulation-synth-adhesive/ remains accessible and shows project results and examples, but it does not expose a dataset download in the parsed page.
- Related public dataset: [[Structural Adhesive Defects Dataset]] provides structural-adhesive dataset assets including `adhesive1024.zip`, `obj.zip`, `test.zip`, and `holdout.zip`. This is related to the same adhesive-inspection research line but is not treated as the canonical A-SEE-Q host because the release belongs to the GAN augmentation paper and its split descriptions differ from A-SEE-Q's 4000 CoppeliaSim-image description.

## Used In These Papers

- [[2021 - Simulation-Based Data Augmentation for Quality Inspection of Structural Adhesive]] uses A-SEE-Q for synthetic-only and real-plus-synthetic object detection experiments.

## Source Anchors

- Reported dataset repository: https://github.com/RicardoSPeres/simulation-synth-adhesive.
- Current repository status: unavailable / 404 as of 2026-06-06.
- Supplemental results page: https://ricardosperes.github.io/simulation-synth-adhesive/.
- Related GAN repository: https://github.com/RicardoSPeres/GAN_Synth_Adhesive.
- Related GAN dataset release: https://github.com/RicardoSPeres/GAN_Synth_Adhesive/releases/tag/v1.0.
- Related public dataset note: [[Structural Adhesive Defects Dataset]].
- Introducing paper: [[2021 - Simulation-Based Data Augmentation for Quality Inspection of Structural Adhesive]].

## Related Concepts

- [[Adhesive bead defect detection]]
- [[Simulation-based data augmentation]]
- [[Automotive manufacturing]]
