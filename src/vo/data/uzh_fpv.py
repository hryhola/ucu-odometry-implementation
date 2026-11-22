"""UZH-FPV sequence loader."""

# TODO: UZHSequence(root, name): parse left_images.txt and groundtruth.txt, build FisheyeCamera via data.camera
# TODO: __len__, image(i) grayscale
# TODO: gt_pose_cam(timestamp): interpolate GT (lerp t, slerp quaternion) at the frame timestamp
# TODO: decide how the GT frame relates to the camera frame (fixed offset?) before comparing R*, t* with estimates
# TODO: relative_gt(i, j) -> (R*, unit t*)
