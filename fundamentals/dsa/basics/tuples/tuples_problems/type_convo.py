# Convert tuple to list and list to tuple

# Input: (1, 2, 3)
# Output: [1, 2, 3] → (1, 2, 3)

my_tuple = tuple(input("Enter elements:").split())

print(my_tuple)
print("Old type:",type(my_tuple))

my_list = list(my_tuple)
print(my_list)
print("New type:",type(my_list))