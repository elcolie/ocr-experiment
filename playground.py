import cv2

from fours_point import read_points, four_point_transform
from utils import get_center

DEMO_DIR = 'demo/'


def tear_down_page(image_filename: str, coords_filename: str, dir: str):
    """
    One page input has multiple texts there. This function will tear down them into
    individual strip picture
    `boxes` p1, p2, p3, p4, score
    p1,    p2
    p3,    p4
    Use p1 and p4 to crop the picture
    :param image_filename
    :param coords_filename
    :return:
    """
    im = cv2.imread(DEMO_DIR + image_filename)
    pts = read_points(coords_filename)

    idx = 0
    for pt in pts:
        wraped = four_point_transform(im, pt)
        cv2.imwrite(f'{dir}/{image_filename}-{idx}.png', wraped)
        idx += 1


def mark_center(image_filename: str, coords_filename: str):
    """

    :return:
    """
    im = cv2.imread(DEMO_DIR + image_filename)
    pts = read_points(coords_filename)
    center_pts = get_center(pts)
    for pt in center_pts:
        point = int(pt[0]), int(pt[1])
        cv2.circle(im, point, 10, (0, 0, 255), -1)
    cv2.imwrite(f'mark-center.png', im)


if __name__ == '__main__':
    # tear_down_page('p23-181.png', 'res/p23-181.txt', 'cropped_sentences')
    mark_center('p23-181.png', 'res/p23-181.txt')
