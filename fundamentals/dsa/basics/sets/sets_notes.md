# 📘 Python Set – Complete Notes

## 1️⃣ What is a Set?

- **Unordered**, **mutable** collection of **unique elements**
- Does **not allow duplicates**
- Elements can be of **different types**, but **must be hashable**
- Useful for **membership tests**, **removing duplicates**, and **set operations**

---

## 2️⃣ Set Methods

- **add(x)** → Add element `x` to the set
- **remove(x)** → Remove element `x` (raises error if not found)
- **discard(x)** → Remove element `x` (no error if not found)
- **pop()** → Remove and return an arbitrary element
- **clear()** → Remove all elements
- **copy()** → Returns a shallow copy
- **union(other_set)** → Returns a new set with elements from both sets
- **update(other_set)** → Adds elements from another set
- **intersection(other_set)** → Returns elements common to both sets
- **intersection_update(other_set)** → Keeps only elements found in both sets
- **difference(other_set)** → Returns elements in current set but not in other
- **difference_update(other_set)** → Removes elements found in other set
- **symmetric_difference(other_set)** → Elements in either set, but not both
- **symmetric_difference_update(other_set)** → Updates current set with symmetric difference

__examples__
```
s = {1, 2, 3}
s.add(4)
s.remove(2)
s.discard(5) # No error
s.pop()
s2 = s.copy()
s.union({5,6})
s.update({7,8})
s.intersection({3,4,7})
s.difference({1,7})
s.symmetric_difference({2,3,9})
```

## 3️⃣ Built-in Functions with Sets

- `len(set)` → Length
- `max(set)` → Maximum element
- `min(set)` → Minimum element
- `sum(set)` → Sum of elements (if numeric)
- `any(set)` → True if any element is True
- `all(set)` → True if all elements are True
- `sorted(set)` → Returns a new **sorted list**
- `set(iterable)` → Converts iterable to set

---

## Tips

- Sets **do not support indexing or slicing**
- Use sets for **fast membership testing**: `x in s`
- Sets are **mutable**, but elements must be **immutable**
- Useful for **removing duplicates** from lists: `unique = set(my_list)`
- Set operations (**union, intersection, difference**) are faster than looping through lists 

