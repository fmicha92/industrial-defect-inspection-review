# Detailed Paper Processing Guide

This reference preserves the full extraction, taxonomy, and graph-linking policy. Follow the concise workflow in the parent `SKILL.md` first, then consult the relevant section here.

Use this skill when turning a scientific paper into a faithful, structured
Obsidian note. Prioritize extraction quality over polished prose: separate what
the paper claims, what it demonstrates, and what remains uncertain.

Never use model training knowledge, memory, or outside assumptions as evidence
for paper notes. Use only the actual paper/source text being read and explicit
metadata fetched for that paper. If a detail is absent, write `not reported`. If
a field does not apply to the paper type, write `not applicable`.

If the `paper-preprocessing` workflow has produced a file in
`workspace/paper-inbox/90_processing/analysis-inputs/`, use that as the default source
for reading. Only fall back to raw PDFs when preprocessing failed or the user
asks for direct PDF analysis.

Preprocessing is only an input-compression step. It is not a substitute for
reading. After preprocessing, read the analysis input thoroughly enough to
extract every source-supported item required by the note template. Do not skim
only the title, abstract, first page, or obvious snippets when creating a final
paper note.

Dataset notes may also be created or updated directly from a public dataset host
page, such as Kaggle, GitHub, IEEE DataPort, Zenodo, Hugging Face, or an
institutional repository. Treat the dataset host page as source text for
dataset-note fields only; do not infer paper results, benchmark scores, or
paper claims from the host page unless the host page explicitly reports them.

## Generated Note Language

Write generated Obsidian notes as standalone research notes, not as commentary
about the note system or processing workflow.

- Do not use vault-relative or self-referential prose in note bodies, concept
  definitions, summaries, evidence, limitations, or connection rationales.
- Avoid phrases like `in this vault`, `used here`, `this note`, `processed
  papers`, `graph node`, `intake`, `manifest`, or `curation` in generated note
  prose unless they are literal quoted source text.
- Avoid source-facing prose such as `the host page describes`, `the host page
  frames`, `the source says`, or `the extracted text reports` in definitions,
  summaries, and rationale sections. State source-supported facts directly in
  subject-facing language, and keep provenance in `## Source Anchors` or
  source-specific detail bullets.
- Prefer subject-facing phrasing: write "The paper evaluates..." or "The
  dataset contains..." instead of explaining why something exists in the note
  system.
- Keep processing provenance in frontmatter fields such as `source_file`,
  `preprocessed_input`, `extracted_text`, `paper_key`, and `processed_at`. If
  human-readable processing detail is necessary, put it under a clearly labeled
  `## Processing Notes` section rather than mixing it into scholarly content.

## Many-Paper Processing Policy

For large drops of new papers, split mechanical intake from judgment-heavy note
creation:

1. **Preprocess in bulk**: It is safe to scan and preprocess many incoming files
   at once with the `paper-preprocessing` workflow. This handles duplicate
   detection, text extraction, compact analysis input generation, and manifest
   updates.
2. **Process all new papers sequentially**: Add papers to Obsidian one by one,
   but keep going through the full new-paper backlog. For each paper, read the
   preprocessed analysis input thoroughly, create the final Obsidian note, graph
   links, new concept nodes, reciprocal backlinks, and processed manifest status
   before starting the next paper. Do not create final notes for many papers in
   a single combined pass unless the user explicitly asks for low-depth triage.
   Sequential processing is a quality gate, not permission to make shallow
   notes quickly.
3. **Audit after each paper or small run**: Run the graph audit after each
   completed paper when graph quality matters.

Default behavior: when the user asks to process many papers, first bulk
preprocess everything, then work through every preprocessed new paper
sequentially until the backlog is done or a real blocker appears.

## New Source Reporting

When new papers are added to the vault, report each processed paper in chat as
its own short paragraph. Include:

- paper title or note name
- key points of what was created or changed
- `Files changed: N`
- `Files added: N`
- `Connections added: N`

For a single new paper, still include the three numeric reporting lines. For
multiple new papers, repeat the same short paragraph format for each paper.

Use the same format when adding or updating vault notes from web sources, such
as dataset host pages. Report each added or updated web source as its own short
paragraph with the source/note name, key points, and the same three numeric
lines.

## Web Source Batch Policy

When multiple web sources are provided, process them one by one. For each web
source, read the source, create or update the matching vault note, refresh
graph connections and reciprocal backlinks, and report the result before
starting the next source.

