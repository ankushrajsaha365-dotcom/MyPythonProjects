---

### CONSTRUCTOR IN PYTHON ( `__init__` )

---

1. What is a Constructor?

A constructor is a **special method** that is called **automatically**
when an object of a class is created.

In Python, the constructor method is named:

`__init__`

It is used to **initialize (set up) object data**.

---

2. Why do we need a Constructor?

Without a constructor:

* Attributes must be added manually
* Code becomes error-prone
* Objects may exist without proper data

With a constructor:

* Object is created with required data
* Code becomes clean and safe
* Initialization happens automatically

---

3. Basic Syntax of a Constructor
```
class ClassName:
    def __init__(self, parameters):
        self.variable = value

```
Example:
```
class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

s1 = Student("Raj", 1)
```
---

4. What does self mean?

* self refers to the **current object**
* It is used to access variables and methods of that object
* Each object has its own self

Example:
```
s1 = Student("Raj", 1)
s2 = Student("Aman", 2)
```
self.name for s1 → "Raj"
self.name for s2 → "Aman"

---

5. Constructor is Called Automatically

You do NOT call the constructor manually.

This is wrong:
``s1.__init__("Raj", 1)``

This is correct:
``s1 = Student("Raj", 1)``

Python calls __init__ internally.

---

6. Instance Variables vs Local Variables

Instance Variables:

* Defined using self
* Belong to the object
* Accessible in all methods

Local Variables:

* Defined without self
* Exist only inside a method

Example:
```
class Demo:
    def __init__(self):
        self.x = 10   # instance variable
        y = 5         # local variable
```
---

7. Constructor with Methods

Constructor sets data,
methods use that data.

Example:
```
class BankAccount:
    def __init__(self, balance):
        self.balance = balance


    def show_balance(self):
        print(self.balance)
```

---

8. Multiple Objects, Same Constructor

One constructor can create many objects.

Example:
```
s1 = Student("Raj", 1)
s2 = Student("Aman", 2)
s3 = Student("Neha", 3)
```
Each object stores its own data.

---

9. Key Points to Remember

* `__init__` is not mandatory, but recommended
* Constructor runs only once per object
* Constructor name must be exactly `__init__`
* self is mandatory as the first parameter
* Constructors help write clean OOP code

---

10. Common Beginner Mistakes

* Forgetting self
* Thinking constructor is a normal function
* Trying to call `__init__` directly
* Using class variables instead of instance variables

---

*FINAL SUMMARY*

Constructor (`__init__`) is used to initialize object data.
It runs automatically when an object is created.
It makes code safer, cleaner, and easier to maintain.

---
