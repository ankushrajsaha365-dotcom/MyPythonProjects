# class_objects4.py
# Introducing constructor (__init__)

class Student:

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

s1 = Student("Raj", 1)
s2 = Student("Aman", 2)

print(s1.name, s1.roll)
print(s2.name, s2.roll)
