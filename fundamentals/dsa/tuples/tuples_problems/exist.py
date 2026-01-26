# Check if an element exists in tuple

# Input: (1, 2, 3, 4), element = 3
# Output: Found


my_tuple = tuple(map(int, input("Enter elements:").split()))

key = int(input("Enter element to search:"))

for i in my_tuple:
    if i == key:
        print("Found")