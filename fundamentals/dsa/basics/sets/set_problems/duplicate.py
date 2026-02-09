# Start with a list that has duplicate values
# numbers = [1, 2, 3, 2, 4, 1, 5]
numbers = list(map(int,input().split()))
# Convert the list to a set
unique_numbers = set(numbers)

print(unique_numbers)

