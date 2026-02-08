# Sorting and Argsort

import numpy as np

arr = np.array([40, 10, 30, 20])

np.sort(arr)     # returns sorted copy
arr.sort()         # sorts in-place


# Indices of sorted order

print(np.argsort(arr))