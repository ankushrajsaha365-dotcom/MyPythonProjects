def Trib(n):
    a, b, c = 1, 1, 2
    series = []
    for i in range(n):
        series.append(a)
        a, b, c= b, c, a+b+c
    return series

n = int(input("Enter Range: "))
print(Trib(n))
