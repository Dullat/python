### **Type Conversion and Typecasting in Python**

In Python, **type conversion** (or **type casting**) is the process of converting one data type to another. Python provides built-in functions to do this explicitly. There are two main ways to handle type conversion:

1. **Implicit Type Conversion (Automatic)**
2. **Explicit Type Conversion (Manual)**

Let's dive into both. [[typecasting]] program

---

### 1. **Implicit Type Conversion (Automatic Type Conversion)**

- Python automatically converts one data type to another when necessary. This happens when a smaller data type is used in an operation with a larger data type.
- **Example**: If you add an integer and a float, Python will automatically convert the integer to a float before performing the operation.

#### Example:

```python
a = 5       # Integer
b = 3.2     # Float
result = a + b  # Implicit conversion of a to float
print(result)  # Output: 8.2
```

In this case, Python automatically converts the integer `5` to a float `5.0` to perform the addition.

#### Why it happens:

- **Type Promotion**: Python promotes a smaller data type to a larger one in an operation to avoid data loss or errors. For example, when an integer and a float are involved in a calculation, the integer is promoted to a float to ensure precision is maintained.

---

### 2. **Explicit Type Conversion (Manual Typecasting)**

Explicit type conversion requires the programmer to manually convert one data type into another using built-in functions. This is also known as **typecasting**.

Python provides several built-in functions for typecasting:

- `int()`: Converts a value to an integer.
- `float()`: Converts a value to a float.
- `str()`: Converts a value to a string.
- `bool()`: Converts a value to a boolean.
- `list()`: Converts a value to a list.
- `tuple()`: Converts a value to a tuple.
- `set()`: Converts a value to a set.
- `dict()`: Converts a value to a dictionary (in a specific format).

#### Examples:

**Converting from `float` to `int`:**

```python
x = 3.7
y = int(x)  # Converts 3.7 to 3 (decimal part is discarded)
print(y)  # Output: 3
```

**Converting from `int` to `float`:**

```python
x = 5
y = float(x)  # Converts 5 to 5.0
print(y)  # Output: 5.0
```

**Converting from `str` to `int` or `float`:**

```python
x = "12"
y = int(x)  # Converts the string "12" to the integer 12
print(y)  # Output: 12

z = "3.14"
w = float(z)  # Converts the string "3.14" to the float 3.14
print(w)  # Output: 3.14
```

**Converting from `int` to `str`:**

```python
x = 100
y = str(x)  # Converts the integer 100 to the string "100"
print(y)  # Output: "100"
```

**Converting from `int` to `bool`:**

```python
x = 0
y = bool(x)  # 0 is converted to False
print(y)  # Output: False

z = 1
w = bool(z)  # Any non-zero number is converted to True
print(w)  # Output: True
```

---

### 3. **Common Type Conversions**

|**From Type**|**To Type**|**Example**|**Result**|
|---|---|---|---|
|`int`|`float`|`float(10)`|`10.0`|
|`float`|`int`|`int(3.99)`|`3`|
|`str`|`int`|`int("25")`|`25`|
|`str`|`float`|`float("25.6")`|`25.6`|
|`bool`|`int`|`int(True)`|`1`|
|`int`|`bool`|`bool(0)`|`False`|
|`list`|`tuple`|`tuple([1, 2, 3])`|`(1, 2, 3)`|
|`tuple`|`list`|`list((1, 2, 3))`|`[1, 2, 3]`|
|`set`|`list`|`list({1, 2, 3})`|`[1, 2, 3]`|
|`str`|`list`|`list("hello")`|`['h', 'e', 'l', 'l', 'o']`|

---

### 4. **Error Handling in Type Conversion**

Type conversion can sometimes fail if the value cannot be converted into the target type. For example, trying to convert a string that does not represent a number into an integer will raise an error.

#### Example:

```python
x = "hello"
try:
    y = int(x)  # This will raise an error because "hello" cannot be converted to an integer
except ValueError:
    print("Cannot convert to int!")
```

Output:

```
Cannot convert to int!
```

This happens because `"hello"` is not a valid numeric string, so Python throws a `ValueError`.

### 5. **Type Conversion in Collections**

- **List to Tuple**:
    
    ```python
    list_data = [1, 2, 3]
    tuple_data = tuple(list_data)
    print(tuple_data)  # Output: (1, 2, 3)
    ```
    
- **Tuple to List**:
    
    ```python
    tuple_data = (1, 2, 3)
    list_data = list(tuple_data)
    print(list_data)  # Output: [1, 2, 3]
    ```
    
- **Set to List**:
    
    ```python
    set_data = {1, 2, 3}
    list_data = list(set_data)
    print(list_data)  # Output: [1, 2, 3] (Note: Order is not guaranteed in sets)
    ```
    

### 6. **Converting Between `str` and `bool`**

- **Empty strings are considered `False`**, and **non-empty strings are considered `True`** when converted to a boolean.
    
    ```python
    x = ""
    print(bool(x))  # Output: False
    
    y = "Non-empty"
    print(bool(y))  # Output: True
    ```
    

### 7. **Converting Between `int` and `bool`**

- Any non-zero integer is considered `True`, and `0` is considered `False` when converted to a boolean.
    
    ```python
    x = 0
    print(bool(x))  # Output: False
    
    y = 10
    print(bool(y))  # Output: True
    ```
    

---

### **Key Takeaways**:

- **Implicit Conversion** happens automatically when Python promotes a smaller data type to a larger one during operations.
- **Explicit Conversion** requires manual intervention using type conversion functions like `int()`, `float()`, `str()`, etc.
- **Common conversions** include `int` to `float`, `float` to `int`, `str` to `int`, and so on.
- Always handle possible errors during type conversion (e.g., using `try` and `except`), especially when converting between incompatible types.

Understanding and using type conversion and typecasting will allow you to manipulate and manage different data types in Python more effectively.