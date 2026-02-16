from abc import ABC, abstractmethod


class Employee(ABC):

    def __init__(self, base_salary):
        self.base_salary = base_salary

    @abstractmethod
    def calculate_salary(self):
        pass


class Manager(Employee):
    def calculate_salary(self):
        return self.base_salary * 1.20


class Developer(Employee):
    def calculate_salary(self):
        return self.base_salary * 1.10


employees = [Manager(100000), Developer(80000)]

for emp in employees:
    print("Final Salary:", emp.calculate_salary())
