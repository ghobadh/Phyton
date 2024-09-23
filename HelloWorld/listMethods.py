"""
Name: listMethods.py
Author: Gavin Hashemi
Date: 2024-09-23 10:20 a.m.
Description:

"""
from findLargestNumber import number

numbers = [ 6, 8,10,20,3, 6]
numbers.append(45)
print(numbers)
numbers.insert(3,66)
print(numbers)

print (numbers.pop()) # print last number
print(numbers.index(66)) # print the index number . if the number does not exist in the list , the program fails
print( 20 in numbers) #check the existence of 20
print (numbers.count(6)) # it counts how many times 6 is shown in the list
print(numbers.sort()) # This is wrong. it should be sorted then printed
numbers.sort()
print(numbers) # That is the right way

numbers.reverse()
print(numbers) # That is the right way
numbers2 = numbers.copy() # the changes in the second list will not impact on the first list as they are two individual list.
numbers2.insert(4,100)
print(numbers2)
print(numbers)

numbers.remove(6) # only the first 6 will be removed
print(numbers)
numbers.clear()
print(numbers)

