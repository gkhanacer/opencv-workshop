#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
from matplotlib import pyplot as plt
import numpy as np

data_path = "/home/gokhan/opencv-workshop/data/"
img = cv2.imread(data_path + "sudoku.png", 0)
img_median = cv2.medianBlur(img, 5) 

kernel = np.ones((5,5), np.float32)/ 25 # smoothing
dst = cv2.filter2D(img, -1, kernel)

_, thr1 = cv2.threshold(dst, 50, 255, cv2.THRESH_BINARY)
thr2 = cv2.adaptiveThreshold(dst, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
thr3 = cv2.adaptiveThreshold(dst, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

cv2.imshow("img", img)
cv2.imshow("img_median", dst)
cv2.imshow("thr1", thr1)
cv2.imshow("thr2", thr2)
cv2.imshow("thr3", thr3)
k = cv2.waitKey(0)

cv2.destroyAllWindows()

# [0...255]
# 0 -> siyah
# 255 -> beyaz
# arada -> grinin tonları