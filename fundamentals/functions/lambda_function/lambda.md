# 🔹 **What is a lambda function?**

A **lambda function** in Python is a **small, anonymous function** — meaning it has **no name**.

It is created using the keyword **`lambda`**.

### 📌 Syntax:

```python
lambda arguments: expression
```

### 📌 Example:

```python
square = lambda x: x * x
print(square(5))
```

**Output:**

```
25
```

---

# 🔹 **Why use lambda functions?**

They are useful when you need a quick function **for one-time use**, especially inside:

* `map()`
* `filter()`
* `sorted()`
* GUI callbacks
* Small functional-style operations

---

# 🔹 More Examples

### 1️⃣ **Lambda with two arguments**

```python
add = lambda a, b: a + b
print(add(3, 4))
```

Output:

```
7
```

---

### 2️⃣ **Using lambda with `map()`**

Square each number:

```python
nums = [1, 2, 3, 4]
result = list(map(lambda x: x*x, nums))
print(result)
```

Output:

```
[1, 4, 9, 16]
```

---

### 3️⃣ **Using lambda with `filter()`**

Filter even numbers:

```python
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)
```

Output:

```
[2, 4, 6]
```

---

### 4️⃣ **Using lambda with `sorted()`**

Sort tuples by the second value:

```python
pairs = [(1, 4), (3, 1), (5, 2)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)
```

Output:

```
[(3, 1), (5, 2), (1, 4)]
```

---

# 🔹 When NOT to use lambda

* When the function is long
* When readability matters
* When you need documentation or reuse
