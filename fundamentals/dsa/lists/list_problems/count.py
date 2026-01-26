# Count occurrences of each element

# Input: [1, 2, 2, 3]
# Output: {1:1, 2:2, 3:1}

from list_input import listy

l = listy()

print("list:",l)


lst = [1, 2, 2, 3]
freq = {}

for item in lst:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1

print(freq)
