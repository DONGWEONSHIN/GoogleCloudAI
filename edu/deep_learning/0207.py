# 0207.py
import cv2
import os
##cap = cv2.VideoCapture(0)  # 0번 카메라
cap = cv2.VideoCapture('./data/vtest.avi')
##cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
##cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
              int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print('frame_size =', frame_size)
print('frame count=', frame_count)

frameNum = 0

dataPath = './dataset/'
os.makedirs(dataPath, exist_ok=True)

while True:   
    retval, frame = cap.read() # 프레임 캡처
    if not retval:
        break

    cv2.imshow('frame',frame)
    
    key = cv2.waitKey(25)
    if key == 27: # Esc
        break
    if frameNum%30==0:
        # 파일명 : dataset+'frameNum'.jpg
        filename = os.path.join(dataPath, 'dataset'+str(frameNum)+'.jpg')
        #print(filename)
        cv2.imwrite(filename,frame, [cv2.IMWRITE_JPEG_QUALITY, 90])
    frameNum +=1


if cap.isOpened():
    cap.release()
cv2.destroyAllWindows()
