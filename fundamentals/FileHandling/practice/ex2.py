# Write a program in python to store the first n prime numbers in text file.


def is_prime(num):
    if num < 2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i == 0:
            return False
    return True

n = int(input("Enter range:"))
prime = []
num = 2 

while len(prime) < n:
    if is_prime(num):
        prime.append(num)
    num+=1

with open("prime_num.txt","w") as f:
    for p in prime:
        f.write(str(p)+ "\n")

print("First", n ," prime numbers are written to the txt file")

with open("prime_num.txt","r") as f:
    print("File content:")
    print(f.read())