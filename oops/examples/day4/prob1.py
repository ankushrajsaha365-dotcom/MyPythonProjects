# Problem 1: Employee → Developer
# Employee: name, salary
# Developer: language
# Show all details


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary   # private

    def get_salary(self):
        return self.__salary

    def update_salary(self, amount):
        if amount > 0:
            self.__salary += amount
        else:
            print("Invalid salary update")


class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def show_details(self):
        print("Employee name:", self.name)
        print("Salary:", self.get_salary())
        print("Language:", self.language)


name = input("Enter your name: ")
salary = int(input("Enter salary: "))
language = input("Enter coding language: ")

dev = Developer(name, salary, language)

dev.show_details()
