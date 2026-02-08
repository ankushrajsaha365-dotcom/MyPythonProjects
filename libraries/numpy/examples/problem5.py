# Axis Concept
# This confuses many people — remember this one rule:
#    Axis 0 → down (rows)
#    Axis 1 → across (columns)

import numpy as np

mat = np.array([[1,2,3],
                [4,5,6]])

print(mat)
print("\n")
print(np.sum(mat))           # total sum
print(np.sum(mat, axis=0))   # column-wise
print(np.sum(mat, axis=1))  # row-wise
 
print("\n")
print(np.mean(mat, axis=0))
print(np.max(mat, axis=1))
