# class_objects2.py
# Class with methods (no constructor)

class Student:

    def set_details(self, name, roll):
        self.name = name
        self.roll = roll

    def display(self):
        print("Name:", self.name)
        print("Roll:", self.roll)

s1 = Student()
s1.set_details("Raj", 1)
s1.display()
