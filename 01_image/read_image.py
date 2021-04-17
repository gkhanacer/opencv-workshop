import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys

# READ IMAGE
data_path = "../data/"
img = cv2.imread(data_path + "starry_night.jpg")

if img is None:
    sys.exit("Could not read the image.")

cv2.imshow("Display window", img)
k = cv2.waitKey(0)

if k == ord("s"):
    cv2.imwrite("starry_night.png", img)


