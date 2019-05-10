import unittest

import numpy as np

from experiments import find_horizontal_boundary


class TestFilter(unittest.TestCase):
    def setUp(self):
        w, h = 10, 5
        self.data = np.zeros((h, w, 3), dtype=np.uint8)

        self.data[:, 2:8] = [255, 255, 255]  # white squares on the left & right
        self.data[3, 3] = [255, 0, 0]  # red dot

    def test_get_index(self):
        """
        Do a vertical sum and get the boundary indexes
        :return:
        """
        ans = find_horizontal_boundary(self.data)
        assert 2, 7 == ans


if __name__ == '__main__':
    unittest.main()
