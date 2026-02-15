# Using initial values

from functools import reduce

def add(x, y):
    return x + y

nums = [1, 2, 3]

result = reduce(add, nums, 10)
print(result)


# Process
# 10 + 1 → 11
# 11 + 2 → 13
# 13 + 3 → 16
