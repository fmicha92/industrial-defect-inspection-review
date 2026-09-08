---
title: "Deep Unsupervised Learning using Nonequilibrium Thermodynamics"
aliases:
  - "Deep Unsupervised Learning using Nonequilibrium Thermodynamics"
  - "Diffusion Probabilistic Models"
paper_key: "sha256:29131f03cd4688d25283b805c91f801948f2a93187c6f058512d84c3b672ba54"
paper_type: "research"
year: 2015
venue: "International Conference on Machine Learning"
authors:
  - "Jascha Sohl-Dickstein"
  - "Eric A. Weiss"
  - "Niru Maheswaranathan"
  - "Surya Ganguli"
status: "processed"
topics:
  - "diffusion probabilistic models"
  - "deep generative models"
  - "nonequilibrium thermodynamics"
tasks:
  - "[[Generative modeling]]"
methods:
  - "[[Diffusion models]]"
  - "[[Learned generative synthesis]]"
model_family:
  - "[[Generative Models]]"
architectures:
  - "multi-layer perceptrons"
metrics:
  - "[[Log likelihood]]"
  - "[[Parzen window log-likelihood]]"
primary_metric:
  - "[[Log likelihood]]"
metric_definitions:
  - "K: Jensen lower bound on model log likelihood"
  - "Parzen-window log-likelihood: MNIST comparison estimator reused from Goodfellow et al. 2014"
datasets:
  - "Swiss roll"
  - "Binary heartbeat"
  - "MNIST"
  - "CIFAR-10"
  - "Bark texture images"
  - "Dead leaves"
baselines:
  - "MCGSM"
  - "Stacked CAE"
  - "DBN"
  - "Deep GSN"
  - "Adversarial net"
code: "https://github.com/Sohl-Dickstein/Diffusion-Probabilistic-Models"
data: "not reported"
doi: "10.48550/arxiv.1503.03585"
arxiv: "1503.03585"
openalex: "https://openalex.org/W2129069237"
url: "http://arxiv.org/abs/1503.03585"
pdf: "https://arxiv.org/pdf/1503.03585"
introduced_by: []
related_papers:
  - "[[2014 - Generative Adversarial Nets]]"
  - "[[2020 - Denoising Diffusion Probabilistic Models]]"
related_concepts:
  - "[[Synthetic data generation]]"
related_methods:
  - "[[Diffusion models]]"
  - "[[Learned generative synthesis]]"
related_tasks:
  - "[[Generative modeling]]"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2015 - Sohl-Dickstein - Deep Unsupervised Learning using Nonequilibrium Thermodynamics.md"
extracted_text: "paper-inbox/90_processing/text/2015 - Sohl-Dickstein - Deep Unsupervised Learning using Nonequilibrium Thermodynamics.txt"
source_file: "paper-inbox/10_processed/Research/2015 - Sohl-Dickstein - Deep Unsupervised Learning using Nonequilibrium Thermodynamics.pdf"
processed_at: "2026-06-02"
---

# Deep Unsupervised Learning using Nonequilibrium Thermodynamics

## Summary

Sohl-Dickstein, Weiss, Maheswaranathan, and Ganguli introduce diffusion probabilistic models as a deep generative modeling framework inspired by nonequilibrium statistical physics. The central idea is to slowly destroy structure in a data distribution through a forward diffusion process, then learn a reverse diffusion process that restores structure and samples from the data distribution. The paper demonstrates the framework on toy distributions, binary sequences, MNIST, CIFAR-10, bark textures, and dead-leaves images, and reports tractable likelihood estimates or bounds for the trained models.

## Paper Type

Research paper. It proposes a generative modeling algorithm, derives its objective and probability evaluation procedure, and evaluates it on synthetic, binary, digit, and natural-image datasets.

## Problem

Flexible probabilistic models can represent rich distributions but are often difficult to normalize, sample from, train, or evaluate. Tractable distributions are easy to work with but too limited for complex data. The paper frames diffusion probabilistic modeling as a way to keep the flexibility of deep generative models while retaining tractable sampling, likelihood evaluation, posterior computation, and distribution multiplication.

## Contribution

- Introduces the diffusion probabilistic modeling framework: a Markov forward process maps data to a tractable noise distribution, and a learned reverse Markov process maps noise back to data.
- Derives a training objective as a lower bound on model log likelihood by comparing forward and reverse diffusion trajectories.
- Shows that the reverse transitions become simple to estimate when the diffusion trajectory uses many small steps, reducing density estimation to regression over Gaussian means/covariances or binomial flip probabilities.
- Demonstrates exact sampling, probability evaluation, and posterior-style manipulations such as image inpainting under the learned model.

## Method

