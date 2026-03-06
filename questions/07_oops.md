# 🐍 Python – OOP Viva Questions & Answers

*(Common interview patterns inspired by GeeksforGeeks and HackerRank)*

---

# 🔹 1️⃣ What is OOP?

**Answer:**

OOP (Object-Oriented Programming) is a programming paradigm based on objects and classes.

It focuses on:

* Reusability
* Modularity
* Data security

---

# 🔹 2️⃣ What are the four pillars of OOP?

1. Encapsulation
2. Abstraction
3. Inheritance
4. Polymorphism

---

# 🔹 3️⃣ What is a Class?

**Answer:**

A class is a blueprint for creating objects.

Example:

```python id="c1k9sd"
class Person:
    pass
```

---

# 🔹 4️⃣ What is an Object?

**Answer:**

An object is an instance of a class.

```python id="d8k3ls"
p1 = Person()
```

---

# 🔹 5️⃣ What is `__init__` method?

**Answer:**

It is a constructor method that runs automatically when an object is created.

```python id="a7k9sl"
class Person:
    def __init__(self, name):
        self.name = name
```

---

# 🔹 6️⃣ What is `self`?

**Answer:**

`self` refers to the current object.

It allows access to:

* Instance variables
* Instance methods

---

# 🔹 7️⃣ What are instance variables and class variables?

### 🔹 Instance Variable

Defined inside constructor using `self`.

Each object has its own copy.

### 🔹 Class Variable

Defined inside class but outside methods.

Shared by all objects.

---

# 🔹 8️⃣ What is Inheritance?

**Answer:**

Inheritance allows one class to acquire properties and methods of another class.

Example:

```python id="k2m9sd"
class Parent:
    pass

class Child(Parent):
    pass
```

---

# 🔹 9️⃣ Types of Inheritance in Python

1. Single
2. Multiple
3. Multilevel
4. Hierarchical

---

# 🔟 What is Method Overriding?

**Answer:**

When a child class provides its own implementation of a method already defined in parent class.

---

# 1️⃣1️⃣ What is Polymorphism?

**Answer:**

Polymorphism means "many forms".

Same method name behaves differently for different objects.

---

# 1️⃣2️⃣ What is Encapsulation?

**Answer:**

Binding data and methods together inside a class.

Achieved using:

* Private variables (`__var`)
* Getter and setter methods

---

# 1️⃣3️⃣ What is Abstraction?

**Answer:**

Hiding implementation details and showing only essential features.

In Python, done using:
`abc` module.

---

# 1️⃣4️⃣ What are Dunder (Magic) Methods?

Special methods that start and end with double underscores.

Examples:

* `__init__`
* `__str__`
* `__repr__`
* `__len__`

---

# 1️⃣5️⃣ What is Multiple Inheritance?

When a class inherits from more than one parent class.

---

# 🔥 Common OOP Trick Questions

1. Does Python support method overloading?
2. Difference between abstraction and encapsulation?
3. What is MRO (Method Resolution Order)?
4. What is super()?
5. Can constructor be private?

---

# 🎯 Viva Structure Tip

When answering OOP questions:

Say:

1. Definition
2. Why needed
3. Small example
4. Real-world analogy

That makes you sound mature, not memorized.
