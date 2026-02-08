# Even Numbers Filter

# Given a NumPy array with numbers from 1 to 20,
# print only the even numbers.


import numpy as np

array = np.arange(1,21,1)

print(array[array % 2 == 0])



# 🧠 What This Concept Is Called
# 👉 Boolean Masking
# This will appear everywhere in:
#       Data analysis
#       Pandas
#       Machine learning preprocessing

# Boolean masking means:
#        Selecting elements from an array using a
#        boolean (True/False) condition.