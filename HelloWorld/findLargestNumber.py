"""
Name: findLargestNumber.py
Author: Gavin Hashemi
Date: 2024-09-23 9:51 a.m.
Description:

"""

numbers= [10, 4, 8,20, 14, 18,1 ,0]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(f'The largest number is: {max}.')
