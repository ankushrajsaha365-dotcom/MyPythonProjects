# 📘 Python List – Complete Notes

## 1️⃣ What is a List?
- **Ordered**, **mutable** collection of elements
- Allows **duplicates**
- Elements can be of **different types**

## 2️⃣ List Methods

- append(x) → Add element at end
- extend(iterable) → Add multiple elements
- insert(i, x) → Insert at index i
- remove(x) → Remove first occurrence
- pop([i]) → Remove & return element (last by default)
- clear() → Remove all elements
- index(x) → Index of first occurrence
- count(x) → Number of occurrences
- sort(reverse=False) → Sort in place
- reverse() → Reverse order in place
- copy() → Shallow copy

__examples__
```
a = [1, 2, 3]
a.append(4)
a.extend([5, 6])
a.insert(1, 10)
a.remove(2)
a.pop()
a.clear()
a.index(3)
a.count(1)
a.sort()
a.reverse()
b = a.copy()
```
### 3️⃣ Built-in Functions with Lists

-len(list) → Length
-max(list) → Maximum
-min(list) → Minimum
-sum(list) → Sum of elements
-sorted(list) → Returns new sorted list
-any(list) → True if any element is True
-all(list) → True if all elements are True
-enumerate(list) → Index & value pairs
-zip(list1, list2) → Combine multiple lists

### Tips

-Prefer append() over + for efficiency
-Use sorted() if original list must remain
-Use copy() instead of = to avoid reference issues
-Use enumerate() for index in loops