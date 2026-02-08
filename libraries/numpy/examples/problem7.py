# Copy vs View (VERY IMPORTANT)

# View (shares memory)

import numpy as np

a = np.array([1,2,3])
print(a)

b = a[:]
b[0]= 99

print(a)
print("_____________")
# Copy (independent)

c = a.copy()
c[0] = 100
print(a)
print(c)