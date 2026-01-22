def greet(name):
    print(f"Hello {name}")

# this runs ONLY when greet.py is executed directly
if __name__ == "__main__":
    name = input("Enter your name: ")
    greet(name)
