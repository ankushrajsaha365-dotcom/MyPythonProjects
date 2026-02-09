class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, x):
        self.queue.append(x)

    def dequeue(self):
        if not self.queue:
            return None
        return self.queue.pop(0)

    def front(self):
        return self.queue[0] if self.queue else None

    def size(self):
        return len(self.queue)

    def display(self):
        return self.queue

q = Queue()

print("""
1. Enqueue
2. Dequeue
3. Front
4. Display
5. Size
0. Exit
""")

while True:
    choice = int(input("Enter choice: "))

    if choice == 1:
        x = int(input("Enter element: "))
        q.enqueue(x)

    elif choice == 2:
        item = q.dequeue()
        print("Dequeued:", item if item else "Queue Empty")

    elif choice == 3:
        print("Front:", q.front())

    elif choice == 4:
        print("Queue:", q.display())

    elif choice == 5:
        print("Size:", q.size())

    elif choice == 0:
        break

    else:
        print("Invalid choice")
