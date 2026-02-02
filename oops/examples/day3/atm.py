# -----ATM-----
# Create a class ATMAccount that represents a bank ATM account.
# Constructor
# Takes:
#     account_holder
#     balance
# Balance must not be negative
# Store balance as a private variable

# Methods
#     deposit(amount)
#         Add money only if amount is positive
#     withdraw(amount)
#         Withdraw only if:
#             amount is positive
#             sufficient balance exists
#     show_balance()
#         Display current balance safely

# Rules
#   Balance must never be accessed directly
#   Balance must never go negative
#   All changes must go through methods only


class ATMAccount:
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.__balance = balance if balance >= 0 else 0

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print("Cash deposited successfully!!!")
        else:
            print("Wrong amount entered!!!")

    def withdraw(self,amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print("Cash withdrawn successfully!!!")
        else:
            print("Not enough cash in account!!!")
    
    def show_balance(self):
        print(f"You have {self.__balance} $ in your account")

account_holder = int(input("Enter your account number:"))
atm = ATMAccount(account_holder,1000)
amount = int(input("Enter amount to deposit:"))
atm.deposit(amount)
amount = int(input("Enter amount to withdraw:"))
atm.withdraw(amount)

atm.show_balance()