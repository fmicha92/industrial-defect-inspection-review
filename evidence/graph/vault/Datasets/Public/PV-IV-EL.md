---
title: "PV-IV-EL"
aliases:
  - "Photovoltaic Module Current-Voltage and Electroluminescence Image Data"
  - "Photovoltaic Module Current-Voltage and Electroluminescence Image Data (PV-IV-EL)"
related_domain: "[[Solar cells and photovoltaic]]"
url: "https://data.openei.org/submissions/8378"
data_sources:
  - "Open Energy Data Initiative"
  - "Sandia National Laboratories"
licenses: "CC BY 4.0"
introduced_by: "[[2025 - Advanced Photovoltaic Module Characterization Using Image Transformers for Current-Voltage Curve Prediction From Electroluminescence Images]]"
related_tasks:
  - "[[PV module current-voltage curve prediction]]"
---
# PV-IV-EL

## Definition

PV-IV-EL is a public photovoltaic module dataset pairing current-voltage flash-test traces with electroluminescence images for commercial PV modules measured by Sandia National Laboratories' Photovoltaic Systems Evaluation Laboratory.

## Why It Matters

PV-IV-EL supports methods that connect visual electroluminescence evidence to module-level electrical behavior. It provides paired image and I-V measurements needed for [[PV module current-voltage curve prediction]] and broader [[Solar cells and photovoltaic]] module characterization.

## Dataset Details

- Domain: [[Solar cells and photovoltaic]].
- Task: [[PV module current-voltage curve prediction]].
- Modality: current-voltage flash-test data and electroluminescence images.
- Host-reported size: 613 corresponding IV/EL sets.
- Host-reported modules: 438 unique modules, 28 unique module models, and 17 brands.
- Paper subset: [[2025 - Advanced Photovoltaic Module Characterization Using Image Transformers for Current-Voltage Curve Prediction From Electroluminescence Images]] uses 612 paired EL-image and I-V-curve samples from 439 unique modules after selecting mono- and multicrystalline silicon modules and standard-test-condition measurements.
- Collection site: Sandia National Laboratories Photovoltaic Systems Evaluation Laboratory, with modules from fielded systems in Albuquerque, New Mexico, USA.
- Exposure coverage: modules were removed from the field and measured in the lab after 0 to 5 years of outdoor exposure.
- Metadata: `AnonDB.csv` records anonymized module metadata, IV acquisition metadata, EL acquisition metadata, and outdoor exposure length.
- IV acquisition: IV traces are reported as forward-direction flash-test measurements from short circuit to open circuit at standard test conditions with an AAA-rated flash tester.
- EL acquisition: high- and low-current-injection EL images are reported at approximately 80% and 20% of module short-circuit current.
- Files: `AnonDB.csv`, `IV.zip`, `EL.zip`, `RefIV.zip`, and `AnonDB_descriptions.xlsx`.
- Total hosted download size: 16.69 GB.
- License: CC BY 4.0.

## Source Anchors

- Hosting source: [Open Energy Data Initiative submission 8378](https://data.openei.org/submissions/8378).
- Introducing paper: [[2025 - Advanced Photovoltaic Module Characterization Using Image Transformers for Current-Voltage Curve Prediction From Electroluminescence Images]].
- Dataset citation key: `OEDI_Dataset_8378`.

## Used In These Papers

- [[2025 - Advanced Photovoltaic Module Characterization Using Image Transformers for Current-Voltage Curve Prediction From Electroluminescence Images]] trains and evaluates a Swin transformer on paired EL images and normalized I-V curves from PV-IV-EL.

## Related Concepts

- [[Solar cells and photovoltaic]]
- [[PV module current-voltage curve prediction]]
- [[Open-circuit voltage]]
- [[Short-circuit current]]
- [[Maximum power point]]
