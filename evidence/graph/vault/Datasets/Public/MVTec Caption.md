---
title: "MVTec Caption"
aliases:
  - "MVTec Caption"
related_domain: "[[Multi-industry anomaly detection]]"
url: "https://github.com/hujiecpp/MVTec-Caption"
data_sources:
  - "[[MVTec AD]]"
  - "[[MVTec LOCO AD]]"
introduced_by: "[[2024 - AnomalyXFusion Multi-modal Anomaly Synthesis with Diffusion]]"
related_papers:
  - "[[2024 - AnomalyXFusion Multi-modal Anomaly Synthesis with Diffusion]]"
availability: "public construction repository"
access: "GitHub repository provides construction scripts; captions are built from downloaded MVTec AD and MVTec LOCO AD datasets"
licenses:
  - "base MVTec datasets are CC BY-NC-SA 4.0"
  - "repository license not reported"
---
# MVTec Caption

## Definition

MVTec Caption is a multimodal annotation extension for [[MVTec AD]] and [[MVTec LOCO AD]]. It adds image-mask-text annotations and anomaly captions to support text-, mask-, and image-conditioned anomaly synthesis and anomaly understanding.

## Why It Matters

It supplies the semantic descriptions that ordinary image-level labels and masks do not capture, especially for logical anomalies where missing, misplaced, wrong-count, or wrong-color objects need textual context.

## Dataset Details

- Scope: caption annotations for MVTec AD and MVTec LOCO AD.
- Size: 2.2k image-mask-text annotations reported by the introducing paper.
- Caption counts: 1,258 captions for MVTec AD and 982 captions for MVTec LOCO AD.
- Components: MVTec AD Caption and LOCO Caption.
- Modalities: images, anomaly masks, and text descriptions.
- Construction: the GitHub repository instructs users to download MVTec AD and MVTec LOCO AD separately, then run scripts to build the captioned dataset structure.
- Availability: public construction repository at https://github.com/hujiecpp/MVTec-Caption.
- Access constraints: the underlying MVTec AD and MVTec LOCO AD datasets are governed by MVTec's CC BY-NC-SA 4.0 noncommercial terms; the repository license is not reported.

## Used In These Papers

- [[2024 - AnomalyXFusion Multi-modal Anomaly Synthesis with Diffusion]] introduces MVTec Caption as 1,258 MVTec AD captions plus 982 MVTec LOCO captions for text-, mask-, and texture-conditioned anomaly synthesis.

## Source Anchors

- Hosting source: https://github.com/hujiecpp/MVTec-Caption.
- Introducing paper: [[2024 - AnomalyXFusion Multi-modal Anomaly Synthesis with Diffusion]].
- Base datasets: [[MVTec AD]] and [[MVTec LOCO AD]].
- Access terms: public construction scripts; base datasets are CC BY-NC-SA 4.0, noncommercial.

## Related Concepts

- [[Multi-industry anomaly detection]]
- [[Industrial anomaly detection]]
- [[Surface defect detection]]
