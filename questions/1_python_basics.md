# 🐍 Python Basics – Viva Questions & Answers

*(Inspired by common interview patterns from GeeksforGeeks and HackerRank)*

---

## 1️⃣ What is Python?

**Answer:**

Python is a high-level, interpreted, general-purpose programming language known for its readability and simplicity.

It supports:

* Object-Oriented Programming
* Functional Programming
* Procedural Programming

Example:

```python
print("Hello, World!")
```

---

## 2️⃣ Why is Python called an interpreted language?

**Answer:**

Python code is executed line-by-line by the Python interpreter rather than being compiled into machine code before execution.

This makes:

* Debugging easier
* Development faster

---

## 3️⃣ What is dynamic typing?

**Answer:**

In Python, the type of a variable is determined at runtime.

Example:

```python
x = 10        # integer
x = "Hello"   # string
```

The same variable can store different data types at different times.

---

## 4️⃣ What are mutable and immutable data types?

**Answer:**

### 🔹 Mutable (can be changed)

* List
* Dictionary
* Set

Example:

```python
a = [1, 2, 3]
a.append(4)
```

### 🔹 Immutable (cannot be changed)

* int
* float
* string
* tuple

Example:

```python
s = "hello"
# s[0] = 'H'  ❌ Not allowed
```

Strings are immutable to improve performance and memory safety.

---

## 5️⃣ Difference between List and Tuple

| Feature     | List              | Tuple              |
| ----------- | ----------------- | ------------------ |
| Mutable     | ✅ Yes             | ❌ No               |
| Syntax      | `[ ]`             | `( )`              |
| Performance | Slower            | Faster             |
| Use case    | When data changes | When data is fixed |

---

## 6️⃣ What is the difference between `==` and `is`?

**Answer:**

* `==` checks value equality.
* `is` checks memory location (identity).

Example:

```python
a = [1,2,3]
b = [1,2,3]

print(a == b)  # True (values same)
print(a is b)  # False (different objects)
```

---

## 7️⃣ What is indentation in Python?

**Answer:**

Indentation defines blocks of code in Python.

Example:

```python
if True:
    print("Hello")
```

Without proper indentation, Python raises an error.

---

## 8️⃣ What are Python keywords?

**Answer:**

Keywords are reserved words with special meaning.

Examples:

* if
* else
* for
* while
* class
* def
* return

To see all keywords:

```python
import keyword
print(keyword.kwlist)
```

---

## 9️⃣ What is `None` in Python?

**Answer:**

`None` represents the absence of a value.

Example:

```python
x = None
```

It is commonly used as a default value.

---

## 🔟 What is type casting?

**Answer:**

Type casting means converting one data type to another.

### 🔹 Implicit Casting

Automatically done by Python.

```python
x = 5 + 2.0  # Result is float
```

### 🔹 Explicit Casting

Done manually.

```python
x = int("10")
```

---

## 1️⃣1️⃣ What are built-in data types in Python?

* int
* float
* str
* list
* tuple
* set
* dict
* bool
* NoneType

---

## 1️⃣2️⃣ Difference between `append()` and `extend()`

**append()** → Adds a single element.

```python
a = [1,2]
a.append([3,4])
# [1,2,[3,4]]
```

**extend()** → Adds elements individually.

```python
a = [1,2]
a.extend([3,4])
# [1,2,3,4]
```

---

## 1️⃣3️⃣ What is slicing?

**Answer:**

Slicing extracts a portion of a sequence.

Syntax:

```
sequence[start : stop : step]
```

Example:

```python
a = "Python"
print(a[1:5:2])
```

---

## 1️⃣4️⃣ What is shallow copy vs deep copy?

**Shallow Copy**
Copies outer object only.

**Deep Copy**
Copies outer + inner objects.

Example:

```python
import copy
a = [[1,2]]
b = copy.deepcopy(a)
```

---
