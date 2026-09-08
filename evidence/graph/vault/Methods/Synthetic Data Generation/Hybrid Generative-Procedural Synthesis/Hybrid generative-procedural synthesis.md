---
title: "Hybrid generative-procedural synthesis"
aliases:
  - "Hybrid synthetic data generation"
  - "Hybrid generative and procedural synthesis"
  - "Neuro-procedural data synthesis"
tags:
  - method
---

# Hybrid generative-procedural synthesis

## Definition

Hybrid generative-procedural synthesis creates synthetic data by combining learned generative models with explicit procedural, rule-based, rendering, simulation, or physics-driven components.

## Why It Matters

Hybrid systems can separate what should be learned from data from what should remain controllable. A learned generator may synthesize texture, appearance, latent variation, or refinement, while procedural or simulation components may control geometry, scene layout, camera, lighting, physical constraints, labels, masks, or defect placement.

## Typical Use

- Use a simulator or procedural pipeline to produce labels, geometry, masks, or scene structure, then use a learned generator to improve visual realism.
- Use a generative model to produce candidate appearances, defects, or textures, then place or constrain them with rules, rendering, or domain randomization.
- Combine physics or rendering priors with learned image translation, diffusion, GAN, VAE, or other generative refinement.
- Reduce synthetic-to-real domain gap while preserving controllable factors and automatic labels.

## Used In These Papers

- [[2017 - Learning from Simulated and Unsupervised Images through Adversarial Training]] uses SimGAN to refine simulator images with adversarial training while preserving simulator labels.
- [[2018 - RenderGAN Generating Realistic Labeled Data]] combines a 3D marker model with learned GAN augmentations for label-preserving realistic marker images.
- [[2018 - Object Detection using Domain Randomization and Generative Adversarial Refinement of Synthetic Images]] combines physics simulation, ray-traced rendering, domain randomization, and Cyclic-GAN refinement.

## Related Concepts

- [[Synthetic data generation]]
- [[SimGAN]]
- [[RenderGAN]]
- [[Learned generative synthesis]]
- [[Procedural and simulation-based synthesis]]
- [[CycleGAN]]
- [[Rule-based data synthesis]]
- [[Simulation-based data augmentation]]
- [[Domain randomization]]
- [[Defect synthesis]]
- [[GAN]]
- [[Diffusion models]]
