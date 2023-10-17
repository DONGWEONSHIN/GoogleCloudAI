# Python Version : Google Colab
# Created: OCT. 10. 2023
# Author: D.W. SHIN
# Google Colab을 사용하여 파일명 변경하기
# Google에 파일 혹은 폴더 마운트 필요!!

import os

filePath = '/content/drive/MyDrive/G_AI_DEV_01/data/Cats'

fileList = os.listdir(filePath)

# fileList

BASE_NAME = 'cat'
FIR_COL = '00'
SEC_COL = '0'

for i, file in enumerate(fileList):
  priName = os.path.join(filePath, file)
  extName = os.path.splitext(file)
  cntName = ''
  #print(priName)
  if i < 10:
    cntName = FIR_COL + str(i)
  elif i < 100:
    cntName = SEC_COL + str(i)
  else:
    cntName = str(i)
  
  newName = BASE_NAME + cntName + extName[1]

  postName = os.path.join(filePath, newName)
  os.rename(priName, postName)
