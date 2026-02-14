from functools import reduce

def multiply(x, y):
    return x * y

n = 5
numbers = range(1, n + 1)

result = reduce(multiply, numbers)
print(result)
