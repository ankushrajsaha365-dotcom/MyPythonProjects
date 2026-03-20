class NotIntegerError(Exception):
    pass

try:
    a = input("Enter a number a: ")
    b = input("Enter a number b: ")

    if not a.isdigit() or not b.isdigit():
        raise NotIntegerError("Enter integer numbers only!")

    a = int(a)
    b = int(b)

except NotIntegerError as e:
    print(e)

except ValueError:
    print("Invalid input!")

else:
    print("The addition is", a + b)