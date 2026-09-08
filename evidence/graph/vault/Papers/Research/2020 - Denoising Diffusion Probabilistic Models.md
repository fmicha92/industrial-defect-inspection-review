---
title: "Denoising Diffusion Probabilistic Models"
aliases:
  - "DDPM"
  - "Denoising Diffusion Probabilistic Models"
paper_key: "sha256:cb471d4c0063cad56f8d74b6a72fa7dad1677f8423a0a81349487a63bb58d3de"
paper_type: "research"
year: 2020
venue: "NeurIPS 2020"
authors:
  - "Jonathan Ho"
  - "Ajay Jain"
  - "Pieter Abbeel"
status: "processed"
topics:
  - "diffusion probabilistic models"
  - "image synthesis"
  - "denoising score matching"
tasks:
  - "[[Generative modeling]]"
methods:
  - "[[Diffusion models]]"
  - "[[Learned generative synthesis]]"
model_family:
  - "[[Generative Models]]"
architectures:
  - "[[U-Net]]"
metrics:
  - "[[FID]]"
  - "[[Inception Score]]"
  - "[[Bits per dimension]]"
primary_metric:
  - "[[FID]]"
metric_definitions:
  - "FID: lower-is-better image sample quality metric"
  - "Inception Score: higher-is-better image sample quality metric"
  - "bits/dim: negative log likelihood / codelength"
datasets:
  - "CIFAR-10"
  - "CelebA-HQ 256x256"
  - "LSUN Church 256x256"
  - "LSUN Bedroom 256x256"
baselines:
  - "Diffusion original"
  - "Gated PixelCNN"
  - "Sparse Transformer"
  - "PixelIQN"
  - "EBM"
  - "NCSN"
  - "NCSNv2"
  - "SNGAN"
  - "SNGAN-DDLS"
  - "StyleGAN2 + ADA"
code: "https://github.com/hojonathanho/diffusion"
data: "not reported"
doi: "10.48550/arxiv.2006.11239"
arxiv: "2006.11239"
openalex: "https://openalex.org/W3036167779"
url: "http://arxiv.org/abs/2006.11239"
pdf: "https://arxiv.org/pdf/2006.11239"
introduced_by:
  - "[[2015 - Deep Unsupervised Learning using Nonequilibrium Thermodynamics]]"
related_papers:
  - "[[2015 - Deep Unsupervised Learning using Nonequilibrium Thermodynamics]]"
related_concepts:
  - "[[Synthetic data generation]]"
related_methods:
  - "[[Diffusion models]]"
  - "[[Learned generative synthesis]]"
  - "[[U-Net]]"
related_tasks:
  - "[[Generative modeling]]"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2020 - Ho - Denoising Diffusion Probabilistic Models.md"
extracted_text: "paper-inbox/90_processing/text/2020 - Ho - Denoising Diffusion Probabilistic Models.txt"
source_file: "paper-inbox/10_processed/Research/2020 - Ho - Denoising Diffusion Probabilistic Models.pdf"
processed_at: "2026-06-02"
---

# Denoising Diffusion Probabilistic Models

## Summary

Ho, Jain, and Abbeel present high-quality image synthesis results using diffusion probabilistic models. The paper keeps the forward noising process fixed, parameterizes the reverse process with a neural network, and introduces an epsilon-prediction parameterization that connects diffusion models to denoising score matching over multiple noise levels and annealed Langevin dynamics. On unconditional CIFAR-10, the paper reports Inception Score `9.46` and FID `3.17`, and it demonstrates 256x256 LSUN image samples with FID `7.89` for churches and `4.90` for bedrooms.

## Paper Type

Research paper. It develops a practical diffusion-model training and sampling setup for image synthesis, reports benchmark image-generation metrics, and analyzes rate-distortion/progressive coding behavior.

## Problem

Diffusion probabilistic models were straightforward to define and train, but the paper states that high-quality sample generation had not previously been demonstrated. The goal is to show that diffusion models can generate high-quality images while preserving likelihood evaluation and exposing useful connections to score matching, Langevin dynamics, and progressive lossy coding.

## Contribution

- Shows that diffusion models can generate high-quality image samples, with CIFAR-10 FID `3.17` and Inception Score `9.46`.
- Establishes an explicit connection between diffusion probabilistic models, denoising score matching across noise levels, and annealed Langevin dynamics.
- Introduces a simplified epsilon-prediction training objective, `Lsimple`, that improves sample quality relative to several other objective/parameterization choices.
- Analyzes diffusion sampling as progressive lossy decompression and shows that large image features appear before fine details during reverse generation.

## Method

