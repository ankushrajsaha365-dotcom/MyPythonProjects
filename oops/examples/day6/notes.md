# 🟦 Day 6 — Abstraction

 In Day 5 we learned:

> Same method name, different behavior (polymorphism)

Today we will learn:

> Forcing subclasses to implement required behavior.

That’s abstraction.

---

# 🧠 What Is Abstraction?

Simple definition:

> Hiding implementation details and forcing structure.

In real life:

* You can drive a car.
* You don’t need to know how the engine works.

You only interact with:

* Steering
* Brake
* Accelerator

That’s abstraction.

---

# 🔥 Why We Need It in OOP

Look at the Payment example from yesterday.

Right now, someone can do:

```python
p = Payment()
p.pay()
```

But Payment is just a concept.
It shouldn’t exist on its own.

We want to say:

> “You MUST implement pay() in child classes.”

That’s where abstraction comes in.

---

# 🟦 Abstract Class (The Proper Way)

Python provides a module called:

```
abc  → Abstract Base Class
```

It allows us to:

* Prevent instantiation of parent class
* Force child classes to override certain methods

---

# 🟢 Example: Payment System (Abstract Version)

```python
from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCard(Payment):
    def pay(self, amount):
        print(f"Processing credit card payment of {amount}")


class PayPal(Payment):
    def pay(self, amount):
        print(f"Redirecting to PayPal for {amount}")
```

Now:

```python
p = Payment()  ❌ ERROR
```

Python will stop you.

Why?
Because Payment is abstract.

---

# 🧠 What Just Happened?

Two important things:

### 1️⃣ `class Payment(ABC)`

Makes it abstract.

### 2️⃣ `@abstractmethod`

Forces subclasses to implement it.

If a child class forgets to define `pay()`:

Python throws an error.

That’s professional OOP safety.

---

# 🔥 Why This Is Powerful

Before abstraction:

* Developer might forget to override method.
* Parent method accidentally runs.

After abstraction:

* Python enforces design rules.

It protects your architecture.

---

# 🧭 When To Use Abstraction

Use it when:

* You are defining a template/base blueprint.
* The base class should NOT be used directly.
* You want to enforce required methods.

---

# 🧠 Difference So Far

| Concept      | What it does                    |
| ------------ | ------------------------------- |
| Inheritance  | Reuse structure                 |
| Polymorphism | Same method, different behavior |
| Abstraction  | Force required behavior         |


