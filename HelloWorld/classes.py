"""
Name: classes.py
Author: Gavin Hashemi
Date: 2024-09-23 4:22 p.m.
Description:
Unlike variable and method names , we use the first char (Camel style) in the class name capital
"""

class Point:
    #constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        print("move")


    def draw(self):
        print("draw")

point1 = Point(5,7)
#We can add new variable to the class without any issue. They should not be in class definition!
point1.z= 10
point1.f = 20
point1.draw()
print(point1.x, point1.y)
print(point1.f, point1.z)