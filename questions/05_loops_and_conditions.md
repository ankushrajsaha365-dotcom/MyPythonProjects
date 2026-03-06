# 🐍 Python – Loops (Viva Questions & Answers)

*(Commonly asked in interviews inspired by GeeksforGeeks and HackerRank)*

---

# 🔹 1️⃣ What is a loop?

**Answer:**

A loop is used to execute a block of code repeatedly until a condition is satisfied.

Python provides:

* `for` loop
* `while` loop

---

# 🔹 2️⃣ What is a `for` loop?

**Answer:**

A `for` loop is used to iterate over a sequence like:

* List
* Tuple
* String
* Dictionary
* Range

Example:

```python id="f1k3sd"
for i in range(5):
    print(i)
```

---

# 🔹 3️⃣ What is a `while` loop?

**Answer:**

A `while` loop runs as long as a condition is True.

Example:

```python id="d8s9kl"
x = 0
while x < 5:
    print(x)
    x += 1
```

---

# 🔹 4️⃣ Difference between `for` and `while`

| for loop                           | while loop                       |
| ---------------------------------- | -------------------------------- |
| Used for iteration                 | Used for condition-based looping |
| Usually fixed number of iterations | Number of iterations may vary    |
| Cleaner syntax                     | More control                     |

---

# 🔹 5️⃣ What is `range()` function?

**Answer:**

Used to generate a sequence of numbers.

Syntax:

```python id="k3j9sd"
range(start, stop, step)
```

Example:

```python id="m2p8lk"
range(1, 10, 2)
```

---

# 🔹 6️⃣ What is `break` statement?

**Answer:**

Terminates the loop immediately.

```python id="a7d4sl"
for i in range(5):
    if i == 3:
        break
    print(i)
```

---

# 🔹 7️⃣ What is `continue` statement?

**Answer:**

Skips the current iteration and moves to the next.

```python id="q9k2dm"
for i in range(5):
    if i == 2:
        continue
    print(i)
```

---

# 🔹 8️⃣ What is `pass` statement?

**Answer:**

`pass` does nothing. It is a placeholder.

```python id="z4m7tk"
for i in range(5):
    pass
```

---

# 🔹 9️⃣ What is loop `else` in Python?

**Answer:**

The `else` block executes if the loop completes normally (without break).

Example:

```python id="r5l9df"
for i in range(3):
    print(i)
else:
    print("Loop finished")
```

If `break` occurs, `else` will NOT execute.

---

# 🔟 What is nested loop?

**Answer:**

A loop inside another loop.

Example:

```python id="t8m3sd"
for i in range(3):
    for j in range(2):
        print(i, j)
```

---

# 1️⃣1️⃣ What is infinite loop?

**Answer:**

A loop that never ends.

Example:

```python id="y7k2sd"
while True:
    print("Running")
```

---

# 1️⃣2️⃣ Time Complexity of a simple loop?

* Single loop → **O(n)**
* Nested loop → **O(n²)** (if both depend on n)

---

# 🔥 Common Trick Viva Questions

1. What happens if you modify a list while iterating?
2. Does Python support do-while loop?
3. Can you iterate over dictionary?
4. Difference between `enumerate()` and `range()`?
5. Why is `range()` memory efficient?

---

# 🎯 Viva Tip

When explaining loops:

Say:

1. Definition
2. When to use
3. Small example
4. One special concept (break/else)

That makes your answer strong.

