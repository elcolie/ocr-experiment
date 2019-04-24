import cv2

from utils import read_points, four_point_transform

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


if __name__ == '__main__':
    tear_down_page('p23-181.png', 'res/p23-181.txt', 'cropped_sentences')
    # convert_object(cv2.imread('perspective_transform/Original.png'), isDebug=True)
