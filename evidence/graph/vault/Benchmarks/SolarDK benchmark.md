---
title: "SolarDK benchmark"
aliases:
  - "SolarDK classification benchmark"
  - "SolarDK segmentation benchmark"
introduced_by: "[[2022 - SolarDK A high-resolution urban solar panel image classification and localization dataset]]"
datasets:
  - "[[SolarDK]]"
tasks:
  - "[[Solar panel classification]]"
  - "[[Solar panel localization]]"
metrics:
  - "[[Precision]]"
  - "[[Recall]]"
  - "[[Cohen's kappa]]"
  - "[[mIoU]]"
---
# SolarDK Benchmark

## Definition

SolarDK benchmark evaluates solar-panel classification and localization from Danish aerial imagery using the [[SolarDK]] train, validation, and test split.

## Protocol

- Classification uses Gentofte training and validation images and Herlev test images.
- Segmentation/localization uses masks for the positive manually labelled instances.
- BBR positive examples are used in one classification scenario to augment the minority class during training.
- Classification metrics: [[Precision]], [[Recall]], and [[Cohen's kappa]].
- Segmentation metrics: [[Precision]], [[Recall]], and [[mIoU]].

## Reported Baselines

- Classification baselines include ConvNeXt, EfficientNet-b5/b7, InceptionV3, ResNet50/101/152, DeepSolarDE inference, and DeepSolarDK.
- Segmentation baselines include ResNet-backed DeepLabV3+, FPN, PSPNet, DeepSolarDE inference, and DeepSolarDK.
- The paper reports DeepSolarDK test performance of 0.73 recall, 0.65 precision, and 0.67 Cohen's kappa for classification.
- The best reported out-of-domain segmentation baselines reach about 0.72 IoU, while DeepSolarDK reports 0.62 IoU after fine-tuning from German solar-panel data.

## Used In These Papers

- [[2022 - SolarDK A high-resolution urban solar panel image classification and localization dataset]] introduces the benchmark and reports baseline classification and segmentation results.

## Related Concepts

- [[SolarDK]]
- [[Solar panel classification]]
- [[Solar panel localization]]
- [[Urban semantic segmentation]]
