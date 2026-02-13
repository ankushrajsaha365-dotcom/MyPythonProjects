# Remove false values

data = [0, 1, "", "Hello", None, True, False]

result = list(filter(None, data))
print(result)
