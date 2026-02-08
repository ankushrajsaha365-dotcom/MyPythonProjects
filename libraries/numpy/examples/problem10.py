# Stacking & Splitting (Intro)

import numpy as np

a = np.array([1,2])
b = np.array([3,4])

print(np.vstack((a,b)))
print(np.hstack((a,b)))


arr = np.arange(1, 7)

print(np.split(arr, 3))
