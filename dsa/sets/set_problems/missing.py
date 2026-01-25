# Missing Numbers

# Given a set of numbers from 1 to N with some missing, find the missing ones.

N = int(input("Enter the range: "))

full_set = set(range(1, N + 1))
user_set = set(map(int, input(f"Enter numbers between 1 and {N}: ").split()))

missing_numbers = full_set - user_set

print("Missing numbers:", missing_numbers)
