---
title: "Autoencoder-decoder data augmentation"
tags:
  - method
  - data-augmentation
---

# Autoencoder-Decoder Data Augmentation

## Definition

Autoencoder-decoder data augmentation generates additional training examples by reconstructing or modifying input images through an encoder-decoder model.

## Why It Matters

It appears in the wafer-map paper as a way to balance sparse defect classes while filtering generated images by similarity to avoid overfitting or unrecognizable patterns.

## Used In These Papers


- [[2024 - Wafer Map Defect Classification Using Autoencoder-Based Data Augmentation and Convolutional Neural Network]] adds Gaussian noise in an autoencoder latent space to augment each [[WM-811K]] defect class to 10,000 samples before CNN classification.
- [[2020 - A Light-Weight Neural Network for Wafer Map Classification Based on Data Augmentation]] uses CNN encoder-decoder augmentation for WM-811K and a 21-defect wafer-map dataset.
- [[2023 - Wafer Map Defect Patterns Classification Based on a Lightweight Network and Data Augmentation]] uses a convolutional autoencoder with Gaussian noise in the latent feature map to augment minority [[WM-811K]] wafer-map classes.

## Related Concepts

- [[Data augmentation]]
- [[Wafer map defect classification]]
