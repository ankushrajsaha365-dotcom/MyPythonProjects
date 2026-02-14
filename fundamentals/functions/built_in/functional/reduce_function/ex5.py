from functools import reduce

def longer(x, y):
    if len(x) > len(y):
        return x
    return y

words = ["apple", "banana", "kiwi", "strawberry"]

result = reduce(longer, words)
print(result)
