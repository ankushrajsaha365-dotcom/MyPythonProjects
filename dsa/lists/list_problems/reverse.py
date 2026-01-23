l = []   # list declaration
n = int(input("Enter number of elements:"))
for i in range(n):
    el = int(input("Elements:"))
    l.append(el)
print("list is : ",l)


# Reverse a list

# Input: [1, 2, 3]
# Output: [3, 2, 1]

# ❌ Don’t use reverse() at first
# ✔ Try loop or slicing


print(l[::-1])