The model is a latent-variable Markov chain. The forward process gradually adds Gaussian noise to an image through a fixed variance schedule, while the learned reverse process starts from standard Gaussian noise and predicts denoising transitions back to data. The paper fixes the forward variances, uses Gaussian reverse transitions with untrained time-dependent variance, and parameterizes the reverse mean through an epsilon-prediction network.

Training samples a data point, a timestep, and Gaussian noise, then takes a gradient step on the squared error between the sampled noise and the network's predicted noise. Sampling starts from `x_T ~ N(0, I)` and iteratively applies the learned reverse transition. Images are scaled to `[-1, 1]`, and the reverse process uses a U-Net backbone similar to an unmasked PixelCNN++ with group normalization, sinusoidal timestep embeddings, and self-attention at the 16x16 feature map resolution.

## Evidence

### Experimental Setup

- The paper sets `T = 1000` diffusion steps for all experiments.
- The forward-process variances increase linearly from `beta_1 = 10^-4` to `beta_T = 0.02`.
- Experiments evaluate CIFAR-10, CelebA-HQ 256x256, LSUN Church 256x256, and LSUN Bedroom 256x256.
- Sample quality is compared against autoregressive models, energy-based models, score-matching models, GAN variants, and the original diffusion model.

### Reported Results

- On unconditional CIFAR-10, `Lsimple` reports Inception Score `9.46 +/- 0.11`, FID `3.17`, and NLL `<= 5.40` bits/dim in Table 1.
- The model trained on the true variational bound reports better codelengths than the simplified objective, but the simplified objective yields the best sample quality.
- LSUN 256x256 samples report FID `7.89` for churches and `4.90` for bedrooms.
- In the ablation table, epsilon prediction with `Lsimple` reports FID `3.17`, while several learned-variance or unweighted mean-prediction settings are unstable or poor.
- The progressive coding analysis reports a rate of `1.78 bits/dim` and distortion of `1.97 bits/dim`, corresponding to RMSE `0.95` on a `[0, 255]` scale for the highest-quality CIFAR-10 model.

## ML/DL Extraction

- Task formulation: unconditional image synthesis and likelihood/codelength evaluation with diffusion latent variables.
- Input/output: training consumes images and noised versions at sampled timesteps; sampling outputs images by denoising from Gaussian noise.
- Architecture: U-Net-style image model with group normalization, sinusoidal timestep embeddings, and self-attention at 16x16 resolution.
- Objective/loss: simplified epsilon-prediction objective `Lsimple`; the paper also evaluates the true variational bound and reverse-process parameterization alternatives.
- Training recipe: sample `x0`, timestep `t`, and Gaussian noise, then minimize squared noise-prediction error.
- Evaluation protocol: CIFAR-10 sample quality with FID and Inception Score, NLL/codelength in bits/dim, LSUN sample FID, ablations, rate-distortion, progressive generation, and image interpolation.
- Compute/hardware: Google TensorFlow Research Cloud TPUs are acknowledged, but detailed compute configuration is not reported in the main text.
- Artifacts: implementation is reported at `https://github.com/hojonathanho/diffusion`.

## Limitations

- Sampling requires iterating many reverse-process steps; the paper uses `T = 1000`.
- The paper states that its log likelihoods are not competitive with other likelihood-based models, even though sample quality is strong.
- The broader-impact section notes that generative models can be misused for fake images or videos and can reinforce dataset biases.
- Detailed appendix settings are only partially represented in the available processed input.

## Connections

### Graph Hubs

- Methods: [[Diffusion models]], [[Learned generative synthesis]], [[Generative Models]], [[U-Net]]
- Tasks: [[Generative modeling]]
- Datasets: CIFAR-10, CelebA-HQ 256x256, LSUN Church 256x256, LSUN Bedroom 256x256
- Domains: not applicable
- Metrics: [[FID]], [[Inception Score]], [[Bits per dimension]]
- Method: [[Synthetic data generation]]

### Builds On

- [[2015 - Deep Unsupervised Learning using Nonequilibrium Thermodynamics]] introduced diffusion probabilistic models as learned reverse processes for forward diffusion chains; this paper adapts that framework to high-quality image synthesis.

### Shares Method

- [[Diffusion models]]: the paper popularizes the denoising diffusion probabilistic model setup for images and shows strong sample quality.
- [[U-Net]]: the reverse-process network uses a U-Net backbone for image denoising.

### Shares Task

- [[Generative modeling]]: the experiments synthesize image samples from learned data distributions.

### Shares Metric

- [[FID]] and [[Inception Score]]: used for CIFAR-10 sample quality.
- [[Bits per dimension]]: used for negative log likelihood and progressive coding rate analysis.

## Questions

- Which appendix details should be extracted if exact U-Net layer counts, channel multipliers, or training hyperparameters are needed?
- How should later faster samplers and latent diffusion variants be connected back to this source paper?
