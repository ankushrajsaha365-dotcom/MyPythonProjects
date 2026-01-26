# Count Digits, Sum of Digits

# Problem:
# Input a number and print:
# Total digits
# Sum of digits

while True:
    num = input("Enter a number:")
    if num.isdigit():
        count = len(num)
        digit_sum = 0
        for i in num:
            digit_sum += int(i)
        print("Total digits:",count)
        print("Sum of digits:",digit_sum)
        break
    else:
        print("Wrong input!!!")



