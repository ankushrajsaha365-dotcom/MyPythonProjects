from functools import reduce

def find_max(x, y):
    if x > y:
        return x
    return y

nums = [4, 8, 2, 10, 3]

result = reduce(find_max, nums)
print(result)
