from functools import reduce

def combine(x, y):
    return x + y

data = [[1, 2], [3, 4], [5, 6]]

result = reduce(combine, data)
print(result)

