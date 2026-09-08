---
title: "Masked language modeling"
aliases:
  - "MLM"
  - "masked LM"
tags:
  - method
---
# Masked Language Modeling

## Definition

Masked language modeling pretrains a model by masking selected input tokens and training the model to predict their original identities from surrounding context.

## Why It Matters

BERT uses masked language modeling to train deep bidirectional representations rather than constraining pretraining to left-to-right language modeling.

## Used In These Papers

- [[2019 - BERT Pre-training of Deep Bidirectional Transformers for Language Understanding]] uses masked language modeling as the primary bidirectional pretraining objective.

## Related Concepts

- [[BERT]]
- [[Self-attention]]
- [[Language model pretraining]]

