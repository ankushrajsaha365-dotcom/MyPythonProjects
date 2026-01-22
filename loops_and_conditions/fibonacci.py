# Problem:
# Print the first N terms of the Fibonacci series.

n = int(input("Enter Range:"))
a, b = 0, 1
for i in range(n):
    print(a,end="  ")        
    a, b = b, a + b
    


