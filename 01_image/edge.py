#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
from matplotlib import pyplot as plt
import numpy as np

data_path = "/home/gokhan/opencv-workshop/data/"

img1 = cv2.imread(data_path + "messi5.jpg", 0)
edges = cv2.Canny(img1, threshold1=80, threshold2=178)

plt.subplot(121), plt.imshow(img1, cmap='gray')
plt.title("original image")
plt.subplot(122), plt.imshow(edges, cmap='gray')
plt.title("edges")
plt.show()
