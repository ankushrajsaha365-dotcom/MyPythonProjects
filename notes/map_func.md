# 📌 Python `map()` Function

## ## 🔹 Definition

* `map()` applies a function to **each element** of an iterable
* Returns a **map object** (iterator)

---

## ## 🔹 Syntax

```python
map(function, iterable)
```

* To view output, convert it to:

  * `list()`
  * `tuple()`

```python
list(map(function, iterable))
```

---

## ## 🔹 Basic Example

```python
nums = [1, 2, 3]
result = list(map(lambda x: x * x, nums))
print(result)
```

### ### Output

```
[1, 4, 9]
```

---

## ## 🔹 Using Built-in Functions

```python
list(map(int, ["1", "2", "3"]))
list(map(str.upper, ["raj", "saha"]))
list(map(len, ["apple", "kiwi"]))
```

* Best use-case for **map()** ✔️

---

## ## 🔹 Using User-Defined Function

```python
def square(x):
    return x * x

list(map(square, [1, 2, 3]))
```

---

## ## 🔹 Multiple Iterables

```python
a = [1, 2, 3]
b = [4, 5, 6]

list(map(lambda x, y: x + y, a, b))
```

### ### Important

* Stops at the **shortest iterable**

---

## ## 🔹 `map()` vs List Comprehension

```python
# map()
list(map(lambda x: x * x, nums))

# list comprehension
[x * x for x in nums]
```

* List comprehension is often **more readable**

---

## ## 🔹 Common Mistakes ❌

```python
map(lambda x: x * x, nums)
```

* ❌ No output (iterator not consumed)

✔️ Correct:

```python
list(map(lambda x: x * x, nums))
```

---

## ## 🔹 When to Use `map()`?

* Applying an **existing function**
* Simple transformations
* No conditional logic

---

## ## 🔹 Key Points Summary

* Returns an **iterator**
* Memory efficient
* Faster for simple transformations
* For filtering → use `filter()`

---

