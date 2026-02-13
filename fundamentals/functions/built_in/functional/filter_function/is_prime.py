# Prime number filter




def is_prime(num):
    if num < 2:
        return 0
    else:
        is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        return num

    
nums = list(range(1,51))

result = list(filter(is_prime,nums))

print(result)