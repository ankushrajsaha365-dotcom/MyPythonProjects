# Level 2: Inheritance with Constructor + super()

# Problem Statement 2: BankAccount → SavingsAccount

# Task
# BankAccount:
#     account_holder
#     balance (private)

# SavingsAccount:
#     interest rate
#     calculate interest



class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance if balance >= 0 else 0

    def show_balance(self):
        print("Balance:", self.__balance)

    def _get_balance(self):   # protected access
        return self.__balance


class SavingsAccount(BankAccount):
    def __init__(self, name, balance, rate):
        super().__init__(name, balance)
        self.rate = rate

    def calculate_interest(self):
        interest = self._get_balance() * self.rate / 100
        print("Interest earned:", interest)
