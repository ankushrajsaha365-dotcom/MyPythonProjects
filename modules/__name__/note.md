# __name__ == "__main__" in Python

## 1. What is `__name__`?

- `__name__` is a built-in special variable in Python.
- Python automatically assigns a value to it when a file is executed.

### Values of `__name__`

| Situation | Value |
|---------|------|
| File run directly | `"__main__"` |
| File imported | `"module_name"` |

---

## 2. Simple Demonstration

### demo.py
```python
print(__name__)

__output__

`"__main__"`
