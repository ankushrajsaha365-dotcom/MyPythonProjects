class Employee:
    def calculate_bonus(self):
        print("Wrong id!!!")

class Manager(Employee):
    def __init__(self,salary):
        self.salary = salary
    def calculate_bonus(self):
        return self.salary*(1 + (1/5))
    
class Developer(Employee):
    def __init__(self,salary):
        self.salary = salary
    def calculate_bonus(self):
        return self.salary*(1 + (1/10))
    
class Intern(Employee):
    def __init__(self,salary):
        self.salary = salary
    def calculate_bonus(self):
        return self.salary
    
manager = Manager(100000)
developer = Developer(75000)
intern = Intern(25000)

jobs = [manager,developer,intern]

for job in jobs:
    print("Salary:",job.calculate_bonus())