# 🐍 Python – Modules & Packages (Viva Questions & Answers)

*(Common interview patterns inspired by GeeksforGeeks and HackerRank)*

---

# 🔹 1️⃣ What is a Module in Python?

**Answer:**

A module is a Python file (`.py`) that contains:

* Functions
* Variables
* Classes

It helps in:

* Code reusability
* Better organization
* Modularity

Example:

If `math_utils.py` contains:

```python id="m1a9ks"
def add(a, b):
    return a + b
```

You can import it in another file.

---

# 🔹 2️⃣ How do you import a module?

### 🔹 Import entire module

```python id="k3s8dl"
import math
print(math.sqrt(16))
```

---

### 🔹 Import specific function

```python id="d8k2sl"
from math import sqrt
print(sqrt(16))
```

---

### 🔹 Import with alias

```python id="a7d9sm"
import math as m
print(m.pi)
```

---

# 🔹 3️⃣ What is the difference between:

```python id="r3j8sd"
import math
```

and

```python id="t7k2ls"
from math import *
```

**Answer:**

* `import math` → Access using `math.function()`
* `from math import *` → Imports everything into current namespace (not recommended)

Using `import math` is safer and avoids name conflicts.

---

# 🔹 4️⃣ What is `__name__ == "__main__"`?

**Answer:**

Every Python file has a special variable `__name__`.

* If file is run directly → `__name__ = "__main__"`
* If file is imported → `__name__ = module_name`

Example:

```python id="p4k9sl"
if __name__ == "__main__":
    print("Run directly")
```

Used to:

* Prevent code from running during import.

---

# 🔹 5️⃣ What is a Package?

**Answer:**

A package is a folder that contains multiple modules.

Example structure:

```
mypackage/
    __init__.py
    module1.py
    module2.py
```

It helps organize large projects.

---

# 🔹 6️⃣ What is `__init__.py`?

**Answer:**

* Marks a directory as a Python package.
* Can contain initialization code.

---

# 🔹 7️⃣ What are Built-in Modules?

Modules that come with Python.

Examples:

* `math`
* `random`
* `os`
* `sys`
* `datetime`

---

# 🔹 8️⃣ What is the difference between module and package?

| Module          | Package                   |
| --------------- | ------------------------- |
| Single .py file | Folder containing modules |
| Contains code   | Contains modules          |

---

# 🔹 9️⃣ What is PYTHONPATH?

**Answer:**

It is an environment variable that tells Python where to look for modules.

---

# 🔟 What happens when you import a module?

1. Python searches for the module.
2. Compiles it (if needed).
3. Executes module code.
4. Stores it in memory.
5. Reusing import doesn’t reload it.

---

# 🔥 Common Viva Trick Questions

1. Can two modules have same name?
2. What is circular import?
3. Difference between local module and third-party module?
4. Where are installed packages stored?
5. What is pip?

---

# 🎯 Viva Tip

When asked about modules:

Say:

1. Definition
2. Why needed
3. import types
4. **main** usage

That’s a complete answer.
