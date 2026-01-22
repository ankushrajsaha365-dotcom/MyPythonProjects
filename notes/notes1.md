1️⃣ Input & Output Functions

| Function  | Description      |
| --------- | ---------------- |
| `print()` | Displays output  |
| `input()` | Takes user input |

## 2️⃣ Type Conversion Functions

| Function  | Converts To |
| --------- | ----------- |
| `int()`   | Integer     |
| `float()` | Float       |
| `str()`   | String      |
| `bool()`  | Boolean     |
| `list()`  | List        |
| `tuple()` | Tuple       |
| `set()`   | Set         |
| `dict()`  | Dictionary  |

```
x = int("10")
y = list("abc")
```

## 3️⃣ Mathematical Functions

| Function    | Description     |
| ----------- | --------------- |
| `abs()`     | Absolute value  |
| `pow(a, b)` | Power           |
| `round()`   | Rounds number   |
| `min()`     | Smallest value  |
| `max()`     | Largest value   |
| `sum()`     | Sum of elements |

```
abs(-5)        # 5
pow(2, 3)      # 8
sum([1,2,3])   # 6
```

## 4️⃣ Sequence & Iterable Functions

| Function      | Description        |
| ------------- | ------------------ |
| `len()`       | Length             |
| `range()`     | Sequence generator |
| `enumerate()` | Index + value      |
| `zip()`       | Combine iterables  |
| `sorted()`    | Sort items         |
| `reversed()`  | Reverse sequence   |

```
for i, v in enumerate(['a','b','c']):
    print(i, v)
```

## 5️⃣ Logical & Comparison Functions

| Function | Description                 |
| -------- | --------------------------- |
| `all()`  | True if all values are true |
| `any()`  | True if any value is true   |

```
all([True, True])    # True
any([False, True])  # True
```

## 6️⃣ Checking & Validation Functions

| Function       | Purpose           |
| -------------- | ----------------- |
| `type()`       | Returns data type |
| `isinstance()` | Type checking     |
| `id()`         | Memory address    |
| `callable()`   | Is callable       |

```
isinstance(5, int)  # True
```
## 7️⃣ Character & Number Functions

| Function | Description       |
| -------- | ----------------- |
| `ord()`  | Character → ASCII |
| `chr()`  | ASCII → Character |
| `bin()`  | Binary            |
| `oct()`  | Octal             |
| `hex()`  | Hexadecimal       |

```
ord('A')   # 65
chr(97)    # 'a'
```
## 8️⃣ Object & Memory Functions

| Function    | Description       |
| ----------- | ----------------- |
| `dir()`     | Object attributes |
| `vars()`    | Object variables  |
| `help()`    | Documentation     |
| `delattr()` | Delete attribute  |
| `getattr()` | Get attribute     |
| `setattr()` | Set attribute     |


```
help(str)
```

## 9️⃣ Functional Programming Functions

| Function   | Description                      |
| ---------- | -------------------------------- |
| `map()`    | Apply function                   |
| `filter()` | Filter values                    |
| `reduce()` | Reduce values *(from functools)* |
| `lambda`   | Anonymous function               |

```
list(map(lambda x: x*x, [1,2,3]))
```

## 🔟 Exception Handling Functions

| Function      | Description     |
| ------------- | --------------- |
| `raise`       | Raise exception |
| `Exception()` | Base exception  |

```
raise ValueError("Invalid input")
```

## 🔹 Special Built-ins (Advanced)

| Function    | Description         |
| ----------- | ------------------- |
| `eval()`    | Executes expression |
| `exec()`    | Executes code       |
| `compile()` | Compiles code       |


- ⚠️ Use carefully — security risk if input is untrusted.