import cv2
import numpy as np

from fours_point import order_points


def get_center(pts):
    """
    Get center coords from given 4 points
    For loop version
    :return:
    """
    return np.sum(pts, axis=1) / 4.0


def customized_four_point_transform(image, pts, factor: float = 0.05):
    """

    :param image:
    :param pts:
    :return:
    """
    # obtain a consistent order of the points and unpack them
    # individually
    rect = order_points(pts)

    # ---->x
    # |
    # |
    # V y
    (raw_tl, raw_tr, raw_br, raw_bl) = rect

    center_pt = np.sum(rect, axis=0) / 4.0

    # pointing vector from center to tl
    center_to_tl = raw_tl - center_pt
    # pointing vector from center to tr
    center_to_tr = raw_tr - center_pt
    # pointing vector from center to br
    center_to_br = raw_br - center_pt
    # pointing vector from center to bl
    center_to_bl = raw_bl - center_pt

    tl = center_to_tl * factor + raw_tl
    tr = center_to_tr * factor + raw_tr
    br = center_to_br * factor + raw_br
    bl = center_to_bl * factor + raw_bl

    # compute the width of the new image, which will be the
    # maximum distance between bottom-right and bottom-left
    # x-coordiates or the top-right and top-left x-coordinates
    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))

    # compute the height of the new image, which will be the
    # maximum distance between the top-right and bottom-right
    # y-coordinates or the top-left and bottom-left y-coordinates
    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))

    # now that we have the dimensions of the new image, construct
    # the set of destination points to obtain a "birds eye view",
    # (i.e. top-down view) of the image, again specifying points
    # in the top-left, top-right, bottom-right, and bottom-left
    # order
    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype="float32")

    # compute the perspective transform matrix and then apply it
    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))

    # return the warped image
    return warped