Extract only facts explicitly present in the web source being read and existing
vault notes used for identity or connection checks. Do not infer missing dataset
sizes, licenses, tasks, domains, papers, results, availability, or access terms
from memory, host conventions, or similar datasets. If a field is absent, write
`not reported`.

## Workflow

1. **Identify the source**: Prefer `workspace/paper-inbox/90_processing/analysis-inputs/` when available, otherwise the paper PDF or official landing page.
2. **Classify the paper**: Set `paper_type` to `research`, `review`, `dataset`, `benchmark`, or `systems`.
3. **Extract metadata**: Title, authors, year, venue, affiliations if relevant, topic area, tasks, datasets, methods, metrics, identifiers, artifacts, and links.
4. **Read for structure**: Abstract, introduction, method, experiments, results, limitations, conclusion, appendices. For long papers, process section-by-section. Do not skip dataset, experiment, ablation, implementation, or limitation sections just because the abstract seems sufficient.
5. **Capture the contribution**: Write the core contribution in 1-3 precise bullets. Do not overstate novelty beyond what the paper supports.
6. **Extract ML/DL details**: Task formulation, inputs/outputs, model family, architecture, objective/loss, training recipe, data pipeline, augmentation/synthesis, inference path, and deployment constraints.
7. **Extract evidence**: Note experimental setup, baselines, ablations, dataset splits, used performance metrics, evaluation protocol, and the strongest/weakest results.
8. **Assess reliability**: Look for code/data availability, reproducibility details, leakage risks, benchmark saturation, missing baselines, compute requirements, and evaluation limitations.
9. **Create or update an Obsidian note**: Use Obsidian markdown with YAML frontmatter, wikilinks for internal concepts, and external markdown links for URLs.
10. **Extract graph notes**: Identify concepts, methods, datasets, tasks, benchmarks, application domains, failure modes, metrics, and assumptions that should be reusable graph notes.
11. **Route or stage graph notes**: Reuse stable folders when the fit is clear. If a concept is interesting but does not fit the current taxonomy, create it under the appropriate emerging folder with promotion metadata.
12. **Link the note graph thoroughly**: Connect the new note to existing paper and concept notes, create missing concept notes when they are central, and add reciprocal links where the target note should know about this paper.
13. **End with open questions**: Preserve unresolved technical questions, follow-up experiments, and papers to read next.

## Dataset Web Source Workflow

Use this workflow when the user asks to add a dataset from a web host rather
than from a paper PDF.

1. **Read the host page**: Use Defuddle for ordinary web pages when possible.
   For Kaggle, GitHub, DataPort, Zenodo, Hugging Face, or similar hosts, capture
   the canonical URL, dataset title, owner/organization, access status, license,
   files or modalities, labels/annotations, size, task, domain, and citation or
   paper references when reported. Extract only facts that are actually present
   in the host page or explicit linked metadata being read; do not fill gaps
   from memory, assumptions, or likely dataset conventions. When writing the
   note, convert host-page evidence into direct dataset prose; do not write
   formulations like `the host page describes...` or `the host page frames...`.
2. **Check for an existing dataset note**: Search aliases, title, host URL, DOI,
   repository name, and paper links before creating a new note. Update the
   existing note when the web source clearly names the same dataset.
3. **Route by availability**: Put the dataset note under `Datasets/Public`,
   `Datasets/Private`, or `Datasets/Availability Unspecified` based on the host
   page and any explicit access restrictions. Kaggle and GitHub are public only
   when the dataset files or release are actually accessible; if access requires
   approval or is unclear, use `Availability Unspecified` or `Private` as
   supported by the source.
4. **Record source anchors**: The dataset note frontmatter should include `url`
   for the canonical host page and `data_source` or `data_sources` for the
   hosting platform/source when a host exists. It should also include
   `related_papers` or `introduced_by` for the most relevant paper that
   introduces the dataset when such a paper exists. The body must include a
   `## Source` or dataset-detail bullet pointing to the host URL and another
   bullet linking the introducing paper note when it exists; otherwise add the
   external paper URL or write `not reported`.
5. **Separate host evidence from paper evidence**: Facts from the host page can
   support dataset availability, size, modality, labels, license, and download
   location. Experimental results, benchmark claims, and paper contribution
   claims still require the paper/source text that reports them.
