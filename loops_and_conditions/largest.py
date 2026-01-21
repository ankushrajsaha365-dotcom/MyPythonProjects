# Largest of Three Numbers
# Input three numbers and print the largest using only if-elif-else.

a = int(input("Enter a number a: "))
b = int(input("Enter a number b: "))
c = int(input("Enter a number c: "))

if a > b:
    if a > c:
        print(f"{a} is the largest")
    else:
        print(f"{c} is the largest")
elif b > a:
    if b > c:
        print(f"{b} is the largest")
    else:
        print(f"{c} is the largest")
else:  # a == b
    if a > c:
        print(f"{a} is the largest")
    else:
        print(f"{c} is the largest")
