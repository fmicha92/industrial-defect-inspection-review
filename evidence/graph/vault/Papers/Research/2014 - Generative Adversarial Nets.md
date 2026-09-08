---
title: "Generative Adversarial Nets"
aliases:
  - "Goodfellow et al. 2014 GAN"
  - "Original GAN paper"
paper_key: "arxiv:1406.2661"
paper_type: research
year: 2014
venue: "arXiv stat.ML"
authors:
  - "Ian J. Goodfellow"
  - "Jean Pouget-Abadie"
  - "Mehdi Mirza"
  - "Bing Xu"
  - "David Warde-Farley"
  - "Sherjil Ozair"
  - "Aaron Courville"
  - "Yoshua Bengio"
status: processed
processed_at: 2026-06-02
topics:
  - "generative modeling"
  - "adversarial training"
tasks:
  - "[[Generative modeling]]"
domains: []
application_area: "general generative modeling"
datasets:
  - "MNIST"
  - "Toronto Face Database"
  - "CIFAR-10"
methods:
  - "[[GAN]]"
  - "[[Learned generative synthesis]]"
model_family:
  - "[[Generative Models]]"
architectures:
  - "multilayer perceptron generator"
  - "multilayer perceptron discriminator"
losses:
  - "two-player minimax adversarial objective"
training_regime: "adversarial training"
augmentation: []
synthetic_data: "generated samples from random noise through a learned generator"
metrics:
  - "[[Parzen window log-likelihood]]"
primary_metric: "[[Parzen window log-likelihood]]"
metric_definitions:
  - "Gaussian Parzen window fitted to generated samples; report test-set log-likelihood under that density estimate."
baselines:
  - "DBN"
  - "Stacked CAE"
  - "Deep GSN"
benchmarks:
  - "MNIST generative sample evaluation"
  - "Toronto Face Database generative sample evaluation"
evaluation_protocol: "Fit a Gaussian Parzen window to samples from the generator, choose sigma by validation, and report test-set log-likelihood estimates."
parameters: "not reported"
compute: "not reported"
hardware: "not reported"
training_time: "not reported"
inference_cost: "sampling uses forward propagation through the generator"
url: "https://arxiv.org/abs/1406.2661"
pdf: "paper-inbox/10_processed/Research/2014 - Goodfellow - Generative Adversarial Nets.pdf"
code: "http://www.github.com/goodfeli/adversarial"
data: "MNIST, TFD, and CIFAR-10 are used; dataset download sources are not reported."
doi: "10.48550/arXiv.1406.2661"
arxiv: "1406.2661"
related_papers:
  - "[[2022 - A Survey of Defect Detection Applications Based on Generative Adversarial Networks]]"
related_concepts:
  - "[[Synthetic data generation]]"
related_methods:
  - "[[GAN]]"
  - "[[Learned generative synthesis]]"
related_datasets: []
related_domains: []
related_tasks:
  - "[[Generative modeling]]"
related_benchmarks: []
concept_notes_created_or_updated:
  - "[[GAN]]"
  - "[[Generative Models]]"
  - "[[Learned generative synthesis]]"
  - "[[Synthetic data generation]]"
  - "[[Parzen window log-likelihood]]"
source_file: "paper-inbox/10_processed/Research/2014 - Goodfellow - Generative Adversarial Nets.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2014 - Goodfellow - Generative Adversarial Nets.md"
extracted_text: "paper-inbox/90_processing/text/2014 - Goodfellow - Generative Adversarial Nets.txt"
artifact_status: "code URL reported by paper; data sources and trained checkpoints not reported"
tags:
  - paper
---

# Generative Adversarial Nets

## Summary

Goodfellow et al. introduce [[GAN|generative adversarial networks]], a generative modeling framework that trains a generator and discriminator in a two-player minimax game. The generator maps random noise into samples, while the discriminator estimates whether a sample came from the training data or the generator. The paper shows, in a non-parametric theoretical setting, that the game has an optimum when the generator distribution matches the data distribution and the discriminator cannot distinguish generated from real samples.

## Paper Type

- Type: research.
- Why: the paper proposes a new generative modeling framework, derives theoretical properties of the objective, and evaluates generated samples on image datasets.

## Problem

- Task: learn a generative model of complex data distributions.
- Setting: deep generative modeling with differentiable generator and discriminator networks.
- Inputs: random noise variables sampled from a prior for generation; real data samples for discriminator training.
- Outputs: generated samples intended to match the data distribution.
- Motivation: deep generative models had been difficult to train because maximum-likelihood and related methods often required intractable inference, partition-function estimation, Markov chains, or approximate posterior networks.
- Assumptions: the theoretical analysis assumes sufficient model capacity and, for convergence, discriminator optimization close to its optimum for the current generator.

