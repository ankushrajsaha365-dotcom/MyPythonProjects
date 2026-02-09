# Check if an element exists

# Input: list = [10, 20, 30], element = 20
# Output: Found

from list_input import listy


l = listy()
key = int(input("Enter a key element:"))

if key in l:
    print("Found")
else:
    print("Not Found")
