# Reversing a string


s = "PYTHON"

stack = []

for ch in s:
    stack.append(ch)

rev = ""
while stack:
    rev += stack.pop()
print(rev)