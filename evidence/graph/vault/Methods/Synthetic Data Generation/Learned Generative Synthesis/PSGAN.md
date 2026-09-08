---
title: "PSGAN"
aliases:
  - "Periodic spatial GAN"
  - "Periodic spatial generative adversarial network"
tags:
  - method
---

# PSGAN

## Definition

PSGAN is a periodic spatial generative adversarial network used to synthesize periodic texture patches. In the CycleGAN defect-segmentation paper, it is based on DCGAN and modifies the GAN loss for periodic texture generation.

## Why It Matters

Periodic-texture inspection can lack defect-free training images. PSGAN supports synthetic non-defect image generation from defect-removed periodic textures, giving the golden-template generator a non-defect domain to learn from.

## Used In These Papers

- [[2020 - Weakly-Supervised Defect Segmentation on Periodic Textures Using CycleGAN]] uses PSGAN after PatchMatch defect removal to generate synthetic non-defect images for weakly supervised periodic-texture defect segmentation.

## Related Concepts

- [[DCGAN]]
- [[CycleGAN]]
- [[Learned generative synthesis]]
- [[Synthetic data generation]]
- [[PatchMatch]]
