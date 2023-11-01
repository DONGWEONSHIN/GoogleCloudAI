import cv2
import sys
import numpy as np


imgPath = './data/lena.jpg'
imgPath2 = './data/2560x1440.jpg'
imgBGR = cv2.imread(imgPath)
imgBGR2 = cv2.imread(imgPath2)

if imgBGR is None:
    print('Image Load Fail!')
    sys.exit()

imgResize = cv2.resize(imgBGR2,(1280,720))
imgResize2 = cv2.resize(imgBGR2, dsize=(0,0), fx=0.7, fy=0.4)

print(imgBGR.shape)


cv2.imwrite('./data/1280_720.jpg', imgResize, [cv2.IMWRITE_JPEG_QUALITY, 95])



cv2.imshow('lenna', imgBGR)
cv2.imshow('resize', imgResize)
cv2.imshow('resize2', imgResize2)
key = cv2.waitKey(0)
cv2.destroyAllWindows()





