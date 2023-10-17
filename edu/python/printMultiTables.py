# Python Version : 3.9
# Created: OCT. 06. 2023
# Author: D.W. SHIN
# 구구단 프린트 하기

initNum = 2
for i in range(3):
    for j in range(9):
        col = initNum
        for k in range(3):
            space = " " if col*(j+1) < 10 else ""
            endStr = ""
            if k != 2 and col != 9:
                endStr = " " * 4
            elif col == 10:
                break
            else:
                endStr = "\n"
            print("{} X {} = %s{}".format(col, j+1, col*(j+1)) % space, end=endStr)
            col = col + 1
    print("")
    initNum = initNum + 3
