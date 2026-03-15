# Write a program that accepts a sentence and calculate the number of upper-case
# letters and lower-case letters.
# Input Format: The first line of the input contains a statement.
# Output Format: Print the number of upper case and lower case respectively.
# Example: Input: Hello world! Output: 1 9



s = input("Enter your sentence:")
up = 0
low = 0

for i in range(len(s)):
    c = s[i]
    if ord(c) >= 65 and ord(c) <= 90:
        up+=1
    if ord(c) >= 97 and ord(c) <= 122:
        low+=1
    else:
        end = " "
print(up)
print(low)