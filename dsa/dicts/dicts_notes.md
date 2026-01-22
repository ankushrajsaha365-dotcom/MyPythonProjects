# 📘 Python Dictionary – Complete Notes

## 1️⃣ What is a Dictionary?

- **Unordered**, **mutable** collection of **key–value pairs**
- Keys must be **unique** and **hashable**
- Values can be of **any type**, including lists, tuples, or other dictionaries
- Used for **fast lookups, mapping relationships, and storing structured data**

---

## 2️⃣ Dictionary Methods

- **keys()** → Returns a view object of all keys
- **values()** → Returns a view object of all values
- **items()** → Returns a view object of (key, value) pairs
- **get(key, default=None)** → Returns value for key; default if key not found
- **update(other_dict)** → Adds key–value pairs from another dictionary
- **pop(key, default)** → Removes key and returns its value
- **popitem()** → Removes and returns an arbitrary (key, value) pair
- **clear()** → Removes all items
- **copy()** → Returns a shallow copy
- **setdefault(key, default)** → Returns value for key; sets key to default if not present

__examples__

```
d = {"name": "Raj", "age": 20}
d.keys()
d.values()
d.items()
d.get("age")
d.get("gender", "Not Found")
d.update({"grade": "A"})
d.pop("age")
d.popitem()
d.setdefault("country", "India")
d.clear()
d2 = d.copy()
```

---

## 3️⃣ Built-in Functions with Dictionaries

- `len(dict)` → Number of key–value pairs
- `any(dict)` → True if any key is truthy
- `all(dict)` → True if all keys are truthy
- `sorted(dict)` → Returns a sorted list of keys
- `dict(iterable)` → Converts iterable of key–value pairs to dictionary

---

## Tips

- Use dictionaries for **fast lookup**: `value = d[key]`
- To avoid **KeyError**, use `get()` or `setdefault()`
- Dictionary keys must be **immutable** (e.g., strings, numbers, tuples)
- Dictionaries maintain **insertion order** (Python 3.7+)
- Use **nested dictionaries** to store structured data
