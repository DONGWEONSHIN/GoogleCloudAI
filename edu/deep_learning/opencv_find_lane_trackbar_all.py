# OS : Windows-10-10.0.22621-SP0
# Python : 3.8.18
# cv2 : 4.8.1
# Created: NOV. 01. 2023
# Author: D.W. SHIN

import cv2
import os
import sys

def on_trackbar(pos):
    hmin = cv2.getTrackbarPos('H_min', 'dst')
    hmax = cv2.getTrackbarPos('H_max', 'dst')
    smin = cv2.getTrackbarPos('S_min', 'dst')
    smax = cv2.getTrackbarPos('S_max', 'dst')
    vmin = cv2.getTrackbarPos('V_min', 'dst')
    vmax = cv2.getTrackbarPos('V_max', 'dst')
    
    dst = cv2.inRange(src_hsv, (hmin, smin, vmin), (hmax, smax, vmax))
    cv2.imshow('dst', dst)

FILE_BASE = 'edu/deep_learning/'
FILE_PATH = os.path.join(FILE_BASE,'dataset/video100.jpg')

src = cv2.imread(FILE_PATH)

if src is None:
    print('Image Load Failed!')
    sys.exit()

src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

cv2.imshow('src', src)
cv2.namedWindow('dst')

cv2.createTrackbar('H_min', 'dst', 0, 179, on_trackbar)
cv2.createTrackbar('H_max', 'dst', 179, 179, on_trackbar)
cv2.createTrackbar('S_min', 'dst', 0, 256, on_trackbar)
cv2.createTrackbar('S_max', 'dst', 24, 256, on_trackbar)
cv2.createTrackbar('V_min', 'dst', 135, 256, on_trackbar)
cv2.createTrackbar('V_max', 'dst', 255, 256, on_trackbar)
on_trackbar(0)

cv2.waitKey()

cv2.destroyAllWindows()

