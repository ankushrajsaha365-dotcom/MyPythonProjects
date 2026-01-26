# Grade Calculator

# Problem: Input marks (0–100) and print:

# A → 90–100
# B → 75–89
# C → 50–74
# Fail → below 50
# Also handle invalid marks.


marks = int(input("Enter marks:"))

if marks in range(90,101):
    print("Grade : A")
elif marks in range(75,90):
    print("Grade : B")
elif marks in range(50,75):
    print("Grade : C")
elif marks in range(0,50):
    print("Fail")
else:
    print("Invalid marks")
