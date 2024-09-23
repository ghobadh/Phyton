"""
Name: phoneNumber.py
Author: Gavin Hashemi
Date: 2024-09-23 2:04 p.m.
Description:

"""

number = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Sever",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero"

}
phone=input("Enter your phone number: ")
result = ''
for i in phone:
    result += number.get(i,"!") + " "
print(result)