---
title: "SCAN"
aliases:
  - "Simplified CommAI Navigation tasks"
related_domain: "[[Natural language processing]]"
url: "https://github.com/brendenlake/SCAN"
introduced_by: "[[2018 - Generalization without Systematicity On the Compositional Skills of Sequence-to-Sequence Recurrent Networks]]"
tags:
  - dataset
  - benchmark
---

# SCAN

## Definition

SCAN is a synthetic command-to-action benchmark for testing systematic compositional generalization in sequence-to-sequence models.

## Dataset Details

- Full generated grammar size: 20,910 unambiguous commands.
- Input vocabulary: 13 words.
- Output vocabulary: 6 actions.
- Tasks: random split, longer-sequence split, new-primitive split, and related compositional generalization probes.

## Related Papers

- [[2018 - Generalization without Systematicity On the Compositional Skills of Sequence-to-Sequence Recurrent Networks]] introduces SCAN and uses it to show failures of recurrent sequence-to-sequence models under systematic splits.
