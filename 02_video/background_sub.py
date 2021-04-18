#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
from matplotlib import pyplot as plt
import numpy as np

data_path = "/home/gokhan/opencv-workshop/data/"
cap = cv2.VideoCapture(data_path+'vtest.avi')
fps = cap.get(cv2.CAP_PROP_FPS)
print(fps)

ret, base = cap.read()
base_gray = cv2.cvtColor(base, cv2.COLOR_BGR2GRAY)
while (True):

    ret, frame = cap.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    diff = frame_gray - base_gray
    base_gray = frame_gray

    new_diff = cv2.GaussianBlur(diff, (5,5), 0)

    cv2.imshow('frame', frame)
    cv2.imshow('diff', new_diff)
    delay = int(1000 / fps)
    k = cv2.waitKey(delay)
    if k == 27:
        break 

cap.release()
cv2.destroyAllWindows()