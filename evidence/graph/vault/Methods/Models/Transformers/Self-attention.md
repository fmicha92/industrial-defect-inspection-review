---
title: "Self-attention"
aliases:
  - "intra-attention"
tags:
  - method
---
# Self-Attention

## Definition

Self-attention relates positions within a single sequence so each position can compute a representation using information from other positions.

## Why It Matters

The Transformer uses self-attention to remove recurrence from sequence transduction, and BERT uses bidirectional Transformer self-attention to condition token representations on both left and right context.

## Used In These Papers

- [[2017 - Attention Is All You Need]] uses self-attention in both encoder and decoder layers.
- [[2019 - BERT Pre-training of Deep Bidirectional Transformers for Language Understanding]] relies on bidirectional self-attention in Transformer encoders.

## Related Concepts

- [[Transformer]]
- [[Multi-head attention]]
- [[Masked language modeling]]

