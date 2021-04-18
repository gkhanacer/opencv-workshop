#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
from matplotlib import pyplot as plt
import numpy as np

data_path = "/home/gokhan/opencv-workshop/data/"
cap = cv2.VideoCapture(data_path+'vtest.avi')
fps = cap.get(cv2.CAP_PROP_FPS)
print(fps)

fgbg = cv2.createBackgroundSubtractorMOG2()
fgbg.setDetectShadows(False)

while (True):

    ret, frame = cap.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    diff = fgbg.apply(frame_gray)

    # Get connected compenents
    image, contours, h = cv2.findContours(diff, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    new_contours = []
    for cnt in contours:
        area = cv2.contourArea(cnt)
        x, y, w, h = cv2.boundingRect(cnt)
        ratio = float(w)/h

        if area < 10 or ratio > 2.0:
            cv2.fillPoly(diff, pts=[cnt], color=(0,0,0))
        else:
            new_contours.append(cnt)
            
    frame = cv2.drawContours(frame, new_contours, -1, (0,255,0), 3) 

    kernel = np.ones((3,3), np.uint8)
    diff = cv2.erode(diff, kernel, iterations=1)

    cv2.imshow('frame', frame)
    cv2.imshow('diff', diff)
    delay = int(1000 / fps)
    k = cv2.waitKey(delay)
    if k == 27:
        break 

cap.release()
cv2.destroyAllWindows()