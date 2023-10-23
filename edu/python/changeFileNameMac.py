# Python : 3.9.18
# Numpy : 1.26.0
# Pandas : 2.1.1
# Matplotlib : 3.7.2
# Seaborn : 0.12.2
# Scikit-learn : 1.3.0
# Created: OCT. 11. 2023
# Author: D.W. SHIN
# Mac에서 파일명 변환하기

import os

filePath = '/Users/dongweonshin/Downloads/cats'

fileList = os.listdir(filePath)

for i, file in enumerate(fileList):
    preName = os.path.join(filePath, file)
    fileName = os.path.splitext(file)

    newFileName = "CAT" + str(i) + fileName[1]

    postName = os.path.join(filePath, newFileName)

    os.rename(preName, postName)
    
