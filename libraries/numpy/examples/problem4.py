# Reshaping Arrays (VERY IMPORTANT)

import numpy as np

arr = np.arange(1,13)
mat = arr.reshape(3,4)                  # row , column

print(mat)


# Rules
# Total elements must match
# 3 × 4 = 12 ✔