# 1. What is NumPy?

NumPy is a **Python library for numerical computing**. It provides **fast arrays** and **vectorized operations**.

## Key Features

* Multidimensional arrays (`ndarray`)
* Mathematical operations without loops
* Supports linear algebra, statistics, and random numbers

## Importing NumPy

```python
import numpy as np
```

---

# 2. Creating Arrays

## Using `array()`

```python
arr1 = np.array([1, 2, 3])
arr2 = np.array([[1, 2], [3, 4]])
```

## Common Array Creation Functions

```python
np.zeros((2, 3))        # array of zeros
np.ones((3, 3))         # array of ones
np.eye(3)               # identity matrix
np.arange(1, 10, 2)     # array with a range
np.linspace(0, 1, 5)    # evenly spaced numbers
np.random.rand(2, 3)    # random floats [0,1)
np.random.randint(1, 10, (2, 3))  # random integers
```

---

# 3. Array Attributes

```python
arr.ndim      # number of dimensions
arr.shape     # shape of array
arr.size      # total elements
arr.dtype     # data type of elements
```

---

# 4. Reshaping & Flattening

```python
arr.reshape(2, 3)  # change shape
arr.flatten()      # convert to 1D array
```

---

# 5. Indexing & Slicing

```python
arr[0]       # first element
arr[-1]      # last element
arr[1:4]     # slice
arr[:, 1]    # column
arr[0, 1]    # element at row 0, column 1
```

---

# 6. Mathematical Operations

```python
a + b
a - b
a * b
a / b
```

## Universal Functions

```python
np.sqrt(a)
np.sum(a)
np.mean(a)
np.max(a)
np.min(a)
```

---

# 7. Axis Operations

```python
np.sum(arr, axis=0)  # sum of columns
np.sum(arr, axis=1)  # sum of rows
```

---

# 8. Boolean Indexing

```python
arr[arr > 5]   # elements greater than 5
```

---

# 9. Copy vs View

```python
view_arr = arr.view()   # shares memory
copy_arr = arr.copy()   # independent
```

---

# 10. Sorting & Searching

```python
np.sort(arr)
np.where(arr == 5)
np.argmax(arr)
np.argmin(arr)
```

---

# 11. Stacking & Splitting

```python
np.vstack((a, b))  # vertical stack
np.hstack((a, b))  # horizontal stack
np.split(arr, 2)   # split array
```

---

# 12. Linear Algebra

```python
np.dot(a, b)           # matrix multiplication
np.linalg.det(a)       # determinant
np.linalg.inv(a)       # inverse
```

---

# 13. Broadcasting

```python
arr + 10   # adds 10 to each element
```

---

# 14. Why Use NumPy?

* Faster and more memory-efficient than lists
* Supports vectorized operations
* Backbone of **Pandas, ML, AI workflows**

---

# 15. Key Takeaways

* `ndarray` is the core structure
* Operations are element-wise
* Essential for data science and numerical computing

---
