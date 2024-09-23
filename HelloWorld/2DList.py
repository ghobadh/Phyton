"""
Name: 2DList.py
Author: Gavin Hashemi
Date: 2024-09-23 9:55 a.m.
Description:

"""

matrix = [
    [1,2,3],
    [4,5,6],
    [6,7,8]
]
print(matrix[0][1]) # print 2
for row in matrix:
    for item in row:
        print(item)
