"""argparse entry point: `vo features | estimate | synthetic | list`."""

# TODO: run id is generated in code only (no CLI flag, not in Makefile): UTC timestamp %Y%m%dT%H%M%SZ (e.g. 20261122T141600Z, no '-' or ':'); one helper creates it once per command invocation and it names the output folder (matches or results)
# TODO: every subcommand gets --seed (default config.DEFAULT_SEED = 42), passed to config.make_rng
# TODO: main(argv=None): build parser, dispatch to subcommand
# TODO: features: --sequence (one or many, all go into the same run folder) --data-root --extractor --matcher --step --max-pairs --out (default data/matches; files go to <out>/<run-id>/<sequence>/)
# TODO:   -> load sequence, create extractor+matcher from registries, loop over pairs (i, i+step), save matches via features.store
# TODO:   -> NO undistortion here: detect and match on the original (distorted) images, save RAW pixel coordinates
# TODO: estimate: --matches (optional, the only way to choose a run: path to a data/matches/<run-id> folder, default = newest; processes every .npz in it) --data-root --estimator (many) --plot (flag) --out (default data/results; writes into <out>/<new run-id>/metrics and <out>/<new run-id>/figs)
# TODO:   -> order: load raw-pixel matches -> undistort points (data.camera) -> estimate E; undistortion must happen BEFORE estimation
# TODO:   -> then GT (data.uzh_fpv), run each estimator; collect per-pair info (e_R, e_t, n_matches, n_inliers, cond_A, sigma_ratio, time) as PairRecord (vo.datatypes) and pass it to evaluation.metrics to reuse (summaries, plots, saving to data/results/<run-id>/metrics); do not compute or print stats inside cli.py
# TODO: synthetic: --estimator (many) --noise (many) --n-points --outlier-ratio --trials --seed --plot (flag); same results folder layout as estimate
# TODO:   -> generate scenes (data.synthetic), run estimators, aggregate errors, optional error-vs-noise plot
# TODO: list: print registered extractors, matchers, estimators
# TODO: use registry names as argparse choices
