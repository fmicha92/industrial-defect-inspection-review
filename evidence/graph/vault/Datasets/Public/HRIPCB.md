---
title: "HRIPCB"
aliases:
  - "PKU-Market-PCB"
  - "PKU-PCB"
  - "Peking University PCB dataset"
  - "Printed circuit board (PCB) defect dataset"
  - "A PCB Dataset for Defects Detection and Classification dataset"
related_domain: "[[Semiconductor and electronics]]"
url: "https://robotics.pkusz.edu.cn/resources/datasetENG/"
data_sources: "HRI Lab PKU-Market dataset page"
introduced_by: "[[2020 - HRIPCB a Challenging Dataset for PCB Defects Detection and Classification]]"
related_papers:
  - "[[2020 - HRIPCB a Challenging Dataset for PCB Defects Detection and Classification]]"
  - "[[2022 - Semi-Supervised Defect Detection Method with Data-Expanding Strategy for PCB Quality Inspection]]"
---
# HRIPCB

## Definition

HRIPCB is a synthesized naked-PCB defect dataset with 1,386 images and six defect kinds, proposed for detection, classification, and registration tasks.

## Dataset Details

- Hosting source: [HRI Lab PKU-Market dataset page](https://robotics.pkusz.edu.cn/resources/datasetENG/).
- Host listing name: `Printed circuit board (PCB) defect dataset`; later papers also refer to this dataset as `PKU-Market-PCB` or `PKU-PCB`.
- Contact listed on host page: Dai Linhui, `ddailinhui@pku.edu.cn`.
- Access link: the host page provides a Baidu download link.
- Availability: public.
- Size: 1,386 images.
- Defect classes: missing hole, mouse bite, open circuit, short circuit, spur, and spurious copper.
- Supported tasks: image detection, classification, and registration.
- License: not reported.

## Why It Matters

The dataset provides template images, PCB defect annotations, rotated images, and Python access support for PCB inspection experiments.

## Used In These Papers

- [[2020 - HRIPCB a Challenging Dataset for PCB Defects Detection and Classification]] introduces HRIPCB and evaluates an RBCNN approach on it.
- [[2022 - Semi-Supervised Defect Detection Method with Data-Expanding Strategy for PCB Quality Inspection]] refers to this dataset as PKU-PCB and processes it into auxiliary negative samples for DeepPCB data expansion.

## Source Anchors

- Hosting source: [HRI Lab PKU-Market dataset page](https://robotics.pkusz.edu.cn/resources/datasetENG/).
- Introducing paper: [[2020 - HRIPCB a Challenging Dataset for PCB Defects Detection and Classification]].
- Aliases used in later papers: `PKU-PCB`, `PKU-Market-PCB`.

## Related Concepts

- [[PCB defect detection]]
- [[PCB defect classification]]
- [[Semiconductor and electronics]]
