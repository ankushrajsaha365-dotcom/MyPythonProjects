###Swap without using a third variable

a = int(input("Enter a number a :"))
b = int(input("Enter a number b :"))

print("Before swap")
print(f"a is {a} and b is {b}")

a,b = b,a

print("After swap:")
print(f"a is {a} and b is {b}")