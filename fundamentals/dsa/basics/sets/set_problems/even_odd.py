# Set of Even and Odd Numbers

# From a list of numbers, create two sets: even and odd.


my_list = list(map(int,input().split()))

even = set()
odd = set()

for i in my_list:
    if i%2 == 0:
        even.add(i)
    else:
        odd.add(i)

print("Even set:",even)
print("Odd set:",odd)




# numbers = list(map(int, input().split()))

# even = {x for x in numbers if x % 2 == 0}
# odd = {x for x in numbers if x % 2 != 0}

# print("Even set:", even)
# print("Odd set:", odd)
