stack = []
stack.append(1)     # Push 
stack.append(2)
stack.append(3)

print(stack)

stack.pop()       # removes 3
print(stack)      # [1, 2]



if stack:
    print(stack[-1])                # returns top element
