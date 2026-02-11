def myfunc(n):
    return lambda a : a**n
mypower = myfunc(2)             # Stores value of n
print(mypower(5))               # Stores value of a