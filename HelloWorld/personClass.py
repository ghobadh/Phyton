"""
Name: personClass.py
Author: Gavin Hashemi
Date: 2024-09-23 4:32 p.m.
Description:

"""
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def talk(self):
        return f"{self.name} is talking"

person1 = Person("Gargamel", 25, 1)
print(person1.talk())