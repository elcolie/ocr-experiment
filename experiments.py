import numpy as np
from PIL import Image


def find_horizontal_boundary(data):
    """
    Vertical sum and find the boundary
    Find the boundary by if-else condition
    :param data:
    :return:
    """
    (height, width, channel) = data.shape
    vertical_sum = np.sum(data, axis=0)
    three_zeros = np.array([0, 0, 0], dtype=np.int)
    vertical_bool = np.all(vertical_sum == three_zeros, axis=1)
    left = 0
    right = width
    for i in range(0, vertical_bool.shape[0] - 1):
        if (vertical_bool[i] == True) and (vertical_bool[i + 1] == False):
            # tl, bl
            left = i + 1
        elif (vertical_bool[i] == False) and (vertical_bool[i + 1] == True):
            # tr, br
            right = i
    return left, right


def remove_horizontal_edges(data):
    """
    return selected data
    :param data: shaped data
    :return:
    """
    left, right = find_horizontal_boundary(data)
    return data[:, left:right]


def main():
    w, h = 10, 5
    data = np.zeros((h, w, 3), dtype=np.uint8)

    data[:, 2:8] = [255, 255, 255]  # white squares on the left & right
    data[3, 3] = [255, 0, 0]  # red dot

    data = remove_horizontal_edges(data)

    img = Image.fromarray(data, 'RGB')
    img.show()


if __name__ == '__main__':
    main()
