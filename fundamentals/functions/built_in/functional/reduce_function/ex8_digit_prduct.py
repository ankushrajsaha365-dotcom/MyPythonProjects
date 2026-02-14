# Custom Accumulation (Digit Product)

from functools import reduce

def multiply(x,y):
    return x*y

n = 5234

result = reduce(multiply, map(int, str(n)))

print(result)