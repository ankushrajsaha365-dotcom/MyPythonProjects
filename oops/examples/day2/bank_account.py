class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def show_balance(self):
        print("Balance:", self.balance)


# user input
name = input("Enter account holder name: ")
balance = float(input("Enter initial balance: "))

acc = BankAccount(name, balance)

amount = float(input("Enter amount to deposit: "))
acc.deposit(amount)

acc.show_balance()
