class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self,x):
        self.stack.append(x)

    def pop(self):
        if not self.stack:
            return None
        else:
            return self.stack.pop()

    def display(self):
        return self.stack
    
    def peek(self):
        return self.stack[-1] if self.stack else None

    def size(self):
        return len(self.stack)
    
stack = Stack()
print("""
1. Push
2. Pop
3. Peek
4. Display
5. Size
0. Exit
""")

while True:
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a number!")
        continue

    if choice == 1:
        x = int(input("Enter element: "))
        stack.push(x)

    elif choice == 2:
        popped = stack.pop()
        if popped is None:
            print("Stack Underflow")
        else:
            print("Popped:", popped)

    elif choice == 3:
        top = stack.peek()
        print("Top:", top if top is not None else "Stack is empty")

    elif choice == 4:
        print("Stack:", stack.display())

    elif choice == 5:
        print("Size:", stack.size())

    elif choice == 0:
        print("Exiting...")
        break

    else:
        print("Invalid choice!")