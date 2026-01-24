# Find duplicate elements in a tuple

# Input: (1, 2, 3, 2, 1)
# Output: (1, 2)

my_tuple = tuple(map(int,input().split()))
my_list = []

for i in my_tuple:
    if i not in my_list:
        my_list.append(i)

my_tuple2 = tuple(my_list)
print(my_tuple2)