6. **Connect the graph**: Link the dataset to exactly one supported domain using
   `domain` or `related_domain`, never plural domain fields. If the dataset
   spans more than one industry, material class, application area, or sensor/use
   context, route it only to `[[Multi-Industry Anomaly Detection]]`, remove any
   narrower domain associations, and update only that reciprocal domain's
   `## Related Datasets` section.
7. **Preserve uncertainty**: If the host page and paper disagree, record both
   source-specific claims with dates or source labels rather than merging them.
   If a field is absent, write `not reported`.

## Reading Depth

Choose the smallest depth that satisfies the request:

- `triage`: metadata, paper type, one-paragraph summary, contribution, read/skip rationale.
- `standard`: full note with problem, method, evidence, limitations, connections, and questions.
- `deep`: standard note plus section-by-section analysis, result tables, ablation analysis, reproducibility audit, and follow-up reading map.

When the user does not specify depth, use `standard` and process one paper at a
time. Use `triage` for batches only when the user asks for screening or a
low-depth pass instead of final paper notes. A `triage` pass must not mark a
paper as fully processed or produce a final paper note unless the note is
explicitly labeled as triage and kept out of the processed-paper workflow.

## Completion Standard

A final paper note must be as complete as the available input permits. Before
marking a paper processed, verify that the analysis input was read beyond the
abstract and that the note captures all source-supported details available for:

- problem, contribution, method, and claimed novelty
- datasets, collection process, sizes, splits, labels, modalities, and licenses
- training setup, losses/objectives, optimizer, hyperparameters, preprocessing,
  augmentation or synthesis, and compute/hardware
- evaluation protocol, baselines, ablations, metrics, metric direction/units,
  and reported values
- artifact availability for code, data, models, and reproducibility materials
- stated limitations, failure cases, and future work
- graph links to tasks, datasets, methods, domains, metrics, benchmarks, and
  important related papers

Use `not reported` only after checking the relevant source section. Do not use
placeholder wording such as `not reported in this concise extraction`, `not
fully extracted`, `not fully reported`, or `see extracted snippets below` in a
final processed note. If the source input is too incomplete to support a full
note, keep the paper unprocessed or explicitly record the blocker instead of
writing a shallow final note.

## Note Structure

Use the template in [PAPER_NOTE_TEMPLATE.md](PAPER_NOTE_TEMPLATE.md) for full paper notes.

Minimum note sections:

- `Summary`: concise, factual overview.
- `Paper Type`: why it is research, review, dataset, benchmark, etc.
- `Problem`: task, setting, assumptions, and motivation.
- `Contribution`: what is new or useful.
- `Method`: model, algorithm, objective, training data, data pipeline, inference, or taxonomy.
- `Evidence`: experiments, baselines, metrics, ablations, and results.
- `ML/DL Extraction`: task formulation, architecture, losses, optimizer, training recipe, evaluation protocol, compute, and artifacts.
- `Limitations`: stated and inferred limits.
- `Connections`: related papers, methods, datasets, tasks, benchmarks, concepts, and connection rationale.
- `Questions`: what to verify or read next.

## Graph Linking

After extracting concepts from a paper, do a dedicated graph-building pass. The
goal is not just to add tags; the goal is to make the paper discoverable through
meaningful Obsidian links.

If an existing paper note is updated after a re-read or audit, repeat this
graph-building pass from scratch for the changed content. New or corrected facts
about datasets, tasks, methods, metrics, domains, benchmarks, baselines,
artifacts, or related papers must be linked into the existing vault again, and
important reciprocal backlinks must be refreshed. Do not leave a repaired paper
note as an isolated local edit.

1. **Inventory existing nodes**: Before writing links, inspect `evidence/graph/vault/Papers/`,
   the stable graph folders, and the parent-scoped `*/Emerging *` folders for
   existing notes that match the paper's datasets, methods, learning paradigms,
   tasks, domains, metrics, benchmarks, and related papers.
2. **Reuse canonical notes**: Link to existing notes with the exact note title
   when they already exist. Avoid near-duplicate concept notes such as
   `Surface defect detection` and `Surface defects` unless the distinction is
   explicit and useful.
3. **Create or stage missing concept notes**: If a concept is central and fits a
   stable folder, create it under the appropriate graph folder. If it is central
   but the folder fit is uncertain, stage it under the related parent's
   emerging subfolder, such as `Concepts/Emerging Concepts/`,
   `Methods/Emerging Methods/`, `Domains/Emerging Domains/`,
   `Metrics/Emerging Metrics/`, or
   `Learning Paradigms/Emerging Learning Paradigms/`, with promotion metadata
   and graph links. A new concept note must explain the concept, not just exist
   as a link target.
