# Problem 2: Vehicle → Car
# Vehicle: brand, speed
# Car: fuel_type
# Display info


class Vehicle:
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed

class Car(Vehicle):
    def __init__(self,brand,speed,fuel_type):
        super().__init__(brand,speed)
        self.fuel_type = fuel_type

    def display(self):
        print("---------------------------")
        print("BRAND:",self.brand)
        print("SPEED:",self.speed)
        print("FUEL:",self.fuel_type)
        print("---------------------------")

        
brand = input("Enter brand name:")
speed = int(input("Enter top speed:"))
fuel_type = input("Enter fuel type:")

car = Car(brand,speed,fuel_type)
car.display()