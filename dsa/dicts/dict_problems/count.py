# Input a string and count frequency of each character.


s = input("Enter a string: ")

d = {}
for ch in s:
    d[ch] = d.get(ch, 0) + 1

print(d)



# short method
# from collections import Counter

# s = input("Enter a string: ")
# print(dict(Counter(s)))