4. **Explain new concepts**: Every newly created concept note needs a short
   grounded explanation with this minimum structure: `## Definition`, `## Why It
   Matters`, `## Used In These Papers`, and `## Related Concepts`. The definition
   must be based on the processed paper text and linked paper notes. If the
   available papers do not support a full definition, say what is known and mark
   the rest as `not reported` or `inferred`.
5. **Use bidirectional links for important relations**: When a paper is strongly
   connected to an existing concept, dataset, domain, method, benchmark, or
   paper, update the target note with a backlink to the new paper and a one-line
   reason. Do not add reciprocal links for weak or merely keyword-level matches.
   For updated paper notes, check whether old backlinks are stale and whether
   new facts require new backlinks.
6. **Classify relationship types**: In the paper's `Connections` section, group
   links by relation type: `Builds on`, `Contrasts with`, `Shares dataset`,
   `Shares task`, `Shares method`, `Shares metric`, `Application/domain`, and
   `Follow-up reading`.
7. **Explain why each important link exists**: For each related paper link, write
   a short rationale such as "both use synthetic defect generation for visual
   inspection, but this paper evaluates unsupervised localization." Do not leave
   unexplained link dumps.
8. **Promote repeated concepts to graph hubs**: If three or more paper notes use
   the same dataset, task, method, or domain, make or update a dedicated concept
   note and point all relevant paper notes to it.
9. **Respect source integrity**: The link target may be chosen from existing note context,
   but the factual claim about this paper must still come from the source text.
   Mark inferred relationships as `inferred` when the paper does not state them
   directly.
10. **Use subject-facing concept prose**: Definitions, "Why It Matters", and
   connection rationales must describe the research object itself. Do not write
   metacommentary about why a note exists, where it is stored, or how it is used
   by the graph.

## Adaptive Taxonomy

The folder taxonomy is a stable starting taxonomy, not a closed ontology. Do not
force new research topics into existing folders when the fit is weak.

### Staging Rules

Use staging folders when a reusable item is interesting but its long-term parent
is unclear:

- `Concepts/Emerging Concepts/` - cross-cutting ideas, assumptions, phenomena,
  failure modes, application ideas, or theory concepts.
- `Methods/Emerging Methods/` - algorithms, training procedures, losses,
  architectures, data pipelines, evaluation techniques, or implementation
  patterns.
- `Metrics/Emerging Metrics/` - measures whose task context, unit, direction,
  or interpretation is not yet established by existing notes.
- `Domains/Emerging Domains/` - application domains, industries, materials,
  sensor contexts, deployment environments, or use settings that do not yet fit
  the stable `Domains/` taxonomy.
- `Learning Paradigms/Emerging Learning Paradigms/` - learning setups or
  supervision regimes that do not yet fit the stable `Learning Paradigms/`
  taxonomy.

Every staged note needs frontmatter:

```yaml
status: emerging
concept_type: method | metric | dataset | benchmark | task | domain | learning_paradigm | concept | other
candidate_parent: "Methods/Example Method Family"
source_papers:
  - "[[Paper Title]]"
evidence_count: 1
```

Use a candidate parent that matches the staged type, such as
`Methods/Example Method Family`, `Metrics/Example Metric Family`,
`Domains/Example Domain`, or `Learning Paradigms/Example Paradigm`. Use
`candidate_parent: "not clear"` when the route is genuinely uncertain.

### Emerging Item Connections

Every new staged note must be connected before the paper is considered
processed:

1. Link the paper to the staged note from frontmatter and from the `Connections`
   section using the right relation type, such as `Shares method`, `Shares
   metric`, `Application/domain`, or `Related concept`.
2. Add the paper to the staged note's `source_papers` frontmatter and to
   `## Used In These Papers` with a one-line reason grounded in the paper.
3. Link the staged note to at least one existing stable hub when a plausible
   parent or neighbor exists, for example a method family, metric family, task,
   domain, dataset, benchmark, or broader concept. If none exists, write
   `candidate_parent: "not clear"` and add a `not reported` or `not clear`
   note under `## Related Concepts`.
4. Link related staged notes to each other when they share the same paper,
   task, domain, method family, metric family, or dataset.
