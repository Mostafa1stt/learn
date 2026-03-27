class car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed


class BankAccount:
    def __init__(self, amount):
        self.__amount = amount

    def deposit(self,amount):
        if amount <= 0:
            print("invalid amount")
        else:
            self.__amount += amount
            print("deposit sucssfly")

    def withdraw(self,amount):
        if amount > self.__amount:
            print("exced blacne amount")
        elif amount <= 0:
            print("invalid amount")
        else:
            self.__amount -= amount
            print("withdraw sucssfly")

    def balance(self):
        print(self.__amount)

class Student:
    def __init__(self, name):
        self.name = name
        self.__grades = []

    def grades_sitter(self,grades):
        self.__grades = grades

    def averager(self):
        sumer = 0
        for i in self.__grades:
            sumer += i
        return sumer/len(self.__grades)

