# 🔗 LINKED LIST IN PYTHON

## Beginner → Practical Applications

---

## 1️⃣ What is a Linked List?

A **linked list** is a linear data structure where:

* Elements are **not stored contiguously** (unlike list)
* Each element (node) contains:

  * **Data**
  * **Reference (link)** to the next node

```
[data | next] → [data | next] → [data | None]
```

---

## 2️⃣ Why Linked List When Python Has List?

| Python List              | Linked List        |
| ------------------------ | ------------------ |
| Contiguous memory        | Non-contiguous     |
| Fast indexing            | No direct indexing |
| Slow insertion in middle | Fast insertion     |
| Fixed structure          | Dynamic size       |

👉 Use linked list when **insert/delete happens a lot**

---

## 3️⃣ Node Structure (CORE CONCEPT)

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

Every linked list is built from this.