5. Update the relevant folder index note, such as
   `Metrics/Emerging Metrics/Emerging Metrics.md`, with a wikilink to the
   staged note.
6. Add reciprocal backlinks only for important relations: update stable hub
   notes when the staged item is central to the paper or likely to recur.
7. Do a final missing-link check for every newly added wikilink.

### Graph Completion Checklist

Before marking a paper processed, verify the graph is complete:

1. Frontmatter and the `Connections` section both link the supported graph
   hubs: task, method/model, dataset or domain, metrics when evaluated,
   benchmarks when applicable, and related papers when supported.
2. Dataset links point to dataset notes under `Datasets/Public`,
   `Datasets/Private`, or `Datasets/Availability Unspecified` based only on reported
   availability.
3. Every dataset note is linked to exactly one supported domain note when
   possible. Use a single `domain` or `related_domain` value for dataset notes,
   never `domains`, `related_domains`, or multiple links in one domain field.
   If the dataset covers more than one industry, application area, material
   class, or sensor/use context, route it only to
   `[[Multi-Industry Anomaly Detection]]` and remove links from narrower domain
   notes' `## Related Datasets` sections.
4. Dataset notes created from web hosts include the canonical host URL in
   frontmatter and body prose. Dataset notes should also point to the most
   relevant paper that introduces the dataset when one exists, using an internal
   paper wikilink when available and an external URL otherwise. Domain notes
   include both `## Related Datasets` and `## Related Papers`.
   Related datasets should show availability by linking to notes under
   `Datasets/Public`, `Datasets/Private`, or `Datasets/Availability Unspecified`; related
   papers should link to the paper notes that support the domain association.
5. Task links point to reusable task notes, not just keywords in prose.
6. Baselines and compared architectures are linked as method/model notes when
   they are important to the evaluation.
7. Architectures and model families live under `Methods/Models/`; optimizers
   live under `Methods/Optimizers/`; procedures, losses, pipelines,
   augmentation, and synthesis live under non-model `Methods/` folders.
8. Paper-to-paper links use explicit relationship types such as `Builds on`,
   `Contrasts with`, `Shares dataset`, `Shares method`, `Shares task`, `Shares
   metric`, or `Follow-up reading`.
9. Code, data, and artifact availability are recorded in frontmatter and linked
   to dataset, method, or benchmark notes when they are reusable graph notes.
10. New graph notes include aliases for common spellings, acronyms, and
   source-specific names to prevent duplicate notes.
11. Emerging notes are not orphaned: they link to the source paper, plausible
   stable hubs, related staged notes, and their folder index.
12. If the paper note was updated, related graph notes have been reviewed and
   refreshed: datasets, tasks, domains, methods, metrics, benchmarks, artifacts,
   and important paper-to-paper links all reflect the updated source-backed
   content.
13. The final note does not contain shallow-extraction placeholders such as
   `concise extraction`, `not fully extracted`, `not fully reported`, or generic
   boilerplate where the preprocessed source contains concrete facts.
14. Run the audit script and resolve missing wikilinks:

```bash
python3 tools/skills/paper-processing/scripts/graph_audit.py
```

### Promotion Rules

Promote a staged note into a stable folder when one of these is true:

- it appears in three or more paper notes
- it anchors several meaningful links from papers, methods, datasets, metrics,
  or domains
- it is central to a paper's contribution or evaluation
- it clearly belongs to an existing stable folder after reading the source
- several related staged notes imply a useful new subfolder

When promoting, update `status: promoted`, move the note to the stable folder,
preserve aliases, and fix incoming links only when Obsidian does not resolve the
move automatically. Do not create a new top-level folder for a single concept;
prefer a staged note or a second-level folder under an existing stable area.

### Periodic Taxonomy Review

After every 10-20 paper notes, review staged notes:

1. Count repeated concepts, methods, datasets, tasks, metrics, and domains.
2. Merge near-duplicates into one canonical note.
3. Promote repeated or central items.
4. Create new subfolders only when multiple promoted notes share a natural parent.
5. Leave weak, one-off, or ambiguous items staged.

## Type-Specific Focus

For **research papers**, emphasize hypothesis, method, baselines, ablations, results, and whether conclusions follow from evidence.

For **review/survey papers**, emphasize scope, taxonomy, inclusion criteria, organizing dimensions, consensus claims, disagreements, and gaps.

