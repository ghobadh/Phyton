"""
Name: CarClass.py
Author: Gavin Hashemi
Date: 2024-09-23 11:35 a.m.
Description:

"""
class Car:
    def __init__(self, brand:str, horsepower:int):
        self.brand = brand
        self.horsepower = horsepower
    def __str__(self) ->str:
        return f'Brand:{self.brand}, {self.horsepower}hp'
    def __add__(self, other ) -> str:
        return f'{self.brand} & {other.brand}'
    def drive(self) -> None:
        print(f'{self.brand} is driving!')
    def get_info(self, var: int) -> None:
        print (f'var: {var}')
        print(f'Brand:{self.brand} with {self.horsepower} horepower')

volvo: Car = Car('Volvo', 200)
print(volvo)
volvo.drive()
volvo.get_info('Volvo')

bmw: Car = Car('BMW', 250)
print(volvo+ bmw)