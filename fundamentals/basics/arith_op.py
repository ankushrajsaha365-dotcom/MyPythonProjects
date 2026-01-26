a = 54
b = 23

sum = a+b
sub = a-b
mul = a*b
div = a/b

print("Sum = ",sum)
print("Subtraction = ",sub)
print("Multiplication = ",mul)
print("Division = ",div)


#output
#Sum =  77
#Substraction =  31
#Multiplication =  1242
#Division =  2.347826086956522      


# # Note:
# In Python, the division operator (/) always returns a float,
# even if the result is a whole number.
# To get an integer result, type conversion or // (floor division) is required.


#print(int(div))                #type conversion
print(a//b)                     # Floor division