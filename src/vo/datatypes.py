"""Shared data structures passed between modules (no logic, only containers)."""

# TODO: use @dataclass(frozen=True, slots=True); numpy arrays inside, shapes in comments
# TODO: Features: keypoints (M,2) pixels, descriptors (M,D) or None
# TODO: PairMatches: i, j (frame ids), pts1 (N,2), pts2 (N,2) pixels
# TODO: Correspondences: x1, x2 (N,3) calibrated homogeneous points
# TODO: EstimationResult: E, R, t (unit), inliers mask, diagnostics (cond(A), sigma ratio)
# TODO: SyntheticScene: x1, x2 (calibrated), R, t
# TODO: PairRecord: one evaluation row (i, j, e_R, e_t, n_matches, n_inliers, cond_A, sigma_ratio, time)
