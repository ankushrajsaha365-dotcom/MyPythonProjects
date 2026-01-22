# 📘 Python Tuple – Complete Notes

## 1️⃣ What is a Tuple?

- **Ordered**, **immutable** collection of elements
- Allows **duplicates**
- Elements can be of **different types**
- Hashable (can be used as dictionary keys if all elements are hashable)

---

## 2️⃣ Tuple Methods

- **count(x)** → Number of occurrences
- **index(x)** → Index of first occurrence

__examples__
```
t = (1, 2, 3, 2)
t.count(2)
t.index(3)
```

# Note: Methods like append(), remove(), or sort()  
# do not exist for tuples because they are immutable.

---

## 3️⃣ Built-in Functions with Tuples

- `len(tuple)` → Length
- `max(tuple)` → Maximum
- `min(tuple)` → Minimum
- `sum(tuple)` → Sum of elements
- `sorted(tuple)` → Returns a new sorted list
- `any(tuple)` → True if any element is True
- `all(tuple)` → True if all elements are True
- `enumerate(tuple)` → Index & value pairs
- `zip(tuple1, tuple2)` → Combine multiple iterables
- `tuple(iterable)` → Converts iterable to tuple

---

## Tips

- Use tuples for **fixed data** (e.g., GPS coordinates, RGB values) to prevent accidental changes
- Single element tuple: Always use a **trailing comma**: `t = (5,)`
- Tuples are **faster** and use **less memory** than lists
- Use **tuple unpacking** to assign values: `x, y = (10, 20)`
- To "modify" a tuple, **convert it to a list**, change it, and convert it back