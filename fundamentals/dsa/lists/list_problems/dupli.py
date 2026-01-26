# Remove duplicates from a list

# Input: [1, 2, 2, 3, 1]
# Output: [1, 2, 3]

from list_input import listy

l = listy()

print("Original list:",l)

new_lst = []

for i in l:
    if i not in new_lst:
        new_lst.append(i)
print("New list:",new_lst)