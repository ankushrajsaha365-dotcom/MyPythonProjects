class Wallet:
    def __init__(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            self.__balance = 0

    def add_money(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Money added successfully")
        else:
            print("Invalid amount")

    def spend_money(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Money spent successfully")
        else:
            print("Not enough balance")

    def show_balance(self):
        print("Current balance:", self.__balance)


wallet = Wallet(500)
wallet.add_money(200)
wallet.spend_money(300)
wallet.show_balance()



## for explanation check the markdown file with the same name
