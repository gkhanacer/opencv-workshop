#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2

data_path = "/home/gokhan/opencv-workshop/data/"

img1 = cv2.imread(data_path + "ml.png")
img2 = cv2.imread(data_path + "opencv-logo.png")

# Get width and height of image
shape = img1.shape # (row/height, column/width, channel)
width = shape[1]
height = shape[0]

# Resize
dst = cv2.resize(img2, (width, height))

new_image = cv2.addWeighted(img1, 0.8, dst, 0.2, 0)

cv2.imshow("img1", img1)
cv2.imshow("dst", dst)
cv2.imshow("new_image", new_image)
k = cv2.waitKey(0)

cv2.destroyAllWindows()

