import cv2
import numpy as np


def order_points(points):
    s = points.sum(axis=1)
    diff = np.diff(points, axis=1)

    ordered_points = np.zeros((4, 2), dtype="float32")

    ordered_points[0] = points[np.argmin(s)]
    ordered_points[2] = points[np.argmax(s)]
    ordered_points[1] = points[np.argmin(diff)]
    ordered_points[3] = points[np.argmax(diff)]

    return ordered_points


def get_vectors(image, points, count):
    with np.load('webcam_calibration_ouput.npz') as X:
        mtx, dist, _, _ = [X[i] for i in ('mtx', 'dist', 'rvecs', 'tvecs')]
    mtx[0, 0] = 720
    mtx[1, 1] = 720
    mtx[0, 2] = image.shape[1] / 2 - image.shape[1] / 300 * count
    mtx[1, 2] = image.shape[0] / 2

    imgp = np.array(points, dtype="float32")

    objp = np.array([[0.5, 0., 0], [0.5, 0., 1], [-0.5, 0., 1], [-0.5, 0., 0]], dtype="float32")

    _, rvecs, tvecs = cv2.solvePnP(objp.reshape(-1, 1, 3), imgp.reshape(-1, 1, 2), mtx, dist)

    return rvecs, tvecs
