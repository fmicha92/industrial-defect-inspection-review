# Eligibility criteria

## Public dataset registry

Include image datasets with a documented public access route and an identifiable industrial manufacturing inspection context. Extract domain, task, modality, annotation granularity, access conditions, license evidence, and synthesis-evaluation suitability. Contextual datasets may remain in the graph but must be labeled outside the final manufacturing registry when they do not meet scope.

## Synthesis-impact studies

A study is eligible only when all of the following hold:

1. it uses at least one public manufacturing dataset included in the registry;
2. it includes an explicit synthesis intervention such as rule-based insertion, simulation, GAN, diffusion, generative augmentation, or a hybrid;
3. it evaluates a classifier, detector, segmenter, anomaly-detection model, or related inspection pipeline downstream; and
4. the reported outcome can be interpreted relative to a baseline, task, metric, dataset, and annotation condition.

Exclude visual-realism-only evaluations, ordinary augmentation without an explicit synthesis component, private-data-only studies, and non-manufacturing studies retained solely as background.

Eligibility decisions should record one primary exclusion reason and the source note used for verification.

