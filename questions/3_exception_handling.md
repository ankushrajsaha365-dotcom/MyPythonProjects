# 🐍 Python – Exception Handling (Viva Q&A)

*(Common interview patterns inspired by GeeksforGeeks and HackerRank)*

---

## 1️⃣ What is an Exception?

**Answer:**

An exception is an error that occurs during program execution (runtime error).

When an exception occurs:

* The normal flow of the program stops.
* Python generates an error object.
* If not handled, the program terminates.

Example:

```python id="a1x9pq"
x = 10 / 0   # ZeroDivisionError
```

---

## 2️⃣ What is Exception Handling?

**Answer:**

Exception handling is a mechanism to handle runtime errors gracefully without stopping the program.

It uses:

* `try`
* `except`
* `else`
* `finally`

---

## 3️⃣ Basic Syntax of try-except

```python id="pq93ms"
try:
    # risky code
    x = int(input("Enter number: "))
except ValueError:
    print("Invalid input")
```

---

## 4️⃣ What is the purpose of `try` block?

Code that may cause an exception is placed inside the `try` block.

---

## 5️⃣ What is the purpose of `except` block?

Handles the exception if it occurs.

You can handle:

* Specific exception
* Multiple exceptions
* All exceptions

Example:

```python id="b8n2df"
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

---

## 6️⃣ What is `else` block in exception handling?

**Answer:**

The `else` block executes only if no exception occurs.

```python id="w0s8pl"
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Error")
else:
    print("Success")
```

---

## 7️⃣ What is `finally` block?

**Answer:**

The `finally` block always executes, whether exception occurs or not.

Used for:

* Closing files
* Releasing resources
* Database connections

```python id="t3ln5d"
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Error")
finally:
    print("Always runs")
```

---

## 8️⃣ Difference between Syntax Error and Exception

| Syntax Error              | Exception               |
| ------------------------- | ----------------------- |
| Detected before execution | Occurs during execution |
| Stops program immediately | Can be handled          |
| Example: Missing colon    | Example: Divide by zero |

---

## 9️⃣ How to handle multiple exceptions?

```python id="r7mt9q"
try:
    x = int(input())
    y = 10 / x
except (ValueError, ZeroDivisionError):
    print("Error occurred")
```

---

## 🔟 What is the use of `raise` keyword?

**Answer:**

Used to manually raise an exception.

```python id="h9d3wr"
age = -5
if age < 0:
    raise ValueError("Age cannot be negative")
```

---

## 1️⃣1️⃣ What is a custom exception?

**Answer:**

User-defined exception created by inheriting from `Exception`.

Example:

```python id="v5md0z"
class BankError(Exception):
    pass

raise BankError("Insufficient balance")
```

---

## 1️⃣2️⃣ What happens if an exception is not handled?

* Program terminates
* Error traceback is displayed

---

## 1️⃣3️⃣ What is Exception Hierarchy?

All exceptions inherit from:

`BaseException`
→ `Exception`
→ Specific exceptions (ValueError, TypeError, etc.)

---

## 1️⃣4️⃣ Difference between `Exception` and `BaseException`

* `BaseException` is the root class.
* `Exception` is used for most user-defined errors.
* SystemExit and KeyboardInterrupt inherit directly from BaseException.

---

# 🎯 Important Viva Tip

When answering:

Say:

1. Definition
2. Why needed
3. Small example

That structure makes you sound confident.

---

# 🔥 Practice Question for You

Explain this code clearly:

```python
try:
    print(10 / 2)
except ZeroDivisionError:
    print("Error")
else:
    print("Success")
finally:
    print("Done")
```
