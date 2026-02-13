# Addition (multiple iterables)

def add(x, y):
    return x + y

a = [1, 2, 3]
b = [4, 5, 6]

result = list(map(add, a, b))
print(result)
