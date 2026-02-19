# Problem:
# Print the first N terms of the Fibonacci series.

def Fib(n):
    a, b = 0, 1
    series = []
    for i in range(n):
        series.append(a)
        a, b = b, a + b
    return series

n = int(input("Enter Range: "))
print(Fib(n))
