from functools import reduce

def add(x, y):
    return x + y

nums = [1, 2, 3, 4]

result = reduce(add, nums)
print(result)
