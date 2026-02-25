# 🐍 Python – File Handling (Viva Questions & Answers)

*(Commonly asked in interviews inspired by GeeksforGeeks and HackerRank)*

---

## 1️⃣ What is File Handling in Python?

**Answer:**

File handling allows us to:

* Create files
* Read files
* Write files
* Append data
* Delete files

It helps in storing data permanently (persistent storage).

---

## 2️⃣ How do you open a file in Python?

**Answer:**

Using the `open()` function.

Syntax:

```python id="a1k3ds"
file = open("filename.txt", "mode")
```

---

## 3️⃣ What are the different file modes?

| Mode   | Meaning                 |
| ------ | ----------------------- |
| `"r"`  | Read (default)          |
| `"w"`  | Write (overwrites file) |
| `"a"`  | Append                  |
| `"x"`  | Create new file         |
| `"rb"` | Read binary             |
| `"wb"` | Write binary            |

---

## 4️⃣ What is the difference between `"w"` and `"a"` mode?

**"w" mode**

* Overwrites existing content
* Creates file if not present

**"a" mode**

* Adds content at the end
* Does not delete existing data

---

## 5️⃣ How do you read data from a file?

### 🔹 read()

Reads entire content.

```python id="c7ghp9"
file = open("data.txt", "r")
print(file.read())
file.close()
```

### 🔹 readline()

Reads one line at a time.

### 🔹 readlines()

Reads all lines into a list.

---

## 6️⃣ Why should we close a file?

**Answer:**

To:

* Free system resources
* Save changes properly
* Prevent memory leaks

---

## 7️⃣ What is the better way to open a file?

**Answer:**

Using `with` statement (context manager).

```python id="b2m9ds"
with open("data.txt", "r") as file:
    print(file.read())
```

It automatically closes the file.

---

## 8️⃣ What is a context manager?

**Answer:**

A context manager manages resources automatically.

In file handling:

* Opens file
* Closes file automatically

---

## 9️⃣ What happens if you open a file in `"r"` mode and file does not exist?

**Answer:**

It raises:
`FileNotFoundError`

---

## 🔟 What happens if you open a file in `"w"` mode and file exists?

**Answer:**

The existing content is erased.

---

## 1️⃣1️⃣ What is the difference between text mode and binary mode?

**Text mode (`"r"`)**

* Reads text
* Returns string

**Binary mode (`"rb"`)**

* Reads raw bytes
* Used for images, PDFs, etc.

---

## 1️⃣2️⃣ How do you write to a file?

```python id="n3q9tk"
with open("data.txt", "w") as file:
    file.write("Hello World")
```

---

## 1️⃣3️⃣ What is file pointer?

**Answer:**

The file pointer indicates the current position in the file.

You can move it using:

```python id="g9hd2p"
file.seek(position)
```

Check current position:

```python id="m8dj2r"
file.tell()
```

---

## 1️⃣4️⃣ What is the difference between read(), readline(), and readlines()?

| Method      | Output        |
| ----------- | ------------- |
| read()      | Full content  |
| readline()  | Single line   |
| readlines() | List of lines |

---

## 1️⃣5️⃣ What is buffering in file handling?

**Answer:**

Buffering temporarily stores data before writing to file to improve performance.

---

# 🎯 Viva Tip

When asked about file handling:

Say:

1. Purpose
2. open() syntax
3. Modes
4. with statement
5. Why close is important

That’s a complete answer.

