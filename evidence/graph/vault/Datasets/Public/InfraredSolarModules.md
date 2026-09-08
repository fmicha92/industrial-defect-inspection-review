---
title: "InfraredSolarModules"
aliases:
  - "Infrared Solar Modules"
  - "Infrared Solar Module Dataset"
  - "InfraredSolarModules dataset"
related_domain: "[[Solar cells and photovoltaic]]"
url: "https://github.com/RaptorMaps/InfraredSolarModules"
data_sources:
  - "GitHub"
  - "Raptor Maps"
licenses: "MIT License"
introduced_by: "[[2020 - Infrared Solar Module Dataset for Anomaly Detection]]"
related_tasks:
  - "[[Solar module anomaly classification]]"
related_methods:
  - "[[Infrared thermography]]"
---
# InfraredSolarModules

## Definition

InfraredSolarModules is a public dataset of infrared solar-module imagery labeled for anomaly classification across solar farms.

## Why It Matters

The dataset provides public thermal imagery for [[Solar module anomaly classification]], a setting where remote solar inspections typically require expert review and public machine-learning data are scarce.

## Dataset Details

- Domain: [[Solar cells and photovoltaic]].
- Task: [[Solar module anomaly classification]].
- Modality: infrared images of solar modules.
- Total images: 20,000.
- Image size: 24 x 40 pixels.
- Classes: 12 total classes, with 11 anomaly classes and one `No-Anomaly` class.
- Paper-reported dataset size: 81.9 MB.
- Repository ZIP: `2020-02-14_InfraredSolarModules.zip`, reported by the GitHub API as 15,495,990 bytes.
- Repository package: the ZIP contains an `images` directory and `module_metadata.json`.
- Metadata schema: each image record includes `image_filepath` and `anomaly_class`.
- Collection: Raptor Maps aggregated real-world solar-module data collected by piloted aircraft and unmanned aerial systems.
- Sensors: midwave or longwave infrared systems, 3-13.5 micrometers, plus visible-spectrum imaging systems used during classification.
- Ground sample distance: 3.0 to 15.0 cm/pixel.
- Annotation process: anomalies were cropped to individual modules and separated into classes; corresponding visible-spectrum images were used during classification to improve accuracy.
- License: MIT License.

## Class Distribution

| Class | Images | Description |
|---|---:|---|
| Cell | 1,877 | Hot spot with square geometry in a single cell. |
| Cell-Multi | 1,288 | Hot spots with square geometry in multiple cells. |
| Cracking | 941 | Module anomaly caused by cracking on the module surface. |
| Hot-Spot | 251 | Hot spot on a thin-film module. |
| Hot-Spot-Multi | 247 | Multiple hot spots on a thin-film module. |
| Shadowing | 1,056 | Sunlight obstructed by vegetation, structures, or adjacent rows. |
| Diode | 1,499 | Activated bypass diode, typically affecting one third of a module. |
| Diode-Multi | 175 | Multiple activated bypass diodes, typically affecting two thirds of a module. |
| Vegetation | 1,639 | Panels blocked by vegetation. |
| Soiling | 205 | Dirt, dust, or other debris on the module surface. |
| Offline-Module | 828 | Entire module is heated. |
| No-Anomaly | 10,000 | Nominal solar module. |

## Source Anchors

- Hosting source: [GitHub repository](https://github.com/RaptorMaps/InfraredSolarModules).
- Download: [2020-02-14_InfraredSolarModules.zip](https://raw.githubusercontent.com/RaptorMaps/InfraredSolarModules/master/2020-02-14_InfraredSolarModules.zip).
- Introducing paper: [[2020 - Infrared Solar Module Dataset for Anomaly Detection]].

## Used In These Papers

- [[2020 - Infrared Solar Module Dataset for Anomaly Detection]] introduces the dataset and class distribution for solar-module anomaly classification research.

## Related Concepts

- [[Solar cells and photovoltaic]]
- [[Solar module anomaly classification]]
- [[Infrared thermography]]
- [[Class imbalance]]
