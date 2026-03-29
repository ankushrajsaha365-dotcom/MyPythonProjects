# 🐼 Pandas Basic Notes

## 📌 1. What is Pandas?

* A Python library for **data analysis & manipulation**
* Works mainly with **tables (rows & columns)**
* Built on **NumPy**

---

## 📦 2. Importing Pandas

```python
import pandas as pd
```

---

## 🧱 3. Core Data Structures

### 🔹 Series (1D)

* Like a column

```python
s = pd.Series([10, 20, 30])
```

With index:

```python
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
```

---

### 🔹 DataFrame (2D)

* Like a table

```python
df = pd.DataFrame({
    'name': ['Raj', 'Sam'],
    'age': [21, 22]
})
```

---

## 📥 4. Reading Data

```python
df = pd.read_csv("file.csv")
df = pd.read_excel("file.xlsx")
```

---

## 📤 5. Writing Data

```python
df.to_csv("output.csv")
df.to_excel("output.xlsx")
```

---

## 🔍 6. Viewing Data

```python
df.head()      # first 5 rows
df.tail()      # last 5 rows
df.info()      # structure
df.describe()  # statistics
df.shape       # (rows, cols)
df.columns     # column names
```

---

## 🎯 7. Selecting Data

### 🔹 Select Column

```python
df['name']
df[['name', 'age']]
```

---

### 🔹 Select Rows

```python
df.loc[0]      # by label
df.iloc[0]     # by index
```

---

### 🔹 Filtering

```python
df[df['age'] > 21]
```

Multiple condition:

```python
df[(df['age'] > 20) & (df['age'] < 25)]
```

---

## ✏️ 8. Adding & Modifying Data

### Add Column

```python
df['salary'] = [1000, 2000]
```

---

### Modify Column

```python
df['age'] = df['age'] + 1
```

---

### Apply Function

```python
df['age'] = df['age'].apply(lambda x: x + 5)
```

---

## ❌ 9. Deleting Data

```python
df.drop('age', axis=1)        # column
df.drop(0, axis=0)           # row
```

---

## 🧹 10. Handling Missing Values

```python
df.isnull()
df.isnull().sum()
```

### Remove Missing Data

```python
df.dropna()
```

---

### Fill Missing Data

```python
df.fillna(0)
df.fillna(method='ffill')   # forward fill
```

---

## 🔄 11. Sorting Data

```python
df.sort_values(by='age')
df.sort_values(by='age', ascending=False)
```

---

## 🔁 12. GroupBy (Important)

```python
df.groupby('department')['salary'].mean()
```

👉 Used for aggregation

---

## 🔗 13. Merging DataFrames

```python
pd.merge(df1, df2, on='id')
```

Types:

* inner
* left
* right
* outer

---

## 🔄 14. Indexing

```python
df.set_index('name')
df.reset_index()
```

---

## 🧮 15. Basic Operations

```python
df['age'].mean()
df['age'].sum()
df['age'].min()
df['age'].max()
```

---

## 🔤 16. String Operations

```python
df['name'].str.lower()
df['name'].str.upper()
```

---

## 📅 17. Date Handling

```python
df['date'] = pd.to_datetime(df['date'])
```

---

## ⚡ 18. Useful Functions Summary

| Function   | Use             |
| ---------- | --------------- |
| head()     | first rows      |
| tail()     | last rows       |
| info()     | structure       |
| describe() | stats           |
| loc        | label selection |
| iloc       | index selection |
| groupby()  | grouping        |
| merge()    | combine data    |

---

## ⚠️ Common Mistakes (Important)

❌ Forgetting `axis` in drop
❌ Using loops instead of vectorization
❌ Confusing `loc` vs `iloc`
❌ Not handling missing values

---

## 🧠 Quick Revision Tips

* DataFrame = table
* Series = column
* `loc` = label
* `iloc` = index
* `groupby` = split + apply + combine

---

