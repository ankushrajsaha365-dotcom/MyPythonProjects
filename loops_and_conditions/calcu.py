### Menu driven calculator program:
# 1. Add
# 2. Subtract
# 3. Multiply
# 4. Divide
# 5. Exit


while(True):
    print("---------------Menu----------------\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Exit")
    choice = int(input("Enter your choice:"))
    if choice in range(1,6):
        if choice == 5:
            print("Exiting program...")
            break
        else:
            a = int(input("Enter a number a:"))
            b = int(input("Enter a number b:"))
            if choice==1:
                print(a+b)
            elif choice == 2:
                print(a-b)
            elif choice == 3:
                print(a*b)
            elif choice == 4:
                if b == 0:
                    print("Cannot divide by zero")
                else:
                    print(a/b)
    else:
        print("Wrong choice!!!")
        