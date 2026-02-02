# Online Game Coins

# Concept: Controlled State Change

# Task
# Create a class GameAccount:

#     Constructor: username, coins
#     Private coins variable
#     Methods:
#         earn_coins(amount)
#         spend_coins(amount)
#         show_coins()


class GameAccount:
    def __init__(self,username,coins):
        self.username = username
        self.__coins = coins if coins >= 0 else 0

    def earn_coins(self,amount):
        if amount >= 0:
            self.__coins += amount
            print("Congrats coins added to account!!!")
        else:
            print("Invalid coin amount!!!")
    
    def spend_coins(self,amount):
        if amount <= self.__coins:
            self.__coins -= amount
            print("Coins spent successfully!!!")
        else:
            print("You don't have enough coins in your account!!!")

    def show_coins(self):
        print(f"You currently have {self.__coins} coins in your account")


username = input("Enter username:") 
game = GameAccount(username,1000)
amount = int(input("Enter coins you want to add:"))
game.earn_coins(amount)

amount = int(input("Enter coins to spend:"))
game.spend_coins(amount)

game.show_coins()