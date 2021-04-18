#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import sys

data_path = "/home/gokhan/opencv-workshop/data/"
img = cv2.imread(data_path + "starry_night.jpg")

if img is None:
    sys.exit("Couldn't read image.")

cv2.imshow("window", img)
k = cv2.waitKey(0)

if k == ord("s"):
    cv2.imwrite("test.png",img)