# Check Element Existence
# Check if a given element exists in a set.

my_set = set(map(int , input().split()))
key = int(input("Enter a element to checkn if it exists in the set:"))

if key in my_set:
    print("Found")
else:
    print("Not Found")