# 📘 Python String – Complete Notes

## 1️⃣ What is a String?

- **Ordered**, **immutable** sequence of characters
- Can contain letters, numbers, symbols, or whitespace
- Strings are **immutable** → cannot be changed after creation
- Defined using **single `' '`**, **double `" "`**, or **triple quotes `''' '''` / `""" """`** for multi-line

---

## 2️⃣ String Methods

- **capitalize()** → Capitalizes first character
- **title()** → Capitalizes first letter of each word
- **lower() / upper()** → Convert to lower/upper case
- **strip() / lstrip() / rstrip()** → Remove whitespace
- **replace(old, new)** → Replace substring
- **split(sep=None)** → Split string into list
- **join(iterable)** → Join elements of iterable into a string
- **find(sub)** → Returns first index of substring (-1 if not found)
- **index(sub)** → Returns first index of substring (error if not found)
- **startswith(prefix)** → True if string starts with prefix
- **endswith(suffix)** → True if string ends with suffix
- **count(sub)** → Number of occurrences of substring
- **isalpha() / isdigit() / isspace()** → Checks content type
- **format()** → Format string with placeholders
- **f-strings** → Concise way to format strings (Python 3.6+)

__examples__
```
s = " hello World "
s.capitalize()
s.title()
s.lower()
s.upper()
s.strip()
s.replace("World", "Python")
s.split()
"-".join(["a","b","c"])
s.find("o")
s.index("o")
s.startswith("h")
s.endswith("d")
s.count("l")
"Name: {}".format("Raj")
name = "Raj"
f"Hello, {name}"
```


---

## 3️⃣ Built-in Functions with Strings

- `len(string)` → Length
- `max(string)` → Maximum character (ASCII)
- `min(string)` → Minimum character (ASCII)
- `any(string)` → True if any character is truthy
- `all(string)` → True if all characters are truthy
- `sorted(string)` → Returns sorted list of characters
- `str(object)` → Converts object to string
- `ord(char)` → Returns ASCII/Unicode of character
- `chr(int)` → Returns character from ASCII/Unicode value

---

## Tips

- Strings are **immutable**; use methods to create modified copies
- Use **triple quotes** for multi-line strings
- f-strings are **fastest and most readable** for variable insertion
- Use `split()` and `join()` for **parsing and combining text**
- Use **slicing** for substrings: `s[1:5]`, `s[::-1]` to reverse
- Strings support **concatenation**: `"Hello " + "World"`
- Strings support **repetition**: `"Hi " * 3` → `"Hi Hi Hi "`
