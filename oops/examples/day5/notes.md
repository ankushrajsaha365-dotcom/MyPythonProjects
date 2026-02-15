# 🟦 Day 5 — Polymorphism

This is where OOP starts feeling elegant.

---

# 🧠 What is Polymorphism?

Simple definition:

> Same method name, different behavior.

That’s it.

---

## Real-Life Meaning

Think about the word:

**Poly** = many
**Morph** = forms

So:

> One interface, many forms.

---

# 🔹 Example (Concept Only)

Imagine:

* Dog → makes sound "Bark"
* Cat → makes sound "Meow"
* Cow → makes sound "Moo"

They all have:

```
make_sound()
```

But each behaves differently.

That is polymorphism.

---

# 🔥 Why It Matters

Without polymorphism:

```python
if animal == "dog":
    ...
elif animal == "cat":
    ...
```

With polymorphism:

```python
animal.make_sound()
```

Cleaner. Scalable. Professional.

---

# 🟦 Two Types of Polymorphism in Python

We’ll focus on the important one:

### 1️⃣ Method Overriding (Inheritance-based)

Child class changes behavior of a method from parent.

---

# 🧠 Concept Structure

Parent class:

```
Vehicle → move()
```

Child classes:

```
Car → move()  # drives
Plane → move()  # flies
Boat → move()  # sails
```

Same method name.
Different implementation.

That’s Day 5.

---

# 🔹 Your First Day 5 Problem (Concept Only)

### Animal → Dog, Cat

Create:

* Parent class `Animal`

  * method `make_sound()`

* Child class `Dog`

  * override `make_sound()`

* Child class `Cat`

  * override `make_sound()`

When called:

* Dog makes bark
* Cat makes meow

Same method.
Different output.

---

# ⚠️ Important Rule

In overriding:

* Method name must be **exactly the same**
* Parameters must match

---

# 🧭 Before You Code

You should understand:

Inheritance = reuse structure
Polymorphism = change behavior

If inheritance is “same structure”
Polymorphism is “different behavior”
