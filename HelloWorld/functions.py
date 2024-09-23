"""
Name: functions.py
Author: Gavin Hashemi
Date: 2024-09-23 2:20 p.m.
Description:
Keyword arguments MUST come after positional arguments --> line 15
"""
def greet_user(first_name:str, last_name:str) -> None :
    print(f"Hi  {first_name} {last_name}")
    print("Welcome aboard")


def square(number):
    return number * number



print("Start")
greet_user(first_name="Gargamel", last_name="Smith") # This is keyword arguments  by using the name of variable
greet_user("Gavin", last_name="Smith")
print("Finish")

print (square(3))