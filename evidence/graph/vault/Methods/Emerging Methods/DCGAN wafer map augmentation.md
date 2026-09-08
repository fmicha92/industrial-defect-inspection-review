---
title: "DCGAN wafer map augmentation"
aliases:
  - "DCGAN wafer map augmentation"
status: emerging
concept_type: method
candidate_parent: "Methods/Synthetic Data Generation"
source_papers:
  - "[[2023 - Deep Convolutional GAN-Based Data Augmentation for Class-Imbalanced Wafer Bin Map Defect Patterns]]"
  - "[[2022 - WaferCaps for Wafer Bin Map Classification Based on DCGAN Data Upsampling]]"
  - "[[2020 - Using GAN to Improve CNN Performance of Wafer Map Defect Type Classification]]"
  - "[[2025 - Wafer Map Defect Classification Using Deep Learning Framework with Data Augmentation on Imbalance Datasets]]"
evidence_count: 4
tags:
  - emerging-method
---
# DCGAN wafer map augmentation

## Definition

DCGAN wafer map augmentation is a wafer bin map data augmentation method that trains DCGAN generators on selected [[WM-811K]] defect patterns, refines generated maps with a masking process, and uses them to train a CNN classifier under class imbalance.

## Why It Matters

It captures a reusable technical approach for handling scarce, imbalanced, or hard-to-label wafer-map defect data in semiconductor manufacturing.

## Used In These Papers


- [[2023 - Deep Convolutional GAN-Based Data Augmentation for Class-Imbalanced Wafer Bin Map Defect Patterns]] uses [[DCGAN wafer map augmentation]] for wafer bin map classification, DCGAN augmentation.
- [[2022 - WaferCaps for Wafer Bin Map Classification Based on DCGAN Data Upsampling]] uses DCGAN data upsampling to increase each WM-811K defect class to about 10,000 samples and improves WaferCaps test accuracy from 78.2% to 91.41%.
- [[2020 - Using GAN to Improve CNN Performance of Wafer Map Defect Type Classification]] uses GAN-generated wafer maps for low-data WM-811K classes and improves CNN accuracy from 97.0% to 98.3%.
- [[2025 - Wafer Map Defect Classification Using Deep Learning Framework with Data Augmentation on Imbalance Datasets]] modifies DCGAN-style wafer-map generation into [[G2LGAN]], using all-class pretraining and class-specific fine-tuning for imbalanced wafer maps.

## Related Concepts

- [[Synthetic data generation]]
- [[Data augmentation]]
- [[Industrial anomaly detection]]
- [[G2LGAN]]
