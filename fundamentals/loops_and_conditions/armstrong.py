# Problem:
# Check if a number is an Armstrong number.

# Example:
# 153 → 1³ + 5³ + 3³ = 153


num = input("Enter a number:")
check_armstrong = 0
power = len(num)
if num.isdigit():
    for i in num:
        check_armstrong += int(i)**power

    if check_armstrong == int(num):
        print("It's an Armstrong number")
    else:
        print("It's not an Armstrong number")
else:
    print("Wrong input")











#### method 2


# num = int(input("Enter a number: "))
# temp = num

# count = 0
# while temp > 0:
#     count += 1
#     temp //= 10

# temp = num
# total = 0

# while temp > 0:
#     digit = temp % 10
#     total += digit ** count
#     temp //= 10

# if total == num:
#     print("Armstrong number")
# else:
#     print("Not an Armstrong number")
