# 🧠 Functions & Scope (Very Important for Interviews)

This is where many students become average or strong. No middle ground.

Below is your **Markdown-ready viva sheet**.

---

# 🐍 Python – Functions & Scope (Viva Q&A)

*(Commonly asked in interviews and coding rounds inspired by GeeksforGeeks and HackerRank)*

---

## 1️⃣ What is a function in Python?

**Answer:**

A function is a reusable block of code that performs a specific task.

It helps in:

* Code reusability
* Modularity
* Reducing repetition

Example:

```python
def greet():
    print("Hello")
```

---

## 2️⃣ What is the difference between a function and a method?

**Answer:**

* A **function** is defined independently.
* A **method** is a function associated with an object.

Example:

```python
def greet():   # function
    pass

a = "hello"
a.upper()      # method
```

---

## 3️⃣ What are function parameters and arguments?

**Answer:**

* **Parameter** → Variable in function definition.
* **Argument** → Value passed to function.

```python
def add(a, b):   # a, b → parameters
    return a + b

add(2, 3)        # 2, 3 → arguments
```

---

## 4️⃣ Types of Arguments in Python

### 🔹 Positional Arguments

Order matters.

### 🔹 Keyword Arguments

Specified using key=value.

### 🔹 Default Arguments

Provide default value.

```python
def greet(name="Guest"):
    print(name)
```

### 🔹 Variable-Length Arguments

#### *args → Multiple positional arguments

#### **kwargs → Multiple keyword arguments

---

## 5️⃣ What is `*args`?

**Answer:**

Allows passing multiple positional arguments as a tuple.

```python
def add(*args):
    return sum(args)
```

---

## 6️⃣ What is `**kwargs`?

**Answer:**

Allows passing multiple keyword arguments as a dictionary.

```python
def display(**kwargs):
    print(kwargs)
```

---

## 7️⃣ What is recursion?

**Answer:**

A function calling itself.

Used in:

* Factorial
* Fibonacci
* Tree traversal

Example:

```python
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)
```

---

## 8️⃣ What is a lambda function?

**Answer:**

A small anonymous function written in one line.

Syntax:

```python
lambda arguments : expression
```

Example:

```python
square = lambda x: x * x
```

---

## 9️⃣ Difference between map(), filter(), and reduce()

* **map()** → Transforms each element
* **filter()** → Filters elements
* **reduce()** → Reduces list to single value

---

## 🔟 What is scope in Python?

**Answer:**

Scope determines where a variable can be accessed.

Python follows **LEGB Rule**.

---

## 1️⃣1️⃣ What is LEGB Rule?

Python searches variables in this order:

1. **Local**
2. **Enclosing**
3. **Global**
4. **Built-in**

---

## 1️⃣2️⃣ What is a global variable?

Declared outside function and accessible everywhere.

```python
x = 10

def test():
    print(x)
```

---

## 1️⃣3️⃣ What is a local variable?

Declared inside function and accessible only there.

---

## 1️⃣4️⃣ What is a closure?

A function that remembers variables from its enclosing scope even after the outer function has finished execution.

---

## 1️⃣5️⃣ What is a decorator?

A function that modifies the behavior of another function.

Example:

```python
def decorator(func):
    def wrapper():
        print("Before function")
        func()
    return wrapper
```

---