## Contribution

- Claimed: introduces the adversarial generative modeling framework now known as [[GAN]], where a generator and discriminator are trained jointly by backpropagation in a minimax game.
- Claimed: shows that, in the non-parametric limit, the global optimum is reached when the generator distribution equals the data distribution and the optimal discriminator outputs one half everywhere.
- Shown: demonstrates sample generation and Parzen-window log-likelihood estimates on MNIST and the Toronto Face Database, plus qualitative samples on CIFAR-10.
- Inferred: the paper is the origin anchor for later GAN-based defect synthesis and augmentation methods in the vault.

## Method

- Core idea: pit a generative model against a discriminative model; the discriminator learns to separate real data from generated samples, and the generator learns to make the discriminator fail.
- Architecture / algorithm: the paper explores the case where both generator and discriminator are multilayer perceptrons. The generator maps noise `z` through `G(z)` into data space; the discriminator maps data samples to a scalar probability `D(x)`.
- Objective / loss: the discriminator maximizes correct assignment for real and generated samples; the generator minimizes the discriminator's success on generated samples. The paper also notes that maximizing `log D(G(z))` can provide stronger gradients early in learning than minimizing `log(1 - D(G(z)))`.
- Optimization: alternating minibatch stochastic gradient descent; the experiment uses one discriminator update step per generator update and momentum.
- Training data: MNIST, Toronto Face Database, and CIFAR-10.
- Data pipeline: sample minibatches from the data distribution and minibatches of noise from the prior.
- Augmentation / synthesis: generation is learned from noise rather than produced by hand-coded augmentations.
- Inference: sampling requires only forward propagation through the generator.
- Complexity / deployment constraints: training requires synchronizing the discriminator and generator; likelihood is not explicitly represented.

## ML / DL Extraction

### Task Formulation

- Input modality: images.
- Output target: generated images drawn from a learned model distribution.
- Supervision: unsupervised generative modeling, with discriminator labels indicating real versus generated samples during training.
- Objective: adversarial minimax training to match the generator distribution to the data distribution.

### Model And Training

- Model family: [[Generative Models]], specifically [[GAN]].
- Architecture: multilayer perceptron generator and multilayer perceptron discriminator in the main described setup; CIFAR-10 examples also include a convolutional discriminator and deconvolutional generator visualization.
- Parameters: not reported.
- Pretraining: not reported.
- Fine-tuning: not applicable.
- Losses: adversarial minimax objective; stronger-gradient generator variant described for early training.
- Optimizer: minibatch stochastic gradient descent with momentum.
- Hyperparameters: the number of discriminator steps per generator step is a hyperparameter; the experiments use `k = 1`.
- Seeds: not reported.
- Training compute: not reported.

### Data

- Datasets: MNIST, Toronto Face Database, CIFAR-10.
- Data source: standard benchmark datasets; download sources not reported.
- Dataset size: not reported in the extracted text.
- Labels / annotations: labels are not central to the generative objective; dataset labels are not described as used.
- Splits: validation data are used to cross-validate Parzen-window sigma; test data are used for reported log-likelihood estimates. Exact split sizes are not reported.
- Preprocessing: not reported.
- Augmentation: not reported.
- Synthetic data: the generator produces synthetic samples from random noise.
- Leakage checks: nearest-neighbor visualization is used to argue that displayed generated samples are not memorized training examples.
- License: not reported.

### Evaluation

- Protocol: fit a Gaussian Parzen window to generated samples, choose sigma on validation data, and report test-set log-likelihood estimates. Visual samples and nearest training examples are also shown.
- Used performance metrics: [[Parzen window log-likelihood]].
- Primary metric: [[Parzen window log-likelihood]].
- Metric definitions: Gaussian Parzen density fitted to generated samples and evaluated as test-set log-likelihood.
- Metric direction / units: higher log-likelihood is better; unit is reported as log-likelihood estimate.
- Baselines: DBN, Stacked CAE, Deep GSN.
- Benchmarks: MNIST and Toronto Face Database for Table 1; CIFAR-10 for qualitative generated samples.
- Statistical tests: not reported.
- Failure cases: discriminator/generator synchronization problems and diversity collapse risk are discussed as disadvantages.

## Evidence

### Experimental Setup

