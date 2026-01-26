# Find duplicate elements in a tuple

# Input: (1, 2, 3, 2, 1)
# Output: (1, 2)

my_tuple = tuple(map(int, input().split()))

seen = []
duplicates = []

for item in my_tuple:
    if item in seen and item not in duplicates:
        duplicates.append(item)
    else:
        seen.append(item)

print(tuple(duplicates))
