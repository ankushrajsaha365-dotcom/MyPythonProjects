# Check if all elements are unique

# Input: (1, 2, 3, 4)
# Output: Unique


# *this version is done with using lists*
# *this will be muh easier if we use sets logic*

my_tuple = tuple(map(int,input().split()))

l1 = list(my_tuple)
l2 = []

for i in l1:
    if i not in l2:
        l2.append(i)

if l1 == l2:
    print("Unique")
else:
    print("Not Unique")