For **dataset/benchmark papers**, emphasize data source, collection process, annotation protocol, task definition, splits, metrics, licensing, leakage risks, bias, maintenance, and baseline results.

For **ML/deep learning papers**, always check:

- task formulation and input/output assumptions
- architecture, model family, components, and parameter counts if reported
- training objective, losses, regularization, and optimization setup
- datasets, preprocessing, augmentation, synthetic data, and splits
- evaluation protocol, used performance metrics, statistical significance, and uncertainty if reported
- baseline strength and implementation fairness
- ablations isolating the claimed contribution
- compute, hardware, training time, inference cost, and reproducibility artifacts

For **systems papers**, also extract latency, throughput, memory, scaling
behavior, hardware/software stack, deployment assumptions, failure modes, and
cost trade-offs.

For **data synthesis / augmentation papers**, explicitly extract what is
synthetic, how it is generated, how it is mixed with real data, whether leakage
is possible, and which metrics improve because of synthesis.

## Structured Fields To Capture

Capture these as frontmatter where possible and in sections where detail is
needed:

- Identification: `title`, `aliases`, `paper_key`, `doi`, `arxiv`, `url`, `pdf`, `source_file`.
- Bibliographic: `authors`, `year`, `venue`, `affiliations`, `paper_type`.
- Topics: `topics`, `tasks`, `domains`, `application_area`, `problem_type`.
- ML/DL: `model_family`, `architectures`, `methods`, `losses`, `optimizers`, `training_regime`, `pretraining`, `fine_tuning`, `augmentation`, `synthetic_data`.
- Data: `datasets`, `dataset_sizes`, `splits`, `labels`, `modalities`, `data_sources`, `licenses`, `url`.
- Evaluation: `metrics`, `baselines`, `benchmarks`, `evaluation_protocol`, `ablations`, `statistical_tests`.
- Performance metrics: record every metric used, its unit/direction, exact definition if nonstandard, primary metric, secondary metrics, and which dataset/task/result table each metric belongs to.
- Efficiency: `parameters`, `compute`, `hardware`, `training_time`, `inference_cost`, `latency`, `throughput`.
- Reproducibility: `code`, `data`, `environment`, `seeds`, `hyperparameters`, `artifact_status`.
- Graph: `related_papers`, `related_concepts`, `related_methods`, `related_datasets`, `related_domains`, `related_tasks`, `related_benchmarks`.
- Processing: `status`, `processed_at`, `preprocessed_input`, `extracted_text`, `note_created`.

## Writing Rules

- Ground every extracted fact in the actual paper/source text or explicit paper
  metadata. Do not fill gaps from memory or model training data.
- Distinguish `claimed`, `shown`, and `inferred`.
- Prefer concrete numbers over vague comparative language.
- Treat used performance metrics as mandatory when applicable. If a paper evaluates a model, dataset, benchmark, or system, record the metric names, units, direction (`higher is better` / `lower is better`), primary metric, and reported values. If no metric is reported, write `not reported`.
- If a detail is absent, write `not reported` rather than guessing.
- For dataset notes sourced from Kaggle, GitHub, DataPort, Zenodo, Hugging Face,
  or similar hosts, preserve the host URL exactly and separate source anchors
  from subject prose. Also record the most relevant paper that introduces the
  dataset when one exists; if no introducing paper is reported, write
  `not reported`.
- If a field or section is irrelevant to the paper type, write `not applicable`.
- Keep direct quotes short and only when exact wording matters.
- Do not use vault-relative metacommentary in generated notes. Avoid phrases
  such as `in this vault`, `used here`, `this note`, `processed papers`, `graph
  node`, `curation`, `manifest`, or `intake`; use subject-facing phrasing.
- Use `[[wikilinks]]` for internal concepts and papers; use markdown links for external URLs.
- Prefer wikilinks inside frontmatter list values for graph-facing fields when
  Obsidian supports them, for example `metrics: ["[[AU-ROC]]"]` or
  `optimizers: ["[[AdamW]]"]`.
- Preserve uncertainty: mark unresolved items under `Questions` instead of smoothing them away.
- Do not treat frontmatter tags as a substitute for graph links. Tags classify;
  wikilinks connect.
- Avoid orphan paper notes. Every processed paper note should link to at least
  three meaningful graph notes when the source supports them: usually a task, a
  dataset/domain, and a method or related paper.

## Source Integrity

