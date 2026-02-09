# 🚶‍♂️ QUEUE IN PYTHON

## Beginner → Intermediate

---

## 1️⃣ What is a Queue?

A **queue** is a linear data structure that follows:

> **FIFO — First In, First Out**

Real-life examples:

* People standing in a line 🧍🧍🧍
* Printer queue 🖨️
* Task scheduling (CPU)

```
Enqueue → [10, 20, 30] → Dequeue
```

---

## 2️⃣ Basic Queue Operations

| Operation | Meaning                   |
| --------- | ------------------------- |
| enqueue   | Add element at rear       |
| dequeue   | Remove element from front |
| front     | View first element        |
| rear      | View last element         |
| is_empty  | Check empty               |
| size      | Number of elements        |

---

## 🟢 LEVEL 1: Queue Using Python List (Beginner)

### ⚠️ Important Note

Using list is **not efficient**, but good for learning.

```python
queue = []

queue.append(10)   # enqueue
queue.append(20)
queue.append(30)

print(queue)

queue.pop(0)       # dequeue (slow ❌)
print(queue)
```

Why slow?

* `pop(0)` shifts all elements → O(n)

---

### 🔹Circular Queue Concept

Used in:

* CPU scheduling
* Buffers
* Streaming data



---

## 🧠 Stack vs Queue (Quick Compare)

| Feature       | Stack          | Queue              |
| ------------- | -------------- | ------------------ |
| Order         | LIFO           | FIFO               |
| Insert        | Top            | Rear               |
| Remove        | Top            | Front              |
| Python method | `append/pop()` | `append/popleft()` |

---
