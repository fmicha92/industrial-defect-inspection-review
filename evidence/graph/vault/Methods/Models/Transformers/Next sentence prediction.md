---
title: "Next sentence prediction"
aliases:
  - "NSP"
tags:
  - method
---
# Next Sentence Prediction

## Definition

Next sentence prediction trains a model to classify whether two input segments occur consecutively in the source text.

## Why It Matters

The BERT paper uses NSP to pretrain text-pair representations and reports that removing it hurts QNLI, MNLI, and SQuAD performance.

## Used In These Papers

- [[2019 - BERT Pre-training of Deep Bidirectional Transformers for Language Understanding]] includes NSP as one of BERT's two pretraining tasks and ablates it.

## Related Concepts

- [[BERT]]
- [[Language model pretraining]]

