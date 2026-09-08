---
title: "Modified recall"
aliases:
  - "average modified recall"
  - "AMR"
tags:
  - metric
---
# Modified Recall

## Definition

Modified recall is a source-defined detection metric in [[2024 - Open Stamped Parts Dataset]] that combines recall on real labeled holes with a penalty for predictions made on masked holes.

## Direction

Higher is better.

## Used In These Papers

- [[2024 - Open Stamped Parts Dataset]] uses modified recall to penalize models that incorrectly detect a masked missing hole as present.

## Related Metrics

- [[Recall]]
- [[Precision]]
- [[Modified F0.9 score]]