The method defines a forward trajectory `q(x(0...T))` that repeatedly applies a Markov diffusion kernel to transform the data distribution into a tractable distribution such as an identity-covariance Gaussian or an independent binomial distribution. The generative model defines the reverse trajectory `p(x(0...T))`, initialized from the tractable terminal distribution, with learned reverse transitions.

For Gaussian diffusion, the reverse transition is parameterized by learned mean and covariance functions; for binomial diffusion, it is parameterized by learned bit-flip probabilities. The paper uses multi-layer perceptrons for these functions and notes that other regression or function-fitting methods could be used. The training objective maximizes a Jensen lower bound on log likelihood; for the diffusion trajectories used in the paper, the bound decomposes into analytically computable entropies and KL divergences.

## Evidence

### Experimental Setup

- Swiss roll: two-dimensional toy distribution modeled with Gaussian diffusion and radial-basis-function parameterization.
- Binary heartbeat: length-20 binary sequences with periodic pulses modeled with binomial diffusion.
- MNIST: handwritten digits evaluated against several prior models using Parzen-window log-likelihood for comparison.
- CIFAR-10: natural image modeling with generated samples shown.
- Dead leaves: natural image model comparison against MCGSM on the same training and test data.
- Bark texture images: posterior sampling/inpainting demonstration for a missing 100x100 image region.

### Reported Results

- The paper reports lower-bound log likelihood `K` and improvement over a null isotropic Gaussian or independent binomial distribution for Swiss roll, binary heartbeat, bark, dead leaves, and CIFAR-10.
- For dead leaves, the diffusion model reports `1.489 bits/pixel`, compared with `1.244 bits/pixel` for MCGSM in Table 2.
- For MNIST, the diffusion model reports `220 +/- 1.9 bits` with the Parzen-window estimator used for comparison; the listed adversarial-net baseline reports `225 +/- 2 bits`.
- The binary heartbeat experiment is described as nearly perfect, with true-distribution log likelihood `log2 15 = 2.322 bits per sequence`.
- The bark experiment demonstrates inpainting by sampling from the posterior distribution over a missing central region conditioned on the visible region.

## ML/DL Extraction

- Task formulation: unsupervised generative modeling and density estimation.
- Input/output: data samples are diffused into noise; sampling starts from the terminal noise distribution and applies learned reverse transitions to produce data samples.
- Architecture: multi-layer perceptrons define reverse-transition functions; the image experiments use a multi-scale convolutional architecture described in the paper appendix.
- Objective/loss: Jensen lower bound on model log likelihood, built from the ratio between forward and reverse trajectory probabilities.
- Training recipe: maximize the likelihood lower bound with Theano implementation and SFO optimization.
- Evaluation protocol: compare generated samples and log-likelihood estimates/bounds across toy, binary, digit, and natural-image datasets.
- Compute/hardware: not reported.
- Artifacts: an open-source reference implementation is reported at `https://github.com/Sohl-Dickstein/Diffusion-Probabilistic-Models`.

## Limitations

- The source input reports experiments on relatively small or classical datasets compared with later high-resolution image-generation work.
- The reverse process can require many layers or time steps, making sampling cost proportional to the number of reverse evaluations.
- The MNIST comparison uses Parzen-window estimates because prior work reported that metric, and the note records that estimator separately from the likelihood lower bound.
- Appendix implementation details are only partially represented in the available processed input.

## Connections

### Graph Hubs

- Methods: [[Diffusion models]], [[Learned generative synthesis]], [[Generative Models]]
- Tasks: [[Generative modeling]]
- Datasets: Swiss roll, Binary heartbeat, MNIST, CIFAR-10, Bark texture images, Dead leaves
- Domains: not applicable
- Metrics: [[Log likelihood]], [[Parzen window log-likelihood]]
- Method: [[Synthetic data generation]]

### Builds On

- [[2014 - Generative Adversarial Nets]] is cited as an adversarial generative model baseline; the diffusion paper compares MNIST Parzen-window log-likelihood against adversarial nets.

### Follow-Up Reading

- [[2020 - Denoising Diffusion Probabilistic Models]] builds directly on diffusion probabilistic models and shows high-quality image synthesis with a denoising score matching connection and simplified training objective.

### Shares Method

- [[Diffusion models]]: this paper introduces the diffusion-model idea by pairing a fixed forward noising process with a learned reverse generative process.

### Shares Task

- [[Generative modeling]]: the paper learns generative distributions over toy, binary, digit, and natural-image data.

### Shares Metric

- [[Log likelihood]]: the core objective is a lower bound on model log likelihood.
- [[Parzen window log-likelihood]]: used for MNIST comparison to prior generative models.

## Questions

- Which appendix architecture details should be preserved for image experiments if the full appendix is needed later?
- How do the paper's likelihood-oriented results compare with later sample-quality-oriented diffusion models beyond the metrics reported here?
