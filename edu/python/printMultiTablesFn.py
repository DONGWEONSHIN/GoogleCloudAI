# Python Version : 3.9
# Created: OCT. 10. 2023
# Author: D.W. SHIN
# 구구단 프린트 하기
# 가변으로 단 변경하기


# startBase = 2
# endBase = 9
# cols = 3

def howManyRows(startBase, endBase, col):
    rows = ((endBase + 1) - startBase) / col
    rest = ((endBase + 1) - startBase) % col

    rows = int(rows)

    if rest != 0:
        rows = rows + 1
    result = [rows, rest]
    return result


def dispDigit(startBase, next):
    resultStr = ""
    if startBase*next < 10:
        resultStr = " "
    return resultStr


startBase = int(input("시작 구구단을 넣으세요 : "))
endBase = int(input("마치는 구구단을 넣으세요 : "))
in_col = int(input("표현할 컬럼수를 넣으세요 : "))

rowList = howManyRows(startBase, endBase, in_col)


#initNum = 2
for i in range(rowList[0]):
    for j in range(endBase):
        col = startBase
        for k in range(in_col):
            if col > endBase:
                break
            space = " " if col*(j+1) < 10 else ""
            endStr = ""
            if k != (in_col - 1) and col != endBase:
                endStr = " " * 4
            elif col == endBase + 1:
                break
            else:
                endStr = "\n"
            print("{} X {} = %s{}".format(col, j+1, col*(j+1)) % space, end=endStr)
            col = col + 1
    print("")
    startBase = startBase + in_col
