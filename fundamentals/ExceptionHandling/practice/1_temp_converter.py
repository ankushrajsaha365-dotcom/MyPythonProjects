# Write a program that:
# Takes temperature input from user
# Converts Celsius → Fahrenheit

# Rules:
# Input must be numeric
# Temperature cannot be below -273.15 (absolute zero)
# Raise a custom TemperatureError if invalid


class TemperatureError(Exception):
    pass

try:
    temp = float(input("Enter temperature in Celsius: "))

    if temp < -273.15:
        raise TemperatureError("Temperature cannot be below -273.15°C (absolute zero)")

except ValueError:
    print("Input must be numeric!")

except TemperatureError as e:
    print(e)

else:
    fahrenheit = (temp * 9/5) + 32
    print("Temperature in Fahrenheit:", fahrenheit)
