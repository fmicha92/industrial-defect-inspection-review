---
title: "Positional encoding"
aliases:
  - "sinusoidal positional encoding"
  - "positional embeddings"
tags:
  - method
---
# Positional Encoding

## Definition

Positional encoding injects token-order information into a model that otherwise has no recurrence or convolution.

## Why It Matters

The Transformer uses sine and cosine positional encodings so input embeddings can carry sequence order while preserving parallel self-attention.

## Used In These Papers

- [[2017 - Attention Is All You Need]] compares sinusoidal positional encodings with learned positional embeddings and reports nearly identical development-set results.

## Related Concepts

- [[Transformer]]
- [[Self-attention]]

