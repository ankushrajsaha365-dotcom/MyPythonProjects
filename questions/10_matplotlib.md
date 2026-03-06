# 📊 Matplotlib – Viva Questions & Answers

*(Common Python data-visualization interview questions inspired by resources like GeeksforGeeks)*

---

# 🔹 1️⃣ What is Matplotlib?

**Answer:**

Matplotlib is a Python library used for **data visualization**.
It helps create graphs, charts, and plots from data.

Common uses:

* Line plots
* Bar charts
* Histograms
* Scatter plots
* Pie charts

---

# 🔹 2️⃣ What is the main module used in Matplotlib?

The main module is:

```python
matplotlib.pyplot
```

It is usually imported as:

```python
import matplotlib.pyplot as plt
```

---

# 🔹 3️⃣ What is a Line Plot?

A **line plot** is used to display data points connected by straight lines.

Example:

```python
import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,20,25,30]

plt.plot(x,y)
plt.show()
```

---

# 🔹 4️⃣ What does `plt.show()` do?

**Answer:**

`plt.show()` displays the plot window.

Without it, the graph may not appear.

---

# 🔹 5️⃣ What is a Bar Chart?

A **bar chart** represents categorical data using rectangular bars.

Example:

```python
import matplotlib.pyplot as plt

x = ["A","B","C"]
y = [10,20,15]

plt.bar(x,y)
plt.show()
```

---

# 🔹 6️⃣ What is a Histogram?

A **histogram** shows the distribution of numerical data.

Example:

```python
import matplotlib.pyplot as plt

data = [10,20,20,30,30,30,40]

plt.hist(data)
plt.show()
```

---

# 🔹 7️⃣ What is a Scatter Plot?

A **scatter plot** displays the relationship between two variables.

Example:

```python
import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,15,20,25]

plt.scatter(x,y)
plt.show()
```

---

# 🔹 8️⃣ How do you add a title to a plot?

```python
plt.title("Sample Graph")
```

Example:

```python
plt.plot(x,y)
plt.title("Sales Data")
plt.show()
```

---

# 🔹 9️⃣ How do you label axes?

```python
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
```

Example:

```python
plt.plot(x,y)
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()
```

---

# 🔹 🔟 What is `figure()` in Matplotlib?

`figure()` creates a new figure for plotting.

Example:

```python
plt.figure(figsize=(5,5))
```

---

# 🔹 1️⃣1️⃣ What is `subplot()`?

`subplot()` allows multiple plots in one figure.

Example:

```python
plt.subplot(1,2,1)
plt.plot([1,2,3],[4,5,6])

plt.subplot(1,2,2)
plt.plot([1,2,3],[6,5,4])

plt.show()
```

---

# 🔹 1️⃣2️⃣ What is a Pie Chart?

A **pie chart** represents data as slices of a circle.

Example:

```python
import matplotlib.pyplot as plt

data = [30,40,30]
labels = ["A","B","C"]

plt.pie(data, labels=labels)
plt.show()
```

---

# 🔹 1️⃣3️⃣ How do you save a plot?

```python
plt.savefig("plot.png")
```

This saves the plot as an image file.

---

# 🔹 1️⃣4️⃣ What are the advantages of Matplotlib?

* Easy to use
* Supports many plot types
* Highly customizable
* Works well with NumPy and Pandas

---

# 🔹 1️⃣5️⃣ Difference between Matplotlib and Seaborn

| Feature       | Matplotlib            | Seaborn             |
| ------------- | --------------------- | ------------------- |
| Level         | Low level             | High level          |
| Customization | More control          | Easier styling      |
| Built on      | Core plotting library | Built on Matplotlib |

---

# 🎯 Viva Tip (Important)

If a teacher asks **“Explain Matplotlib”**, say:

> Matplotlib is a Python data visualization library used to create graphs like line plots, bar charts, histograms, scatter plots, and pie charts. It works well with NumPy and Pandas for analyzing data visually.

That answer is usually enough for viva.

---
