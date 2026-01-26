## Guess the Number Game
# Problem:
# Program chooses a fixed number (say 7)
# User keeps guessing
# Program tells Too High / Too Low
# Stops when guessed correctly


key = 7                    # the code is made with other numbers in mind ,a general case

while True:
    guess = int(input("Enter a number:"))
    if guess == key:
        print("Guessed correctly! Here's a toffee!!!")
        break
    else:
        if guess in range(key-5,key+6):
            print("Sooo closeeee...")
        elif guess in range(key-10,key+11):
            print("You are close! Try a little more!!!")
        else:
            if guess > key+10:
                print("Nah! you are Too High!!!")
            elif guess < key-10 :
                print("Nah! you are Too Low!!!")



#Another way...

# key = 7

# while True:
#     guess = int(input("Enter a number: "))

#     if guess == key:
#         print("Guessed correctly! Here's a toffee!!!")
#         break

#     diff = abs(guess - key)

#     if diff <= 5:
#         print("Sooo closeeee...")
#     elif diff <= 10:
#         print("You are close! Try a little more!!!")
#     elif guess > key:
#         print("Nah! you are Too High!!!")
#     else:
#         print("Nah! you are Too Low!!!")
