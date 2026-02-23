# 📂 File Handling in Python — Notes

---

# 🟦 1. What is File Handling?

File handling allows a program to:

* Read data from files
* Write data to files
* Append data
* Store data permanently

Without file handling:

> Data disappears when program stops.

With file handling:

> Data persists on disk.

---

# 🟦 2. Opening a File

Basic syntax:

```python
file = open("filename.txt", "mode")
```

Two arguments:

1. File name
2. Mode (how you want to use it)

---

# 🟦 3. File Modes

| Mode   | Meaning                           |
| ------ | --------------------------------- |
| `"r"`  | Read (default)                    |
| `"w"`  | Write (overwrites file)           |
| `"a"`  | Append (adds to file)             |
| `"x"`  | Create new file (error if exists) |
| `"rb"` | Read binary                       |
| `"wb"` | Write binary                      |

---

# 🟦 4. Reading from File

### 🔹 Read entire file

```python
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()
```

---

### 🔹 Read one line

```python
line = file.readline()
```

---

### 🔹 Read all lines into list

```python
lines = file.readlines()
```

---

# 🟦 5. Writing to File

### 🔹 Write (overwrites)

```python
file = open("data.txt", "w")
file.write("Hello World")
file.close()
```

⚠ If file exists → content erased.

---

# 🟦 6. Appending to File

```python
file = open("data.txt", "a")
file.write("\nNew Line")
file.close()
```

Adds content at end.

---

# 🟦 7. Closing a File

Always close file after use:

```python
file.close()
```

Why?

* Frees system resources
* Saves changes properly

---

# 🟦 8. Better Way — `with` Statement (Recommended)

Instead of manually closing:

```python
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
```

Why better?

* Automatically closes file
* Cleaner
* Safer

Professional code always uses `with`.

---

# 🟦 9. Checking if File Exists

```python
import os

if os.path.exists("data.txt"):
    print("File exists")
```

---

# 🟦 10. Common Errors

### ❌ FileNotFoundError

Trying to read a file that doesn't exist.

### ❌ PermissionError

No access permission.

### ❌ Forgetting to close file

May cause unexpected behavior.

---

# 🟦 11. Writing Multiple Lines

```python
lines = ["Hello\n", "World\n"]

with open("data.txt", "w") as file:
    file.writelines(lines)
```

---

# 🟦 12. File Handling Workflow

```
Open file
    ↓
Perform operation (read/write)
    ↓
Close file
```

or

```
Use with statement
```

---

# 🟦 13. Important Interview Concepts

* Difference between `read()`, `readline()`, `readlines()`
* Difference between `w` and `a`
* Why `with` is better
* What happens if file doesn’t exist in write mode

---

# 🟦 14. Real Use Cases

* Storing user data
* Logging systems
* Saving game progress
* CSV data processing
* Configuration files

---

# 🟦 15. Key Takeaways

* Files store persistent data
* Modes control file behavior
* Always close file (or use `with`)
* Writing with `"w"` deletes old data
* `"a"` preserves old data

---
