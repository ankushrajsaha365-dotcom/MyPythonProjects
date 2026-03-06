NumPy is important for:

* Data science
* Machine learning
* Scientific computing
* Even interviews sometimes

---

# 🧮 NumPy Library – Viva Questions & Answers

*(Frequently asked in interviews and technical discussions inspired by GeeksforGeeks and HackerRank)*

---

# 🔹 1️⃣ What is NumPy?

**Answer:**

NumPy (Numerical Python) is a Python library used for:

* Numerical computations
* Working with arrays
* Mathematical operations

It provides the powerful `ndarray` object.

---

# 🔹 2️⃣ Why is NumPy faster than Python lists?

**Answer:**

NumPy is faster because:

* It uses contiguous memory blocks
* It is implemented in C
* It supports vectorized operations

Lists:

* Store mixed data types
* Slower for numerical computation

---

# 🔹 3️⃣ What is ndarray?

**Answer:**

`ndarray` is the main data structure of NumPy.

It is:

* N-dimensional array
* Homogeneous (same data type)

Example:

```python id="n1k3sd"
import numpy as np
arr = np.array([1, 2, 3])
```

---

# 🔹 4️⃣ Difference between Python List and NumPy Array

| Feature                 | List          | NumPy Array |
| ----------------------- | ------------- | ----------- |
| Data type               | Mixed allowed | Homogeneous |
| Speed                   | Slower        | Faster      |
| Mathematical operations | Not direct    | Vectorized  |
| Memory                  | More          | Less        |

---

# 🔹 5️⃣ What is vectorization?

**Answer:**

Performing operations on entire arrays without explicit loops.

Example:

```python id="k9s2dl"
arr = np.array([1, 2, 3])
print(arr * 2)
```

No loop needed.

---

# 🔹 6️⃣ How do you create arrays in NumPy?

```python id="m4d8sl"
np.array([1,2,3])
np.zeros((2,3))
np.ones((3,3))
np.arange(0,10)
np.linspace(0,1,5)
```

---

# 🔹 7️⃣ What is the difference between `arange()` and `linspace()`?

* `arange()` → Uses step size
* `linspace()` → Uses number of elements

---

# 🔹 8️⃣ What is shape in NumPy?

**Answer:**

Shape defines the dimensions of an array.

```python id="b7s3kd"
arr.shape
```

Example:
(2,3) → 2 rows, 3 columns

---

# 🔹 9️⃣ What is reshape()?

**Answer:**

Changes the shape of an array without changing data.

```python id="d3k9sl"
arr.reshape(2,3)
```

---

# 🔟 What is broadcasting?

**Answer:**

Broadcasting allows operations between arrays of different shapes.

Example:

```python id="r9s2dl"
arr = np.array([1,2,3])
print(arr + 5)
```

---

# 1️⃣1️⃣ What is slicing in NumPy?

Similar to list slicing but supports multi-dimensional slicing.

```python id="v3k8sl"
arr[0:2, 1:3]
```

---

# 1️⃣2️⃣ What is difference between view and copy?

* **View** → Reflects changes in original array
* **Copy** → Independent new array

```python id="x5k1sl"
b = arr.view()
c = arr.copy()
```

---

# 1️⃣3️⃣ What is axis in NumPy?

Axis defines direction of operation.

* axis=0 → Column-wise
* axis=1 → Row-wise

---

# 1️⃣4️⃣ What are some common NumPy functions?

* np.mean()
* np.sum()
* np.max()
* np.min()
* np.std()

---

# 🔥 Common NumPy Interview Questions

1. Why is NumPy memory efficient?
2. What is difference between flatten() and ravel()?
3. What is difference between copy() and view()?
4. What is broadcasting rule?
5. What is universal function (ufunc)?

---

# 🎯 Important Advice

If you're preparing for:

* College viva → Basics enough
* ML/DS interview → Must understand broadcasting deeply

---

