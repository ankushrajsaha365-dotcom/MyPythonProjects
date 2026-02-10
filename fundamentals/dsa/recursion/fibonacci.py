def Fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return Fib(num-1)+Fib(num-2)

num = int(input("Enter a number:"))
print(f"{num} th number of the Fibonacci series is {Fib(num)}")