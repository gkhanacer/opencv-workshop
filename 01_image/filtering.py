#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
from matplotlib import pyplot as plt
import numpy as np

data_path = "/home/gokhan/opencv-workshop/data/"
img1 = cv2.imread(data_path + "messi5.jpg", 0)

kernel = np.ones((9,9), np.float32)/ 81 # smoothing
kernel2 = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]]) #sharper

dst = cv2.filter2D(img1, -1, kernel)
dst2 = cv2.filter2D(img1, -1, kernel2)

cv2.imshow("img1", img1)
cv2.imshow("dst", dst)
cv2.imshow("dst2", dst2)
k = cv2.waitKey(0)

cv2.destroyAllWindows()
