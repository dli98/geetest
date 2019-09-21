# 模板匹配
import cv2
from matplotlib import pyplot as plt


def get_gap(img, template):
    img = cv2.split(img)[2]
    template = cv2.split(template)[2]
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = min_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(img, top_left, bottom_right, 255, 2)

    return top_left[0]


if __name__ == '__main__':
    img = cv2.imread("Image/data_image.jpg")
    template = cv2.imread("Image/data_image_bg.jpg")
    distance = get_gap(img, template)
    print(distance)




