
# 📦 Stack – Concept (Python)

## 1️⃣ What is a Stack?

A **stack** is a linear data structure that follows the rule:

> **LIFO — Last In, First Out**

Think of:

* Stack of plates 🍽️
* Browser back button
* Undo (Ctrl + Z)

The **last item added** is the **first one removed**.

---

## 2️⃣ Basic Stack Operations

Every stack supports these core operations:

| Operation    | Meaning                 |
| ------------ | ----------------------- |
| `push`       | Add an element          |
| `pop`        | Remove top element      |
| `peek / top` | View top element        |
| `is_empty`   | Check if stack is empty |
| `size`       | Number of elements      |

---

## 3️⃣ Stack Implementation in Python (Using List)

Python **list** already works perfectly as a stack.

### ✅ Push (add element)

```python
stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print(stack)
```

**Output**

```
[10, 20, 30]
```

---

### ❌ Pop (remove top element)

```python
stack.pop()
print(stack)
```

**Output**

```
[10, 20]
```

> `pop()` removes the **last inserted element**

---

### 👀 Peek (top element)

```python
print(stack[-1])
```

---

### 🔍 Check if stack is empty

```python
print(len(stack) == 0)
```

---

### 📏 Stack size

```python
print(len(stack))
```

---

## 4️⃣ Real-Life Use Cases of Stack

✔ Undo / Redo
✔ Expression evaluation
✔ Function calls (call stack)
✔ Reversing a string
✔ Parenthesis checking

---