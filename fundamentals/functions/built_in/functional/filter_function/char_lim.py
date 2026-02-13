# Keep names longer than 4 characters
 
def long_name(name):
    return len(name) > 4

names = ["Raj", "Aman", "Ritika", "Sohan"]

result = list(filter(long_name, names))
print(result)
