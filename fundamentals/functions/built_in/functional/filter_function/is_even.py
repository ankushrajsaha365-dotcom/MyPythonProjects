# Keep even numbers

def is_even(x):
    return x % 2 == 0

nums = [1, 2, 3, 4, 5, 6]

result = list(filter(is_even, nums))
print(result)
