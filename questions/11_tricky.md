# 🧠 Tricky Python Viva Questions (With Answers)

*(Common tricky concepts discussed on platforms like GeeksforGeeks and HackerRank)*

---

# 🔹 1️⃣ Mutable Default Argument Problem

### Question

What will be the output?

```python
def add_item(item, lst=[]):
    lst.append(item)
    return lst

print(add_item(1))
print(add_item(2))
```

### Answer

Output:

```
[1]
[1, 2]
```

### Explanation

Default mutable arguments are **shared between function calls**.

Correct approach:

```python
def add_item(item, lst=None):
    if lst is None:
        lst = []
```

---

# 🔹 2️⃣ Difference Between `is` and `==`

### Question

```python
a = [1,2,3]
b = [1,2,3]

print(a == b)
print(a is b)
```

### Answer

```
True
False
```

### Explanation

* `==` → compares values
* `is` → compares memory locations

---

# 🔹 3️⃣ String Immutability

### Question

```python
s = "hello"
s[0] = "H"
```

### Answer

Error:

```
TypeError: 'str' object does not support item assignment
```

### Explanation

Strings in Python are **immutable**.

---

# 🔹 4️⃣ List Multiplication Trap

### Question

```python
a = [[0]*3]*3
a[0][0] = 1
print(a)
```

### Answer

```
[[1,0,0],
 [1,0,0],
 [1,0,0]]
```

### Explanation

All rows reference the **same list in memory**.

Correct way:

```python
a = [[0]*3 for _ in range(3)]
```

---

# 🔹 5️⃣ Late Binding in Loops

### Question

```python
funcs = []

for i in range(3):
    funcs.append(lambda: i)

for f in funcs:
    print(f())
```

### Answer

```
2
2
2
```

### Explanation

Lambdas capture variables **by reference**, not value.

---

# 🔹 6️⃣ Modifying List During Iteration

### Question

```python
nums = [1,2,3,4]

for n in nums:
    nums.remove(n)

print(nums)
```

### Answer

```
[2,4]
```

### Explanation

Removing elements shifts the list during iteration.

---

# 🔹 7️⃣ `None` Comparison

### Question

Which is correct?

```
x == None
x is None
```

### Answer

Correct:

```
x is None
```

Reason: `None` is a **singleton object**.

---

# 🔹 8️⃣ Dictionary Key Restriction

### Question

Can lists be dictionary keys?

### Answer

❌ No.

Dictionary keys must be **immutable and hashable**.

Allowed keys:

* int
* string
* tuple

---

# 🔹 9️⃣ Tuple with One Element

### Question

```python
a = (5)
b = (5,)
```

Which one is a tuple?

### Answer

```
b = (5,)
```

Comma makes it a tuple.

---

# 🔹 🔟 Integer Caching

### Question

```python
a = 256
b = 256

print(a is b)
```

### Answer

```
True
```

Python caches small integers (-5 to 256).

---

# 🔹 1️⃣1️⃣ Generator vs List

### Question

```python
a = [x*x for x in range(5)]
b = (x*x for x in range(5))
```

Difference?

### Answer

* `a` → list (stored in memory)
* `b` → generator (lazy evaluation)

Generators save memory.

---

# 🔹 1️⃣2️⃣ Scope Trick

### Question

```python
x = 10

def func():
    x += 5
    print(x)

func()
```

### Answer

Error:

```
UnboundLocalError
```

Because Python treats `x` as a **local variable**.

---

# 🎯 Interview Tip

When facing tricky questions:

1️⃣ Think about **memory references**
2️⃣ Think about **mutability**
3️⃣ Think about **scope rules**

Most Python traps come from these three.

---