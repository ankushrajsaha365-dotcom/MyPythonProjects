def Power(base,power):
    if power == 0:
        return 1
    return base*Power(base,power-1)

base = int(input("Enter a number:"))
power = int(input("Enter power:"))
print("Answer:",Power(base,power))

# Applycable for positive numbers