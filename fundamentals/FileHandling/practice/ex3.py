# Write program in Python to store Fibonacci numbers between 0 to n, in a text file.


n = int(input("Enter range:"))
a,b = 0,1
fibb = []

while a <= n:
    fibb.append(a)
    a,b =b,a+b

with open("fibb.txt","w") as f:
    for num in fibb:
        f.write(str(num)+ "\n")

with open("fibb.txt","r") as f:
    print("File content:")
    print(f.read())