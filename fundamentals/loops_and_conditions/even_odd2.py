##  Print how many even and odd numbers are there between a given range

lower = int(input("Enter the lower range: "))
upper = int(input("Enter the upper range: "))

even = 0
odd = 0

if lower > upper:
    print("Wrong range!!!")
else:
    for i in range(lower, upper + 1):
        if i % 2 == 0:
            even += 1
        else:
            odd += 1

    print("Number of even numbers in range:", even)
    print("Number of odd numbers in range:", odd)
