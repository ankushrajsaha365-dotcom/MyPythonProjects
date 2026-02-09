# From an array 1 to 50, select numbers that:
# are divisible by 3
# greater than 10
# less than 40

import numpy as np

array = np.arange(1,51)

print(array[(array % 3 == 0) & (array > 10) & (array < 40)])