- Do not invent citations, authors, venues, datasets, metrics, results, code
  links, limitations, or claims.
- Do not infer unstated implementation details because they are common in the
  field.
- Do not use general knowledge to "complete" missing equations, baselines,
  hyperparameters, dataset sizes, or metric definitions.
- Mark uncertain interpretations explicitly as `inferred` and explain what text
  supports the inference.

## Suggested Folder Organization

Use this structure unless the user or existing folder conventions indicate otherwise:

```text
Bases/
Canvases/
Papers/
  Research/
    <Year> - <Short Title>.md
  Dataset/
  Review/
  Benchmark/
  Systems/
  Other/
Datasets/
  Public/
  Private/
  Availability Unspecified/
Methods/
  Emerging Methods/
  Optimizers/
  Models/
    Classical ML/
    Neural Networks/
    Transformers/
    Computer Vision Models/
    Generative Models/
    Sequence and Language Models/
    Anomaly Detection Models/
    Segmentation Models/
  Data Augmentation/
  Synthetic Data Generation/
    Learned Generative Synthesis/
    Procedural and Simulation-Based Synthesis/
  Deployment/
Learning Paradigms/
  Emerging Learning Paradigms/
  Supervised Learning/
  Unsupervised Learning/
  Self-Supervised Learning/
  Semi-Supervised Learning/
  Weakly Supervised Learning/
  Reinforcement Learning/
  Transfer Learning/
  Active Learning/
  Few-Shot Zero-Shot Learning/
Benchmarks/
Concepts/
  Emerging Concepts/
Tasks/
Metrics/
  Emerging Metrics/
  Classification/
  Detection/
  Segmentation/
  Anomaly Detection/
  Generative Quality/
  Efficiency/
Domains/
  Emerging Domains/
  Semiconductor and Electronics/
  Solar Cells and Photovoltaic/
  Metals/
  Textiles/
  Glass/
  Automotive/
  Multi-Industry Anomaly Detection/
```

Route each new note to the most specific folder supported by the paper:

- Put paper notes under `Papers/<paper_type>/`, mapping `research`,
  `dataset`, `review`, `benchmark`, `systems`, and unknown/other types to the
  matching subfolder.
- Put model-family overview notes and specific model notes under
  `Methods/Models/<model-family>/`. Use this for compact taxonomy pages such as
  `Classical ML`, `Neural Networks`, `Transformers`, `Computer Vision Models`,
  `Generative Models`, `Sequence and Language Models`, `Anomaly Detection
  Models`, and `Segmentation Models`, plus concrete model notes such as GAN,
  U-Net, or PatchCore-style anomaly models.
- Put optimizer algorithms and optimizer-family notes under
  `Methods/Optimizers/`, such as SGD, Adam, AdamW, RMSProp, momentum variants,
  learning-rate schedules when treated as standalone training methods, and
  optimizer-specific procedures. Do not put optimizers under `Methods/Models/`;
  models are architectures or model families, while optimizers are training
  procedures.
- Put non-model method notes under `Methods/` branches such as
  `Optimizers`, `Data Augmentation`, `Synthetic Data Generation`, or
  `Deployment`.
- Do not put learning paradigms under `Methods/`. Supervised, unsupervised,
  self-supervised, semi-supervised, weakly supervised, reinforcement, transfer,
  active, and few-shot/zero-shot learning belong under `Learning Paradigms/`.
- Put ordinary data augmentation methods under `Methods/Data Augmentation/`.
  Use this for transformations, perturbations, mixing strategies, and other
  augmentation policies that are not themselves full synthetic-data generators.
- Put synthetic data generation methods under `Methods/Synthetic Data Generation/`.
  Route learned model-generated synthetic data to
  `Synthetic Data Generation/Learned Generative Synthesis/`; route explicit
  rules, rendering, physics, and simulators to
  `Synthetic Data Generation/Procedural and Simulation-Based Synthesis/`.
- Put learning setup notes under the matching `Learning Paradigms/<paradigm>/`
  subfolder, for example supervised, unsupervised, self-supervised,
  semi-supervised, weakly supervised, reinforcement, transfer, active, and
  few-shot/zero-shot learning.
- Put new or unclear learning setup notes under `Learning Paradigms/Emerging
  Learning Paradigms/` when their supervision regime or paradigm family is not
  yet clear. Use the same emerging frontmatter as other staged graph notes, with
  `concept_type: learning_paradigm` when appropriate.
