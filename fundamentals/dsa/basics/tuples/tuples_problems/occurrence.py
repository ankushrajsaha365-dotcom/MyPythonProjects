# Count occurrences of an element

# Input: (1, 2, 2, 3, 2)
# Output: 3


my_tuple = tuple(map(int , input("Enter elements:").split()))

key = int(input("Choose an element from the tuple:"))

if key in my_tuple:
    count = 0
    for i in my_tuple:
        if i == key:
            count+=1
    print(count)
else:
    print("Sorry, the element doesn't exist in the tuple!")