SEED       ?= 42
SEQS       ?= indoor_forward_5 indoor_forward_6 indoor_45_12
EXTRACTOR  ?= orb
MATCHER    ?= bf
STEP       ?= 3
MAX_PAIRS  ?= 200
ESTIMATORS ?= plain

RUN_ID       ?= $(shell date -u +%Y%m%dT%H%M%SZ)
RUN_ID       := $(RUN_ID)

MATCHES_RUN  ?= $(shell ls -1 data/matches 2>/dev/null | grep -E '^[0-9]{8}T[0-9]{6}Z$$' | sort | tail -1)

.PHONY: init install dirs features estimate synthetic list clean

init: install dirs

install:
	uv sync

dirs:
	mkdir -p data/matches data/results notebooks

list:
	uv run vo list

features:
	for seq in $(SEQS); do \
		uv run vo features --sequence $$seq --extractor $(EXTRACTOR) --matcher $(MATCHER) --step $(STEP) --max-pairs $(MAX_PAIRS) --seed $(SEED) --run-id $(RUN_ID) || exit 1; \
	done

estimate:
	@test -n "$(MATCHES_RUN)" || { echo "no matches in data/matches, run 'make features' first"; exit 1; }
	for seq in $(SEQS); do \
		uv run vo estimate --matches data/matches/$(MATCHES_RUN)/$$seq/$(EXTRACTOR)_$(MATCHER)_step$(STEP).npz --estimator $(ESTIMATORS) --plot --seed $(SEED) --run-id $(RUN_ID) || exit 1; \
	done

synthetic:
	uv run vo synthetic --estimator $(ESTIMATORS) --noise 0 0.5 1 2 --n-points 200 --trials 100 --seed $(SEED) --plot --run-id $(RUN_ID)

clean:
	find . -name __pycache__ -not -path "./.venv/*" -exec rm -rf {} +
