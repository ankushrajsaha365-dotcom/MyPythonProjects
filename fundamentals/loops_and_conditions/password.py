## Ask user to enter a password repeatedly until:
# Length ≥ 8
# Contains at least one digit


while True:
    password = input("Enter a password: ")

    if len(password) < 8:
        print("Password must be at least 8 characters long")
        continue

    flag = 0
    for i in password:
        if i in ['1','2','3','4','5','6','7','8','9','0']:         #same can be done with isdigit() inbuilt function
            flag = 1                                               # if i.isdigit(): ....
            break                                                  
    if flag == 1:
        print("Password is approved")
        break
    else:
        print("Password must contain at least one digit")
