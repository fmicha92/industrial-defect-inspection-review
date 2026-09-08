export const researchQuestions = [
  [
    "RQ1",
    "Public datasets",
    "Which public image datasets are available for visual defect inspection in industrial manufacturing, and how do they differ by domain, task, modality, annotation level, access, and suitability for evaluating data synthesis?",
  ],
  [
    "RQ2",
    "Synthesis methods",
    "Which data synthesis methods are most promising, based on studies that use those public datasets and report downstream ML inspection outcomes?",
  ],
  [
    "RQ3",
    "ML methods",
    "Which ML classifiers, detectors, segmenters, anomaly-detection models, or related inspection pipelines are most promising when evaluated on those public datasets with data synthesis support?",
  ],
] as const;

export const workflow = [
  [
    "01",
    "Define the inspection problem",
    "Make scarcity, imbalance, annotation cost, and private-data constraints explicit.",
  ],
  [
    "02",
    "Select a public dataset",
    "Record domain, task, modality, annotation, access, and benchmark role.",
  ],
  [
    "03",
    "Specify synthesis as an intervention",
    "Name the method family and the rare defect or underrepresented class it targets.",
  ],
  [
    "04",
    "Specify the inspection model",
    "Identify the classifier, detector, segmenter, localizer, or anomaly-detection model.",
  ],
  [
    "05",
    "Evaluate downstream performance",
    "Use a task-appropriate metric with a real-data-only baseline or another interpretable comparator.",
  ],
  [
    "06",
    "Interpret conditionally",
    "Separate traceable benefit, fragmented evidence, and deployment relevance.",
  ],
] as const;

export const challenges = [
  "Evidence remains fragmented by task and metric",
  "Incomplete baseline transparency and original-data reporting",
  "Positive-evidence selection and the limits of synthesis",
  "Attribution is difficult in hybrid pipelines",
  "Diffusion evidence is promising but uneven",
  "Public datasets underrepresent industrial deployment",
] as const;

export const recommendations = [
  [
    "Choose the dataset before choosing the synthesis method",
    "Begin with domain, task, modality, annotation, access, and benchmark suitability; only then judge a generator against the data problem.",
  ],
  [
    "Build larger datasets from compatible public sources",
    "Screen task formulation, annotation policy, imaging modality, semantics, scale, access, and domain shift before combining records.",
  ],
  [
    "Report real-only baselines and original-data conditions",
    "Make dataset version, split, distribution, baseline model, metric, and paired scores visible.",
  ],
  [
    "Evaluate synthesis by downstream benefit",
    "Visual plausibility may screen samples, but matched inspection performance is the central comparison.",
  ],
  [
    "Separate synthesis effects from model-tuning effects",
    "Use ablations across real-only, tuned real-only, real-plus-synthesis, and tuned synthesis-supported conditions.",
  ],
  [
    "Interpret methods within task and dataset conditions",
    "Do not rank classification, detection, segmentation, localization, and anomaly results as though they were interchangeable.",
  ],
  [
    "Design future public datasets for synthesis evaluation",
    "Publish acquisition context, defect rarity, imbalance, annotations, stable splits, domain shift, baselines, and intended use.",
  ],
] as const;
