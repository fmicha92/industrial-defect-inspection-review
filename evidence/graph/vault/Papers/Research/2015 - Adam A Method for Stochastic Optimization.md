---
title: "Adam: A Method for Stochastic Optimization"
aliases:
  - "Adam A Method for Stochastic Optimization"
paper_key: "arxiv:1412.6980"
paper_type: "research"
year: 2015
venue: "ICLR 2015"
authors:
  - "Diederik P. Kingma"
  - "Jimmy Lei Ba"
status: "processed"
topics:
  - "stochastic optimization"
tasks:
  - "[[Stochastic optimization]]"
datasets:
  - "[[MNIST]]"
  - "[[IMDB movie reviews]]"
  - "[[CIFAR-10]]"
methods:
  - "[[Adam]]"
  - "[[AdaGrad]]"
  - "[[RMSProp]]"
  - "[[AdaMax]]"
  - "[[Stochastic gradient descent]]"
metrics:
  - "[[Error rate]]"
  - "[[Mean Squared Error]]"
primary_metric: "[[Error rate]]"
code: "not reported"
data: "not applicable"
arxiv: "1412.6980"
url: "https://arxiv.org/abs/1412.6980"
source_file: "paper-inbox/10_processed/Research/2015 - Kingma - Adam A Method for Stochastic Optimization.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2015 - Kingma - Adam A Method for Stochastic Optimization.md"
extracted_text: "paper-inbox/90_processing/text/2015 - Kingma - Adam A Method for Stochastic Optimization.txt"
related_methods:
  - "[[Adam]]"
  - "[[AdaGrad]]"
  - "[[RMSProp]]"
  - "[[AdaMax]]"
related_datasets:
  - "[[MNIST]]"
  - "[[IMDB movie reviews]]"
  - "[[CIFAR-10]]"
related_tasks:
  - "[[Stochastic optimization]]"
---
# Adam: A Method for Stochastic Optimization

## Summary

Kingma and Ba introduce [[Adam]], a first-order optimizer for stochastic objectives that adapts per-parameter learning rates from bias-corrected estimates of first and second gradient moments. The paper positions Adam as combining [[AdaGrad]]-style sparse-gradient behavior with [[RMSProp]]-style handling of non-stationary objectives, then evaluates it across convex logistic regression, multilayer neural networks, convolutional networks, and a variational autoencoder.

## Paper Type

Research paper introducing an optimization algorithm and supporting it with theory, algorithmic variants, and empirical optimizer comparisons.

## Problem

The target setting is large-scale, high-dimensional stochastic optimization where objective evaluations are noisy because of minibatches, dropout, or other stochasticity. The paper focuses on first-order methods because higher-order methods are poorly suited to these large parameter spaces.

## Contribution

- Introduces Adam, which maintains moving averages of gradients and squared gradients, corrects their initialization bias, and uses the estimates for adaptive parameter updates.
- Provides an online convex optimization regret analysis with a bound comparable to known adaptive methods under the paper's assumptions.
- Introduces [[AdaMax]], an infinity-norm variant of Adam.
- Shows empirically that Adam is robust across dense, sparse, deterministic, and dropout-regularized training settings.

## Method

Adam initializes first-moment vector `m0` and second raw-moment vector `v0` at zero. At each step it computes a stochastic gradient, updates exponential moving averages controlled by beta1 and beta2, bias-corrects both estimates, and updates parameters using the corrected first moment divided by the square root of the corrected second moment plus epsilon. The paper reports default settings alpha = 0.001, beta1 = 0.9, beta2 = 0.999, and epsilon = 1e-8 for tested machine-learning problems.

## Evidence

| Evaluation | Dataset/model | Baselines | Reported result |
|---|---|---|---|
| Logistic regression | [[MNIST]] | AdaGrad, SGD with Nesterov momentum | Adam converges similarly to momentum SGD and faster than AdaGrad on MNIST negative log likelihood. |
| Sparse logistic regression | [[IMDB movie reviews]] bag-of-words with 50% dropout | AdaGrad, RMSProp, SGD with Nesterov momentum | Adam converges as fast as AdaGrad and much faster than SGD with momentum for sparse features. |
| Multilayer neural network | [[MNIST]], two hidden layers of 1000 ReLU units | AdaGrad, RMSProp, AdaDelta, SGD Nesterov, SFO | Adam makes faster progress than SFO by iteration and wall-clock time; SFO is reported 5-10x slower per iteration and fails with stochastic dropout objectives. |
| Convolutional network | [[CIFAR-10]], c64-c64-c128-1000 architecture | AdaGrad, SGD Nesterov | Adam and AdaGrad reduce cost rapidly early; Adam and SGD eventually converge much faster than AdaGrad. |
| Bias correction | VAE with 500-unit hidden layer and 50-dimensional latent variable | RMSProp-like Adam without bias correction | Bias correction stabilizes training when beta2 is close to 1; Adam performs equal or better than RMSProp across settings. |

## ML/DL Extraction

- Task formulation: minimize stochastic objective functions using minibatch or noisy gradients.
- Model family: optimizer, not a predictive architecture.
- Objective/loss: optimizer-agnostic; experiments include logistic negative log likelihood, cross-entropy, convolutional-network training cost, and VAE loss.
- Training recipe: algorithm defaults alpha = 0.001, beta1 = 0.9, beta2 = 0.999, epsilon = 1e-8; minibatch size 128 in reported logistic, multilayer, and CNN experiments.
- Evaluation protocol: compare training cost or negative log likelihood curves across optimizers after dense hyperparameter search.
- Compute: SFO is reported 5-10x slower per iteration than Adam; exact hardware not reported.
- Artifacts: code not reported.

## Limitations

- The convergence proof applies to online convex optimization assumptions, while several headline experiments are non-convex neural-network settings.
- Empirical comparisons are primarily training-curve comparisons rather than final test-set generalization tables.
- Later optimizer issues such as decoupled weight decay are outside this paper's scope.

## Connections

### Graph Hubs

- Tasks: [[Stochastic optimization]]
- Methods: [[Adam]], [[AdaGrad]], [[RMSProp]], [[AdaMax]], [[Stochastic gradient descent]]
- Datasets: [[MNIST]], [[IMDB movie reviews]], [[CIFAR-10]]
- Domains: [[Document analysis]], [[Natural language processing]], [[General computer vision]]
- Metrics: [[Error rate]], [[Mean Squared Error]]

| Link | Relation | Rationale |
|---|---|---|
| [[AdaGrad]] | Builds on | Adam is designed to preserve AdaGrad's sparse-gradient advantages. |
| [[RMSProp]] | Builds on | Adam inherits the moving-average second-moment idea and adds bias correction. |
| [[AdaMax]] | Method variant | AdaMax is introduced as an infinity-norm Adam variant. |
| [[Stochastic gradient descent]] | Baseline | Momentum SGD is a recurring comparator in the experiments. |
| [[2017 - Attention Is All You Need]] | Follow-up use | The Transformer paper uses Adam with modified beta2, epsilon, and learning-rate schedule. |

## Questions

- How sensitive are the reported conclusions to final validation/test performance rather than training-cost curves?
- How should Adam's original regret analysis be interpreted alongside later convergence critiques?
