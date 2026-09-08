PYTHON ?= python
PYTHONPATH := tools/src

.PHONY: export export-check validate test check reproduce website-check

export:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m inspection_evidence.cli export

export-check:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m inspection_evidence.cli export --check

validate:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m inspection_evidence.cli validate

test:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m unittest discover -s tools/tests -v

reproduce: export validate test

check: validate export-check test

website-check:
	cd website && pnpm lint && pnpm typecheck && pnpm test && pnpm build
