# Python : 3.9.18
# Numpy : 1.26.0
# Pandas : 2.1.1
# Matplotlib : 3.7.2
# Seaborn : 0.12.2
# Scikit-learn : 1.3.0
# Created: OCT. 06. 2023
# Author: D.W. SHIN
# 별 만들기

# 1
print("1번")
for i in range(5):
    print("*", end='')


print("\n\n")


# 2
print("2번")
for i in range(5):
    print("*")


print("\n\n")


# 3
print("3번")
for i in range(5):
    print("*"*5)


print("\n\n")


# 4
print("4번")
for i in range(5):
    print("*"*(i+1))


print("\n\n")


# 5
print("5번")
for i in range(5, 0, -1):
    print("*"*i)


print("\n\n")


# 6
print("6번")
for i in range(5, 0, -1):
    print(" "*(i-1) + "*"*(6-i))


print("\n\n")


# 7
print("7번")
for i in range(5):
    print(" "*i + "*"*(5-i))


print("\n\n")


# 8
print("8번")
for i in range(5, 0, -1):
    print(" "*(i-1) + "*"*(6-i) + "*"*(5-i))


print("\n\n")


# 9
print("9번")
for i in range(5):
    print(" "*i + "*"*(5-i) + "*"*(4-i))


print("\n\n")


# 10
print("10번")
for i in range(5, 0, -1):
    print(" "*(i-1) + "*"*(6-i) + "*"*(5-i))
for i in range(5):
    print(" "*(i+1) + "*"*(4-i) + "*"*(3-i))
