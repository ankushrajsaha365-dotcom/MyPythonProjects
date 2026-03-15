# Write a Python program to create a new blank file and write
# some new contents in that file using write and writeline both .


with open("Welcome.txt","w") as f:
    f.write("Welcome to Python")

c = open("Welcome.txt")
print(c.read())