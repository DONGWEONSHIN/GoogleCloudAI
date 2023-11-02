# OS : Windows-10-10.0.22621-SP0
# Python : 3.8.18
# cv2 : 4.8.1
# Created: NOV. 01. 2023
# Author: D.W. SHIN

import numpy as np
import cv2
import os


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


def on_mouse(event, x, y, flags, param):
    print("x={}, y={}".format(x, y))



# 파일 가져오기
FILE_BASE = 'edu/deep_learning/'
SAVE_DIR = os.path.join(FILE_BASE, 'dataset/')
VIDEO_PATH = os.path.join(FILE_BASE,'data/project_video.mp4')

os.makedirs(SAVE_DIR, exist_ok=True)
cap = cv2.VideoCapture(VIDEO_PATH)

frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
frame_fps = int(cap.get(cv2.CAP_PROP_FPS))



# 메인 함수
frameNum = 0
while True:
    retval, frame = cap.read()
    if not retval:
        break

    cv2.imshow('frame', frame)
    
    key = cv2.waitKey(25)
    if key == 27:
        break
    
    if frameNum % frame_fps == 0:
        fileName = os.path.join(SAVE_DIR, 'video' + str(frameNum) + '.jpg')
        cv2.imwrite(fileName, frame, [cv2.IMWRITE_JPEG_QUALITY, 90])
        
        img_shape = frame.shape

        vertices = np.array([[(100, img_shape[0]),
                            (530, 460),
                            (772, 460),
                            (img_shape[1]-20, img_shape[0])]], dtype=np.int32)

        mask = region_of_interest(frame, vertices)
        cv2.imshow("mask",mask)
        cv2.namedWindow('mask')
        cv2.setMouseCallback('mask', on_mouse, mask)
        
        mask_hsv = cv2.cvtColor(mask, cv2.COLOR_BGR2HSV)
        
        yellow = cv2.inRange(mask_hsv, (18, 150, 0), (24, 255, 255))
        white = cv2.inRange(mask_hsv, (0, 0, 135), (179, 24, 255))
        cv2.imshow("yellow", yellow)
        cv2.imshow("white", white)
        
        mask_all = cv2.add(yellow, white)
        cv2.copyTo(frame, mask, yellow)
        cv2.copyTo(frame, mask, white)
        cv2.imshow('mask_all', mask_all)
        
        
    frameNum += 1

if cap.isOpened():
    cap.release()
    
cv2.destroyAllWindows()

