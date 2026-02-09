from list_input import listy

l1 = listy()


even = []
odd = []
for x in l1:
    if x%2 == 0:
        even.append(x)
    else:
        odd.append(x)

    
print("Even:",even)
print("Odd:",odd)