# OS : Windows-10-10.0.22621-SP0
# Python : 3.8.18
# cv2 : 4.8.1
# Created: NOV. 01. 2023
# Author: D.W. SHIN

import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import sys


def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    
    if len(img.shape) > 2:
        channel_count = img.shape[2]
        ignore_mask_color = (255,) * channel_count
    else:
        ignore_mask_color = 255
        
    cv2.fillPoly(mask, vertices, ignore_mask_color)
    
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image


FILE_BASE = 'edu/deep_learning/'
FILE_PATH = os.path.join(FILE_BASE,'dataset/video100.jpg')

src = cv2.imread(FILE_PATH)

if src is None:
    print('Image Load Failed!')
    sys.exit()

img_shape = src.shape

vertices = np.array([[(100, img_shape[0]),
                      (450, 320),
                      (550, 320),
                      (img_shape[1]-20, img_shape[0])]], dtype=np.int32)

mask = region_of_interest(src, vertices)

# plt.figure(figsize=(10,8))
# plt.imshow(mask, cmap='gray')
# plt.show()

src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
mask_hsv = cv2.cvtColor(mask, cv2.COLOR_BGR2HSV)

dst = cv2.inRange(mask_hsv, (18, 150, 0), (24, 255, 255))
dst_white = cv2.inRange(mask_hsv, (0, 0, 135), (179, 24, 255))

mask_all = cv2.add(dst, dst_white)

cv2.copyTo(src, mask, dst)

cv2.imshow('src', src)
cv2.imshow('mask', mask)
cv2.imshow('dst', dst)

cv2.copyTo(src, mask, dst_white)

cv2.imshow('dst_white', dst_white)
cv2.imshow('dst_mask_all', mask_all)

cv2.waitKey()
cv2.destroyAllWindows()

