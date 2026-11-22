"""Cache matches so all estimators run on identical input."""

# TODO: file layout: data/matches/<run-id>/<sequence>/<extractor>_<matcher>_step<k>.npz, run-id = UTC timestamp like 20261122T141600Z
# TODO: use PairMatches from vo.structures
# TODO: store RAW pixel coordinates (not undistorted): the cache stays independent of the camera calibration,
#       so the same file can be run with and without undistortion (pixel-coordinate experiment); undistortion is done later in `estimate`
# TODO: save_matches(path, sequence, pairs, meta); meta includes seed and extractor/matcher params
# TODO: load_matches(path) -> sequence, pairs, meta
