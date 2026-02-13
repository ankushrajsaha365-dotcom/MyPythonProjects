# Strip whitespace

def clean(text):
    return text.strip()

data = ["  Raj ", " Aman  ", "  Riya"]

result = list(map(clean, data))
print(result)
