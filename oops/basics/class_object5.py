# class_objects5.py
# Constructor with behavior

class Student:

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def display(self):
        print("Name:", self.name)
        print("Roll:", self.roll)

s1 = Student("Raj", 1)
s1.display()
