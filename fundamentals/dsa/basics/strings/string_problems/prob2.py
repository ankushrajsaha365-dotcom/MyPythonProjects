# Write a program to show all the common words between two strings.

s1 = input("Enter sentence 1:")
s2 = input("Enter sentence 2:")

words1 = s1.split(" ")
words2 = s2.split(" ")

# for i in words1:
#     for j in words2:
#         if i == j:
#             print(i,end=" ")
#             break
#         else:
#             end=" "
common = set(words1) & set(words2)
print("Common words:", common)