"""
Name: tuples.py
Author: Gavin Hashemi
Date: 2024-09-23 10:42 a.m.
Description:

"""
from findLargestNumber import number

#Tuples are similar to lists, but you cannot add or removed any items from it.
#Tuples are immutable. We use () instead of []

numbers = (1,2,3,4,5)
# it has only two method, count() and index()
print(numbers.count(3)) # it counts how many 3 in the tuple
print(numbers.index(3)) # it give the index number of 3
print(numbers[4])





