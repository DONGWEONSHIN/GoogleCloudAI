import cv2
import sys

imgPath = './data/cannyTest.png'

imgGray = cv2.imread(imgPath, cv2.IMREAD_GRAYSCALE)

if imgGray is None:
    print("Load is Fail!!!")
    sys.exit()

imgCanny = cv2.Canny(imgGray, 140, 192)

cv2.imshow('org', imgGray)
cv2.imshow('canny', imgCanny)
cv2.waitKey(0)

cv2.destroyAllWindows()