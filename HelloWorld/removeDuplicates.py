"""
Name: removeDuplicates.py
Author: Gavin Hashemi
Date: 2024-09-23 10:35 a.m.
Description:

"""

numbers = [5,6,6,7,3,5,7,8,9]
for number in numbers:
    if  numbers.count(number) > 1:
        numbers.remove(number)
print(numbers)


numbers = [5,6,6,7,3,5,7,8,9]
uniques = []
for number in numbers:
    if  number not in uniques:
        uniques.append(number)
print(uniques)