- Datasets: MNIST, Toronto Face Database, CIFAR-10.
- Splits: validation set for sigma selection and test set for log-likelihood estimates; exact split sizes not reported.
- Baselines: DBN, Stacked CAE, Deep GSN.
- Used performance metrics: [[Parzen window log-likelihood]].
- Compute: not reported.
- Hardware: not reported.
- Training time: not reported.
- Inference cost: sampling by forward propagation; exact runtime not reported.

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| Adversarial nets compared with Deep GSN | MNIST generation | Parzen-window log-likelihood | higher | 214 +/- 1.1 | 225 +/- 2 | DBN is 138 +/- 2; Stacked CAE is 121 +/- 1.6. |
| Adversarial nets compared with Stacked CAE | TFD generation | Parzen-window log-likelihood | higher | 2110 +/- 50 | 2057 +/- 26 | DBN is 1909 +/- 66; Deep GSN is 1890 +/- 29. |
| Generated sample visualization | MNIST, TFD, CIFAR-10 | qualitative samples | not applicable | not applicable | samples shown | The paper states samples are fair random draws rather than cherry-picked and includes nearest training examples. |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[Parzen window log-likelihood]] | Generated image evaluation on MNIST and TFD | Gaussian Parzen-window density fitted to generated samples; report test-set log-likelihood | higher | yes | The paper states this method has high variance and does not perform well in high-dimensional spaces. |

### Ablations

- not reported.

## Dataset / Benchmark Details

- Source: MNIST, Toronto Face Database, and CIFAR-10.
- Collection: not reported.
- Annotation: labels are not reported as used by the generative objective.
- Size: not reported.
- Splits: validation and test use are reported for Parzen-window evaluation; exact split sizes not reported.
- Modalities: image.
- License: not reported.
- Leakage risks: visual nearest-neighbor comparison is used to check whether samples resemble memorized training examples.
- Bias / coverage: not reported.
- Maintenance: not reported.

## Limitations

- Stated: GANs do not explicitly represent the model density `p_g(x)`.
- Stated: the discriminator must stay synchronized with the generator during training.
- Stated: overtraining the generator without enough discriminator updates can collapse many noise inputs to the same output, reducing diversity.
- Stated: Parzen-window likelihood evaluation has high variance and weak performance in high-dimensional spaces.
- Inferred: the original experiments are proof-of-concept image generation experiments rather than task-specific data augmentation evaluations.

## Reproducibility

- Code: the paper reports code and hyperparameters at `http://www.github.com/goodfeli/adversarial`.
- Data: MNIST, Toronto Face Database, and CIFAR-10 are named; download and licensing details are not reported.
- Hyperparameters: `k = 1` discriminator step per generator step is reported; other hyperparameters are not reported in the extracted text.
- Random seeds: not reported.
- Environment: not reported.
- Checkpoints / models: not reported.
- Exact preprocessing: not reported.
- Artifact status: code URL reported; dataset acquisition, environment, and trained checkpoints not reported.

## Connections

### Graph Hubs

- Tasks: [[Generative modeling]]
- Methods: [[GAN]], [[Generative Models]], [[Learned generative synthesis]]
- Datasets: MNIST, Toronto Face Database, CIFAR-10
- Domains: not applicable; general generative modeling
- Metrics: [[Parzen window log-likelihood]]

### Builds On

| Link | Relation | Rationale |
|---|---|---|
| [[Generative Models]] | Method family | The paper introduces a new deep generative modeling framework. |

### Shares Method

| Link | Relation | Rationale |
|---|---|---|
| [[GAN]] | Introduces method | This paper introduces the adversarial generator-discriminator framework and is the origin paper for GANs. |
| [[Learned generative synthesis]] | Method family | The generator learns to synthesize samples from noise through a trained model. |

### Shares Metric

| Link | Relation | Rationale |
|---|---|---|
| [[Parzen window log-likelihood]] | Evaluation metric | The paper uses Parzen-window log-likelihood estimates for MNIST and TFD generated samples. |

### Related Concepts

| Link | Relation | Rationale |
|---|---|---|
| [[Synthetic data generation]] | Related concept | GANs synthesize artificial samples, though this paper evaluates generative modeling rather than downstream augmentation. |

### Follow-up Reading

| Link | Relation | Rationale |
|---|---|---|
| [[2022 - A Survey of Defect Detection Applications Based on Generative Adversarial Networks]] | Follow-up reading | Later survey literature applies GAN variants to defect detection and industrial inspection. |

## Questions

- Which later GAN variants in the vault should be explicitly linked back to this origin paper as `Builds on` rather than only to the `GAN` method note?
- Should the original GAN paper be promoted into a broader foundational generative modeling index?
