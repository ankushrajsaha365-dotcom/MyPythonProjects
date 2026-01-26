###Swap using a third variable

a = int(input("Enter a number a :"))
b = int(input("Enter a number b :"))

print("Before swap")
print(f"a is {a} and b is {b}")

temp = a 
a = b
b = temp


print("After swap:")
print(f"a is {a} and b is {b}")