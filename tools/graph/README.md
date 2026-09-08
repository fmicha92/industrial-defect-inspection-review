# Graph figure helpers

`generate_vault_ego_tikz.py` creates a curated TikZ view of a selected vault node. Pass repository-relative paths explicitly:

```bash
python tools/graph/generate_vault_ego_tikz.py \
  --vault evidence/graph/vault \
  --output evidence/review/publication/figures/vault_ego_graph.tex
```
