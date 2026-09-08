---
title: "SEE-Q"
aliases:
  []
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
# SEE-Q

## Definition

SEE-Q is a dataset of 124 manually annotated real industrial structural adhesive bead images introduced by [[2021 - Simulation-Based Data Augmentation for Quality Inspection of Structural Adhesive]]. The paper reports the dataset as publicly available, but the recorded GitHub repository was unavailable during the 2026-06-06 host audit.

## Why It Matters

It is the real-data anchor for simulation-based augmentation in adhesive quality inspection.

## Dataset Details

- Image count: 124 real adhesive bead images.
- Defect instances: 160 discontinuity instances and 70 excess-defect instances.
- Annotation: manual bounding-box annotations for object detection.
- Availability: the paper reports data, simulation, model configurations, and weights as publicly available at https://github.com/RicardoSPeres/simulation-synth-adhesive.
- Current host status: the GitHub repository URL returned 404 through both the web endpoint and GitHub API on 2026-06-06.
- Supplemental source: https://ricardosperes.github.io/simulation-synth-adhesive/ remains accessible and shows project results, synthetic/real/augmented examples, and the 0.9173 mAP@0.50 augmented-test result, but it does not expose a dataset download in the parsed page.
- Related public dataset: [[Structural Adhesive Defects Dataset]] provides structural-adhesive dataset assets including `adhesive1024.zip` with 143 real 1024 x 1024 images, plus `obj.zip`, `test.zip`, and `holdout.zip` for object detection. This is related evidence from the same structural-adhesive inspection line of work, but it is not treated as the canonical SEE-Q host because its paper/release description and image counts differ from SEE-Q's 124-image description.

## Used In These Papers

- [[2021 - Simulation-Based Data Augmentation for Quality Inspection of Structural Adhesive]] uses this dataset as reported in the processed paper note.
## Source Anchors

- Reported dataset repository: https://github.com/RicardoSPeres/simulation-synth-adhesive.
- Current repository status: unavailable / 404 as of 2026-06-06.
- Supplemental results page: https://ricardosperes.github.io/simulation-synth-adhesive/.
- Related GAN repository: https://github.com/RicardoSPeres/GAN_Synth_Adhesive.
- Related GAN dataset release: https://github.com/RicardoSPeres/GAN_Synth_Adhesive/releases/tag/v1.0.
- Related public dataset note: [[Structural Adhesive Defects Dataset]].
- Introducing paper: [[2021 - Simulation-Based Data Augmentation for Quality Inspection of Structural Adhesive]].

## Related Concepts

- [[Surface defect detection]]
- [[Adhesive bead defect detection]]
- [[Simulation-based data augmentation]]
- [[Automotive manufacturing]]
