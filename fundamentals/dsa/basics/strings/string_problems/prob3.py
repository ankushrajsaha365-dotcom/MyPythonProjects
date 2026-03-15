# Write a program that accepts a comma-separated sequence of words as input and prints
# the words in a comma-separated sequence after sorting them alphabetically.
# Input Format: The first line of input contains words separated by the comma.
# Output Format: Print the sorted words separated by the comma.
# Example:
# Input: without, hello, bag, world
# Output: bag, hello, without, world


s = input("Enter the comma separated string:")
a = s.split(",")
a.sort()
b = ','.join(a)
print("After sorting:")
print(b)