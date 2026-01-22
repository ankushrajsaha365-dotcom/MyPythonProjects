# Problem:
# Input N and print all prime numbers between 1 and N.


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


N = int(input("Enter range: "))

for i in range(1, N + 1):
    if is_prime(i):
        print(i)