- Put dataset notes under `Datasets/Public`, `Datasets/Private`, or
  `Datasets/Availability Unspecified` based only on the paper, dataset host
  page, or explicit metadata source being read. If availability is missing, use
  `Availability Unspecified`. Link each dataset note to exactly one supported
  domain note when possible using a singular `domain` or `related_domain` field,
  and add a reciprocal dataset link from that one domain note. Do not use
  plural dataset-domain fields or list multiple domains.
- Dataset availability may also be supported by a dataset host page such as
  Kaggle, GitHub, IEEE DataPort, Zenodo, Hugging Face, or an institutional
  repository. When adding a dataset from a host page, route by the host's stated
  access conditions and include the canonical host URL in the dataset note's
  `url` field and `## Source` or `## Dataset Details` section. Also link the
  dataset note to the most relevant paper that introduces the dataset when one
  exists, preferably via `related_papers` or `introduced_by` frontmatter and a
  body bullet near the host source.
- Multi-industry anomaly detection datasets must only be related to
  `[[Multi-Industry Anomaly Detection]]`. If the source describes a dataset
  spanning more than one industry, application area, material class, or
  sensor/use context, do not link that dataset to each narrower domain. Preserve
  the narrower contexts in dataset prose only when source-supported, but keep
  graph-facing dataset-domain fields and reciprocal `## Related Datasets` links
  exclusive to `[[Multi-Industry Anomaly Detection]]`. If a dataset already
  appears in more than one domain note, treat that as a graph error: pick the
  one supported domain, or move the association to
  `[[Multi-Industry Anomaly Detection]]` when more than one domain is supported.
- Put domain notes under the configured domain folders. If a domain is new,
  narrow, or its stable parent is unclear, stage it under
  `Domains/Emerging Domains/` with `concept_type: domain` and a plausible
  `candidate_parent` when available.
  If a paper spans several industries, prefer `Multi-Industry Anomaly Detection`
  unless one domain is clearly primary. Domain notes must maintain a
  `## Related Datasets` section grouped or labeled by dataset availability
  (`Public`, `Private`, or `Availability Unspecified`) and a `## Related Papers` section with
  one-line rationales for papers that support the domain association.
- Put metrics under `Metrics/<metric-family>/`: classification, detection,
  segmentation, anomaly detection, generative quality, or efficiency. Create a
  dedicated metric note for every metric used by a processed paper and link it
  from `metrics` and `primary_metric` frontmatter using wikilinks. Record metric
  direction, unit, dataset/task context, and exact reported values when the
  source provides them.
- Put new or unclear metrics under `Metrics/Emerging Metrics/` when the metric
  family, direction, unit, or interpretation is not yet clear. Use frontmatter:
  `status: emerging`, `concept_type: metric`, `candidate_parent`,
  `source_papers`, and `evidence_count`. Promote it into `Metrics/<family>/`
  once its definition and routing are clear or it appears across multiple paper
  notes.
- Put benchmark notes under `Benchmarks/` when the note describes a task plus
  dataset split/protocol/metric combination, not just the dataset itself.
- Keep broad reusable ideas in `Concepts/`, task definitions in `Tasks/`,
  Obsidian Bases in `Bases/`, and canvases in `Canvases/`.
- Put uncertain but potentially reusable graph notes in the matching
  parent-scoped emerging folder, such as `Concepts/Emerging Concepts/`,
  `Methods/Emerging Methods/`, `Metrics/Emerging Metrics/`,
  `Domains/Emerging Domains/`, or `Learning Paradigms/Emerging Learning
  Paradigms/`, instead of expanding the stable taxonomy prematurely.

Use frontmatter fields consistently so Obsidian Bases can index papers later:
`title`, `aliases`, `paper_key`, `paper_type`, `year`, `venue`, `authors`,
`status`, `topics`, `tasks`, `domains`, `datasets`, `methods`, `model_family`,
`architectures`, `losses`, `optimizers`, `metrics`, `primary_metric`,
`metric_definitions`, `baselines`, `benchmarks`, `code`, `data`, `doi`, `arxiv`, `url`, `pdf`,
`data_sources`, `licenses`, `introduced_by`, `related_papers`, `related_concepts`, `related_methods`, `related_datasets`,
`related_domains`, `related_tasks`, `related_benchmarks`, `preprocessed_input`,
`extracted_text`.
