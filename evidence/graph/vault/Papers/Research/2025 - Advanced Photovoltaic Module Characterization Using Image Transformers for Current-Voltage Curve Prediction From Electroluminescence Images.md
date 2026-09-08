---
title: "Advanced Photovoltaic Module Characterization: Using Image Transformers for Current-Voltage Curve Prediction From Electroluminescence Images"
aliases:
  - "Advanced Photovoltaic Module Characterization"
paper_key: "doi:10.1109/jphotov.2025.3562931"
doi: "10.1109/JPHOTOV.2025.3562931"
url: "https://doi.org/10.1109/JPHOTOV.2025.3562931"
authors:
  - "Brandon K. Byford"
  - "Laura E. Boucheron"
  - "Bruce H. King"
  - "Jennifer L. Braid"
year: 2025
venue: "IEEE Journal of Photovoltaics"
paper_type: "research"
status: "processed"
topics:
  - "photovoltaic module characterization"
  - "electroluminescence imaging"
  - "current-voltage curve prediction"
tasks:
  - "[[PV module current-voltage curve prediction]]"
domains:
  - "[[Solar cells and photovoltaic]]"
datasets:
  - "[[PV-IV-EL]]"
methods:
  - "[[Swin Transformer]]"
  - "[[Data augmentation]]"
model_family:
  - "[[Vision Transformer]]"
architectures:
  - "[[Swin Transformer]]"
training_regime:
  - "[[Transfer learning]]"
metrics:
  - "[[Mean Absolute Error]]"
  - "[[Mean Squared Error]]"
  - "[[Maximum power point]]"
  - "[[Short-circuit current]]"
  - "[[Open-circuit voltage]]"
primary_metric: "[[Mean Absolute Error]]"
baselines: "not reported"
benchmarks: "not reported"
code: "not reported"
data: "[[PV-IV-EL]]"
licenses: "CC BY 4.0"
related_papers: []
related_concepts:
  - "[[Solar cells and photovoltaic]]"
related_methods:
  - "[[Swin Transformer]]"
  - "[[Data augmentation]]"
related_datasets:
  - "[[PV-IV-EL]]"
related_domains:
  - "[[Solar cells and photovoltaic]]"
related_tasks:
  - "[[PV module current-voltage curve prediction]]"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2025 - Byford - Advanced Photovoltaic Module Characterization Using Image Transformers for Current-Voltage Curve Prediction From Electroluminescenc....md"
extracted_text: "paper-inbox/90_processing/text/2025 - Byford - Advanced Photovoltaic Module Characterization Using Image Transformers for Current-Voltage Curve Prediction From Electroluminescenc....txt"
source_file: "paper-inbox/10_processed/Research/2025 - Byford - Advanced Photovoltaic Module Characterization Using Image Transformers for Current-Voltage Curve Prediction From Electroluminescenc....pdf"
processed_at: "2026-06-04"
---
# Advanced Photovoltaic Module Characterization: Using Image Transformers for Current-Voltage Curve Prediction From Electroluminescence Images

## Summary

The paper trains a Swin transformer model to predict normalized photovoltaic module I-V curves from electroluminescence images. On a selected [[PV-IV-EL]] subset, predicted curves recover maximum power point, short-circuit current, and open-circuit voltage with mean errors below 1%, while some fitted single-diode parameters remain poorly predicted.

## Paper Type

Research paper. The contribution is a deep learning method and evaluation for [[PV module current-voltage curve prediction]], using a public paired EL-image and I-V-curve dataset rather than introducing only a dataset or benchmark protocol.

## Problem

Direct I-V curve measurement is more disruptive than EL imaging, and field PV inspection needs ways to estimate electrical performance from image evidence. The paper targets module-level characterization from a single EL image, with the explicit caveat that predicted normalized curves should not be interpreted as true flash-test I-V curves.

## Contribution

- Introduces a single Swin-transformer-based network that predicts a 400-point normalized I-V curve from one EL image.
- Uses paired EL images and I-V curves from [[PV-IV-EL]], selecting 612 samples from mono- and multicrystalline silicon modules and standard-test-condition measurements.
- Shows that MPP, Isc, and Voc can be predicted with mean errors below 1% on the paper's dataset, while shunt resistance and dark current remain unreliable.
- Tests high-bias versus low-bias EL inputs and finds similar prediction accuracy.

## Method

The model has three parts: an image preprocessing layer, a SwinV2-B transformer feature extractor, and a dense sigmoid output layer that produces a length-400 normalized I-V curve. The transformer is initialized with pretrained weights, the output layer is trained first while transformer weights are frozen, and then all weights are unfrozen for fine-tuning.

The EL preprocessing pipeline orients modules horizontally, crops to the module area, downsamples 4k x 8k images to 320 x 512 pixels, and converts TIFF images to JPG. Training data are expanded through horizontal, vertical, and combined flips; the paper chooses flipping because module orientation should not change the I-V curve, while intensity and noise augmentations would have physical interpretations that could affect electrical behavior.

The I-V curves are normalized to each module's first measured curve, clipped between 0 V and Voc, smoothed with a Savitzky-Golay filter, and downsampled to 400 samples. Curves outside the target [0, 1] range are renormalized to themselves because the sigmoid output layer is constrained to that range.

