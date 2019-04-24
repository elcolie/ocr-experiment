import numpy as np


def get_center(pts):
    """
    Get center coords from given 4 points
    For loop version
    :return:
    """
    return np.sum(pts, axis=1) / 4.0
