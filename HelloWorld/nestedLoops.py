"""
Name: nestedLoops.py
Author: Gavin Hashemi
Date: 2024-09-23 8:52 a.m.
Description:

"""

for x in range (4):
    for y in range (3):
        print(f'({x},{y})')


f_shape = [5,2,5,2,2]
#for y in f_shape:
#    print('*' * y)

star='*'
for y in f_shape:
    line = ''
    for z in range(y):
        line += star
    print(line)