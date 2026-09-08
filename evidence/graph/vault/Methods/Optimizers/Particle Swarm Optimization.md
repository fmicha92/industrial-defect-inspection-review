---
title: "Particle Swarm Optimization"
aliases:
  - "PSO"
tags:
  - method
---

# Particle Swarm Optimization

## Definition

Particle Swarm Optimization is a population-based optimization method that searches a parameter space with multiple candidate solutions, called particles. Each particle updates its position using its own best-found position and the best position found by the swarm.

## Why It Matters

PSO is useful when a model has hyperparameters that are expensive or awkward to tune manually. In textile inspection, [[2025 - AI-driven fabric classification]] uses PSO to tune the learning rate and momentum of [[ResNet50]], producing [[PSRT50]].

## Used In These Papers

- [[2025 - AI-driven fabric classification]] uses PSO to optimize [[ResNet50]] learning rate and momentum for real-time fabric classification.

## Related Concepts

- [[Stochastic gradient descent]]
- [[ResNet50]]
- [[PSRT50]]
- [[Accuracy]]
