from functools import reduce

def multiply(x, y):
    return x * y

nums = [1, 2, 3, 4]

result = reduce(multiply, nums)
print(result)
