## Check whether a number is prime.

# ⚠️ Don’t check divisibility till n-1. Think smarter.


num = int(input("Enter a number: "))

if num < 2:
    print("Not Prime")
else:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime")
    else:
        print("Not Prime")





## Usual way

# num = int(input("Enter a number: "))

# if num < 2:
#     print("Not Prime")
# else:
#     is_prime = True
#     for i in range(2, num):
#         if num % i == 0:
#             is_prime = False
#             break

#     if is_prime:
#         print("Prime")
#     else:
#         print("Not Prime")
