# 🐼 Pandas Library – Viva Questions & Answers

*(Common interview questions inspired by GeeksforGeeks and HackerRank)*

---

# 🔹 1️⃣ What is Pandas?

**Answer:**

Pandas is a Python library used for:

* Data analysis
* Data manipulation
* Handling structured data

It is built on top of **NumPy**.

---

# 🔹 2️⃣ Why is Pandas used?

Pandas is used for:

* Cleaning data
* Data transformation
* Handling missing values
* Data analysis
* Working with CSV / Excel files

---

# 🔹 3️⃣ What are the main data structures in Pandas?

Pandas has two main data structures:

| Data Structure | Description                              |
| -------------- | ---------------------------------------- |
| Series         | One-dimensional labeled array            |
| DataFrame      | Two-dimensional table (rows and columns) |

---

# 🔹 4️⃣ What is a Series?

A **Series** is a one-dimensional labeled array.

Example:

```python
import pandas as pd

s = pd.Series([10,20,30])
print(s)
```

Output:

```
0    10
1    20
2    30
```

---

# 🔹 5️⃣ What is a DataFrame?

A **DataFrame** is a two-dimensional table.

Example:

```python
import pandas as pd

data = {
    "Name": ["A", "B"],
    "Age": [20, 21]
}

df = pd.DataFrame(data)
print(df)
```

---

# 🔹 6️⃣ Difference between Series and DataFrame

| Feature   | Series         | DataFrame        |
| --------- | -------------- | ---------------- |
| Dimension | 1D             | 2D               |
| Structure | Single column  | Multiple columns |
| Use       | Small datasets | Large datasets   |

---

# 🔹 7️⃣ How do you read a CSV file in Pandas?

```python
df = pd.read_csv("data.csv")
```

Other formats:

* `read_excel()`
* `read_json()`
* `read_sql()`

---

# 🔹 8️⃣ How do you view first rows of data?

```python
df.head()
```

Last rows:

```python
df.tail()
```

---

# 🔹 9️⃣ How do you get information about a dataset?

```python
df.info()
```

Shows:

* column names
* data types
* missing values

---

# 🔹 🔟 How do you check statistics of a dataset?

```python
df.describe()
```

Shows:

* mean
* standard deviation
* min
* max
* quartiles

---

# 🔹 1️⃣1️⃣ How do you select a column?

```python
df["Age"]
```

Multiple columns:

```python
df[["Name","Age"]]
```

---

# 🔹 1️⃣2️⃣ What is indexing in Pandas?

Indexing allows accessing rows and columns.

Two common methods:

* `loc[]` → label based
* `iloc[]` → position based

Example:

```python
df.loc[0]
df.iloc[0]
```

---

# 🔹 1️⃣3️⃣ How do you handle missing values?

Common methods:

```python
df.dropna()
df.fillna(0)
```

---

# 🔹 1️⃣4️⃣ What is groupby()?

Used to group data based on a column.

Example:

```python
df.groupby("Department").sum()
```

---

# 🔹 1️⃣5️⃣ What is the shape of a DataFrame?

Returns number of rows and columns.

```python
df.shape
```

Example:

```
(100, 5)
```

→ 100 rows
→ 5 columns

---

# 🔥 Common Pandas Interview Questions

1. Difference between `loc` and `iloc`
2. Difference between `merge()` and `join()`
3. What is `groupby()` used for?
4. What is pivot table?
5. How does Pandas handle missing values?

---

# 🎯 Viva Tip

When explaining Pandas:

Say in order:

1️⃣ Built on NumPy
2️⃣ Used for data analysis
3️⃣ Two structures → Series & DataFrame
4️⃣ Supports CSV/Excel/SQL

That answer alone satisfies most viva questions.

---
