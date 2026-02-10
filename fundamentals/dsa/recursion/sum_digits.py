def sum_digits(num):
    if num == 0:          # base case
        return 0
    return num % 10 + sum_digits(num // 10)

num = int(input("Enter a number: "))
print("Sum of digits:", sum_digits(num))