## Evidence

### Dataset and split

- Dataset source: [[PV-IV-EL]] from Sandia's Photovoltaic Systems Evaluation Laboratory.
- Paper subset: 612 paired EL-image and I-V-curve samples from 439 unique modules, covering 28 module models and 17 brands.
- Split: 90% training, 5% validation, and 5% testing, yielding 549, 31, and 31 samples before flip augmentation.
- Each EL image is paired with an I-V curve from the same module within 30 days.
- The paper reports all selected curves have high fill factors above 75%, indicating no severely degraded modules in the selected subset.

### Training and losses

- Optimizer: AdamW.
- Learning rate: 0.0001.
- Training stage 1: freeze transformer weights, train output layer with patience 40 and tolerance 0.0001.
- Training stage 2: unfreeze all weights and train with patience 100 and tolerance 0.0001.
- Losses compared: MSE, MAE, weighted MSE, and weighted MAE.
- Weighted losses emphasize curve samples 0-9 for Isc, 300-349 for MPP, and 350-399 for Voc and series resistance.

### Results

- Predicted curves recover MPP, Isc, and Voc with mean errors below 1%.
- Series resistance extracted from predicted curves has mean error 5.19%.
- Photocurrent extracted from predicted curves has mean error 0.197%.
- Shunt resistance and dark current have large errors and large variance.
- Tenfold analysis finds MAE, MPP, Isc, Voc, photocurrent, series resistance, and the paper's `N` parameter have reasonable error with low standard deviation; shunt resistance and dark current remain unreliable.
- Reduced-training experiments show MPP and Isc remain within 1% error even with smaller training fractions, but curve smoothness and some derived parameters improve as training data increases.
- Testing on an external dataset from Hoffman et al. yields 13.9% mean MPP error, which the authors attribute to a domain mismatch: the external data emphasize cracking from stress, while the training data emphasize outdoor exposure and contain no heavily damaged modules with strongly affected I-V curves.

## ML/DL Extraction

- Task formulation: regression from a single EL image to a 400-point normalized I-V curve.
- Input: high-bias EL image by default; low-bias EL images are tested separately.
- Output: length-400 normalized I-V curve.
- Architecture: SwinV2-B transformer backbone plus one dense sigmoid output layer.
- Loss/objective: MAE, MSE, weighted MAE, and weighted MSE variants.
- Data augmentation: horizontal, vertical, and combined flips.
- Pretraining: transformer initialized from pretrained weights.
- Evaluation protocol: held-out random split, tenfold analysis, reduced training-set-size experiments, and external-dataset test.
- Compute/hardware: not reported.
- Code: not reported.
- Data availability: [[PV-IV-EL]] is publicly hosted by Open Energy Data Initiative.

## Limitations

- Predicted normalized I-V curves are not direct replacements for true flash-test I-V curves.
- The dataset lacks severely degraded modules, and the model performs poorly on an external stress-cracked module dataset.
- Degradation or damage modes that affect I-V behavior but are not visible in EL, such as back-sheet cracking and delamination, are outside the model's evidence.
- The model is limited to silicon-based modules with series architectures; butterfly or shingle architectures are not represented in training.
- Shunt resistance and dark current are not reliably predicted from the learned curves.
- Weighted-loss coefficients are heuristic and may need tuning for applications that prioritize different I-V regions.

## Connections

### Graph Hubs

- Tasks: [[PV module current-voltage curve prediction]]
- Methods: [[Swin Transformer]], [[Data augmentation]], [[Transfer learning]]
- Datasets: [[PV-IV-EL]]
- Domains: [[Solar cells and photovoltaic]]
- Metrics: [[Mean Absolute Error]], [[Mean Squared Error]], [[Maximum power point]], [[Short-circuit current]], [[Open-circuit voltage]]

### Shares dataset

- [[PV-IV-EL]] - the paper trains and evaluates on paired EL images and I-V curves from this public dataset.

### Shares task

- [[PV module current-voltage curve prediction]] - the paper predicts module I-V curves and derived electrical parameters from EL images.

### Shares method

- [[Swin Transformer]] - SwinV2-B is the central image feature extractor.
- [[Vision Transformer]] - the method belongs to the vision-transformer family.
- [[Transfer learning]] - the transformer is initialized with pretrained weights and fine-tuned for the PV task.
- [[Data augmentation]] - the training set is expanded using physically motivated image flips.

### Shares metric

- [[Mean Absolute Error]] and [[Mean Squared Error]] - used as loss functions and curve-level fit metrics.
- [[Maximum power point]], [[Short-circuit current]], and [[Open-circuit voltage]] - derived from predicted curves and reported with mean errors below 1%.

### Application/domain

- [[Solar cells and photovoltaic]] - the work targets photovoltaic module inspection and electrical characterization.

## Questions

- Would adding modules with severe cracking, delamination, or back-sheet degradation improve external generalization?
- Would physics-guided losses or constraints improve shunt resistance and dark-current prediction?
- Would using both high- and low-bias EL images, or a derived series-resistance map, provide enough information to improve difficult I-V parameters?
