---
title: "RSW gun fault prediction benchmark dataset"
aliases:
  - "RSW gun fault prediction benchmark data set"
  - "Resistance spot welding gun fault prediction benchmark dataset"
  - "Welding gun fault prediction benchmark dataset"
related_domain: "[[Automotive manufacturing]]"
url: "https://zenodo.org/records/7655193"
doi: "10.5281/zenodo.7655193"
data_sources:
  - "Zenodo"
  - "BMW Brilliance Automotive body shop"
licenses:
  - "CC-BY-4.0"
version: "0.0.1"
access: "open"
modalities:
  - "multivariate time series"
tasks:
  - "[[Welding gun fault prediction]]"
related_concepts:
  - "[[Smart manufacturing]]"
related_papers:
  - "[[2024 - Benchmark for Welding Gun Fault Prediction with Multivariate Time Series Data]]"
introduced_by: "[[2024 - Benchmark for Welding Gun Fault Prediction with Multivariate Time Series Data]]"
---
# RSW Gun Fault Prediction Benchmark Dataset

## Definition

The RSW gun fault prediction benchmark dataset is an open multivariate time-series dataset for predicting faults in resistance spot welding guns used in automotive manufacturing.

## Why It Matters

Resistance spot welding guns are production-critical equipment in automotive body-shop assembly. The dataset supports machine-learning research on forecasting welding-gun parameters and anticipating equipment faults before they interrupt manufacturing lines.

## Dataset Details

- Dataset purpose: train and evaluate models for future welding-parameter prediction and welding-gun fault prediction.
- Hosting source: Zenodo.
- Creators: XiaoyeWang and changsheng Zhang, affiliated with NEU.
- Related paper authors: Xiaoye Wang, Changsheng Zhang, and Tao Wang.
- Collection context reported by the related paper: Body-Shop of BMW Brilliance Automotive Ltd.
- Modality: multivariate time series in CSV files.
- Training set: 72 multivariate time series.
- Test set: 8 multivariate time series.
- Sampling rate: 1 Hz.
- Time-series length: 604800 per series.
- Dimensions: 20 columns, including c1-c19 and an error code.
- Missing values and outliers are retained.
- Error code: included as one of the 20 dimensions.
- File structure: CSV files are grouped by error code and gun number, with demo files available for overview.
- Total hosted file size: 5.3 GB.
- Access: open Zenodo dataset record.
- License: CC-BY-4.0.
- Version: 0.0.1.

## Feature Fields

- c1: Electrode cap offset.
- c2: Electrode force.
- c3: Electrode position.
- c4: Force build-up.
- c5: Balance pressure.
- c6: Friction.
- c7: Maximum aperture.
- c8: Maximum electrode force.
- c9: Mtart friction.
- c10: US2.
- c11: Welding point count.
- c12: Position count.
- c13: Setpoints of counterbalance pressure.
- c14: Setpoints of electrode force.
- c15: Setpoints of electrode position.
- c16: Setpoints of sheet thickness.
- c17: Setpoints of velocity.
- c18: Setpoints of force build-up.
- c19: Offset value in robot.

## Source Anchors

- Zenodo record: [https://zenodo.org/records/7655193](https://zenodo.org/records/7655193)
- Dataset DOI: [10.5281/zenodo.7655193](https://doi.org/10.5281/zenodo.7655193)
- Benchmark code record: [https://zenodo.org/record/7655025](https://zenodo.org/record/7655025)
- Related paper: [[2024 - Benchmark for Welding Gun Fault Prediction with Multivariate Time Series Data]]
- Related paper DOI: [10.1038/s41597-024-02914-z](https://doi.org/10.1038/s41597-024-02914-z)

## Related Concepts

- [[Automotive manufacturing]]
- [[Welding gun fault prediction]]
- [[Smart manufacturing]]
- [[2024 - Benchmark for Welding Gun Fault Prediction with Multivariate Time Series Data]]

## Questions

- Are all five error-code definitions documented in the hosted dataset files or only in the related paper?
- Which benchmark metrics should be represented as dedicated metric notes after reading the full paper?
