# Reverse a tuple

# Input: (1, 2, 3, 4)
# Output: (4, 3, 2, 1)

# Hint: slicing


my_tuple = tuple(map(int,input("Enter elements:").split()))

print("Original:",my_tuple)
print("Reverse:",my_tuple[::-1])