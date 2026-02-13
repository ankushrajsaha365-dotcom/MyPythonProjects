# Keep positive numbers

def is_positive(x):
    return x > 0

nums = [-3, -1, 0, 2, 4]

result = list(filter(is_positive, nums))
print(result)
