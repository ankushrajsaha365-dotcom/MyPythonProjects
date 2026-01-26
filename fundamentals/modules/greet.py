def intro(name):
    print(f"Hello {name}")
    print("\nHere's a guessin game\nGuess a number between 1 - 10\n")
    while(True):
        key = 7
        num = int(input("Enter a number:"))
        if num in range(1,11):
            if num == key:
                print("\nGood Guess!!!")
                print(f"Bye {name}")
                break
            else:
                print("\nSo closeee! Give it a try again!!!\n")
        else:
            print("\nTold you, the range is 1 - 10!!!")