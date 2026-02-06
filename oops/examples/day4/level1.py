# Level 1: Basic Inheritance (No super() yet)

# Problem Statement 1: Person → Student

# Task
# Create a base class Person
# Store name and age
# Create a child class Student
# Add marks
# Display all details



class Person:
    def get_details(self):
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))

class Student(Person):
    def get_marks(self):
        self.marks = int(input("Enter marks: "))

    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)

student = Student()
student.get_details()   # inherited method
student.get_marks()
student.show()

    