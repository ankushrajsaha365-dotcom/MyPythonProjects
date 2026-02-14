# Using initial values

from functools import reduce

def add(x, y):
    return x + y

nums = [1, 2, 3]

result = reduce(add, nums, 10)
print(result)
