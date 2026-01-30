# class_objects3.py
# Using constructor (__init__)

class Student:

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def display(self):
        print("Name:", self.name)
        print("Roll:", self.roll)

s1 = Student("Raj", 1)
s2 = Student("Aman", 2)

s1.display()
s2.display()
