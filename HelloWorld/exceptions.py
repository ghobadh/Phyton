"""
Name: exceptions.py
Author: Gavin Hashemi
Date: 2024-09-23 4:09 p.m.
Description:

"""
try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ValueError:
    print('Please enter an integer')
except ZeroDivisionError:
    print('Please enter age bigger than 0 ')