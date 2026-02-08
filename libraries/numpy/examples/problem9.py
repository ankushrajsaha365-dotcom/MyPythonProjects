# Where Function (Conditional Selection)

import numpy as np

arr = np.array([5, 15, 25, 35])

print(np.where(arr > 20, "High", "Low"))
