# Mobile Recharge System

# Concept: Constructor + Controlled Access
# Task
# Create a class Mobile that:

#   Constructor takes phone number and balance
#   Private variable for balance

#   Methods:
#       recharge(amount)
#       use_data(cost)
#       show_balance()
#--------------------------------------------


class Mobile:
    def __init__(self,balance):
        if balance >= 0:
            self.__balance = balance
        else:
            self.__balance = 0

    def recharge(self,amount):
        if amount < 0:
            print("Invalid recharge")
        else:
            self.__balance += amount
            print("Recharge successful")
    
    def use_data(self,cost):
        if cost <= self.__balance:
            self.__balance -= cost
            print("Data usage warning!!!")
        else:
            print("Not enough data")

    def show_balance(self):
        print(f"Current balance {self.__balance}")

mobile = Mobile(500)
amount = float(input("Enter amount to recharge:"))
mobile.recharge(amount)
cost = float(input("Enter data usage:"))
mobile.use_data(cost)
mobile.show_balance()