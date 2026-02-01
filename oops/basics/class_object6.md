## 1️⃣ Class Definition

```python
class Wallet:
```

This creates a **blueprint** called `Wallet`.

Nothing runs yet.
It only defines **what a wallet has** and **what it can do**.

---

## 2️⃣ Constructor (`__init__`)

```python
def __init__(self, balance):
```

* Runs **automatically** when an object is created
* `self` → the current wallet object
* `balance` → value passed during object creation

---

### Balance Validation

```python
if balance >= 0:
    self.__balance = balance
else:
    self.__balance = 0
```

* Prevents negative balance
* Stores money **securely**
* `__balance` is **private**

🔒 Why private?

```python
wallet.__balance  # ❌ not allowed
```

So users **cannot cheat**.

---

## 3️⃣ Adding Money

```python
def add_money(self, amount):
```

This method:

* Takes money input
* Adds it to balance **safely**

---

### Validation

```python
if amount > 0:
    self.__balance += amount
```

* No zero or negative deposits
* Only valid money updates balance

Encapsulation principle in action.

---

## 4️⃣ Spending Money

```python
def spend_money(self, amount):
```

Controls money spending.

---

### Balance Check

```python
if amount <= self.__balance:
    self.__balance -= amount
```

* Prevents overdraft
* Protects object state

This is **data protection**, not just logic.

---

## 5️⃣ Showing Balance

```python
def show_balance(self):
    print("Current balance:", self.__balance)
```

* Balance is **read-only**
* No direct modification allowed

Good design.

---

## 6️⃣ Object Creation

```python
wallet = Wallet(500)
```

What happens internally:

1. Python creates a new object
2. Calls `__init__`
3. Sets `__balance = 500`

---

## 7️⃣ Method Calls

```python
wallet.add_money(200)
```

Balance: `500 → 700`

```python
wallet.spend_money(300)
```

Balance: `700 → 400`

```python
wallet.show_balance()
```

Output:

```
Current balance: 400
```

---

## 🧠 Big Picture Thinking (IMPORTANT)

| Part             | Purpose           |
| ---------------- | ----------------- |
| `__balance`      | Protect data      |
| Constructor      | Initialize safely |
| Methods          | Control behavior  |
| No direct access | Prevent misuse    |

This is **real OOP**, not syntax learning.

---

## 🔑 Key Rule to Remember Forever

> **Data is private, behavior is public**

