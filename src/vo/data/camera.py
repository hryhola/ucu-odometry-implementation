"""Fisheye camera: loads the dataset intrinsics and undistorts points."""

# TODO: FisheyeCamera: holds K (from [fx, fy, cx, cy]), equidistant distortion coeffs (4), resolution
# TODO: from_yaml(path, cam='cam0') using pyyaml (left camera only)
# TODO: from_sequence(data_root, sequence_name): pick the calibration folder by name,
#       e.g. indoor_forward_5 -> indoor_forward_calib_snapdragon/.../camchain-..*_cam.yaml (camera-only file);
#       intrinsics differ slightly between calibration folders, so never share one set across all sequences
# TODO: undistort_points(pts_px (N,2)) -> (N,3) calibrated homogeneous coords (cv2.fisheye.undistortPoints)
