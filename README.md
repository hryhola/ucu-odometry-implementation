# UCU odometry implementation

Monocular visual odometry for drone footage (UZH-FPV dataset). For each pair of frames we match features,
build the N×9 matrix A from the matches, find the essential matrix E as the smallest right singular vector
(SVD), and factor it into the relative rotation R and the translation direction t. We compare the plain
eight-point algorithm, the Hartley-normalized one, and RANSAC against the ground truth.
Details and math: [CONTEXT.md](CONTEXT.md).

> Status: project skeleton. Files contain TODOs, the commands below describe the intended usage.

## Setup

Put the dataset in `data/The UZH FPV Dataset/` (it is not tracked by git), then:

```
make init        # uv sync + create data/matches, data/results, notebooks
```

`make install` only runs `uv sync`, `make dirs` only creates the folders.

## Usage

The pipeline has two stages, so all estimators run on exactly the same matches.

```
make features    # 1. detect + match features, save matches to data/matches/<run-id>/
make estimate    # 2. run estimators on the matches, save metrics and figures to data/results/<run-id>/
make synthetic   # estimators on synthetic scenes with known (R, t) and noise
make list        # show registered extractors, matchers, estimators
```

Settings are Makefile variables and can be overridden on the command line:

```
make features SEQS="indoor_forward_5 indoor_45_12" EXTRACTOR=sift MATCHER=flann STEP=2
make estimate ESTIMATORS="plain normalized ransac"
make estimate MATCHES=data/matches/20261122T141600Z    # default: newest matches folder
```

| Variable | Default | Meaning |
|---|---|---|
| `SEQS` | 3 indoor sequences | sequences to process |
| `EXTRACTOR`, `MATCHER` | `orb`, `bf` | feature algorithm and matcher |
| `STEP` | `3` | frame gap inside a pair |
| `MAX_PAIRS` | `200` | pairs per sequence |
| `ESTIMATORS` | `plain` | one or several estimators |
| `SEED` | `42` | seed for every random generator |
| `MATCHES` | newest | matches folder for `estimate` |

The same commands work without `make`: `uv run vo features|estimate|synthetic|list --help`.

## Layout

```
src/vo/
  data/         camera model, UZH-FPV loader, synthetic scenes
  features/     base classes + extractors/ and matchers/ + matches cache
  essential/    A matrix, E decomposition, estimators (plain, normalized, ransac)
  evaluation/   metrics, trajectory, plots
data/matches/   cached matches, one timestamped folder per run (git-ignored)
data/results/   metrics/ and figs/ per run, folder named by timestamp, e.g. 20261122T141600Z
notebooks/      experiments, presets and pipelines 
```

## Adding a new method

Subclass the base class (`FeatureExtractor`, `FeatureMatcher` or `EssentialEstimator`) in a new file in the
matching folder and register it with `@REGISTRY.register("name")`. It then appears in `make list` and can be
selected with `EXTRACTOR=`, `MATCHER=` or `ESTIMATORS=`.

## Data

Link to Google Drive with data: https://drive.google.com/drive/folders/1387Y6vx0V5gaX76389Se8x_WXD4yq8U5?usp=drive_link