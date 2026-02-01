# 📘 OOP PROPERTIES (Python – Day 3)

There are **4 core OOP properties**:

1️⃣ Encapsulation
2️⃣ Abstraction
3️⃣ Inheritance
4️⃣ Polymorphism

We’ll go **one by one**, with *simple Python examples* — no overload.

---

## 1️⃣ Encapsulation (MOST IMPORTANT FIRST)

### 🔹 Meaning (simple)

**Binding data and methods together**, and protecting data from direct misuse.

> “Data should not be freely modified from outside the class.”

---

### ❌ Without Encapsulation (bad)

```python
balance = 1000
balance = -500   # allowed (wrong)
```

---

### ✅ With Encapsulation

```python
class Account:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")
```

✔ Data (`balance`)
✔ Methods (`withdraw`)
✔ Controlled access

That’s encapsulation.

---

### 🔐 Access Levels in Python

| Type      | Syntax     | Meaning                   |
| --------- | ---------- | ------------------------- |
| Public    | `self.x`   | Accessible everywhere     |
| Protected | `self._x`  | Internal use (convention) |
| Private   | `self.__x` | Name mangling             |

```python
self.__pin = 1234
```

(Advanced, don’t overuse yet)

---

## 2️⃣ Abstraction (HIDE COMPLEXITY)

### 🔹 Meaning

Show **what** an object does, not **how** it does it.

---

### Real-life example

You press **brake**
You don’t care how hydraulics work.

---

### Python Example

```python
class ATM:
    def withdraw(self):
        self.__validate()
        self.__deduct()

    def __validate(self):
        pass

    def __deduct(self):
        pass
```

User only sees:

```python
atm.withdraw()
```

Details are hidden.

👉 In Python, abstraction is mostly done via:

* method design
* private methods
* later: abstract base classes

---

## 3️⃣ Inheritance (REUSE CODE)

### 🔹 Meaning

A class can **inherit** features of another class.

---

### Example

```python
class Person:
    def speak(self):
        print("I can speak")

class Student(Person):
    def study(self):
        print("I study")
```

Usage:

```python
s = Student()
s.speak()   # inherited
s.study()
```

✔ Avoids code duplication
✔ Logical hierarchy

---

### When NOT to use inheritance

❌ Just to “reuse code”
❌ When classes are not logically related

Use it only when **IS-A relationship** exists.

---

## 4️⃣ Polymorphism (SAME NAME, DIFFERENT BEHAVIOR)

### 🔹 Meaning

Same method name, different behavior.

---

### Example

```python
class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")
```

```python
animals = [Dog(), Cat()]
for a in animals:
    a.sound()
```

Same method → different output.

---

### Method Overriding (important)

```python
class Parent:
    def show(self):
        print("Parent")

class Child(Parent):
    def show(self):
        print("Child")
```

Child version **overrides** parent.

---


## ✅ Quick Summary

| Property      | Purpose                 |
| ------------- | ----------------------- |
| Encapsulation | Protect & organize data |
| Abstraction   | Hide complexity         |
| Inheritance   | Reuse code              |
| Polymorphism  | Flexible behavior       |

---

