# Celsius to Farenheit

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

temperatures = [0, 10, 20, 30, 40]

result = list(map(celsius_to_fahrenheit, temperatures))
print(result)
