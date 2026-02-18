# Initial balance = 10,000

# User enters:
# Transfer amount
# Raise custom exceptions if:
#     Amount ≤ 0
#     Amount > balance
#     Amount > 5000 (daily transfer limit)
# Handle all properly and print remaining balance if valid.



class BankBalanceError(Exception):
    pass


balance = 10000

try:
    amount = int(input("Enter amount to withdraw:"))
    
   
    if amount <= 0:
        raise BankBalanceError("Enter a valid amount!!!")
    if amount > balance:
        raise BankBalanceError("You don't have enough balance!!!")
    if amount > 5000:
        raise BankBalanceError("You have crossed the daily transfer limit\nAmount shouldn't exceed 5000")
        

except BankBalanceError as e:
    print(e)

else:
    balance -= amount
    print("Processing transaction...")
    print("Remaining Balance:", balance)