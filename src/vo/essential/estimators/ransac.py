"""RANSAC wrapper (by 21 Dec)."""

# TODO: @ESTIMATORS.register('ransac') Ransac(EssentialEstimator) wrapping an inner estimator
# TODO: take rng (from config.make_rng) in __init__, never use the global numpy RNG
# TODO: adaptive K = ln(1-p)/ln(1-w^8), epipolar error threshold, final re-estimation from inliers
