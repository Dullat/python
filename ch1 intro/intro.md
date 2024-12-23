### Python Concepts: Notes from the Code You Provided

[[intro programe]]
#### 1. **Basic Output with `print()`**

- The `print()` function is used to display information on the screen.
- Example:
    
    ```python
    print("hello world")
    ```
    

#### 2. **Variables and Data Types**

- Variables store values of different data types, such as numbers, strings, booleans, etc.

**Common Data Types**:

- **Integer (`int`)**: Whole numbers (e.g., 13).
- **String (`str`)**: Text, enclosed in quotation marks (e.g., `"day"`).
- **Boolean (`bool`)**: Represents True or False values.
- **None**: A special value representing 'nothing' or 'no value'.

**Example**:

```python
age = 13        # Integer
word = "day"    # String
boolean = True  # Boolean
var = None      # NoneType
```

#### 3. **Variable Operations**

- You can perform arithmetic operations on variables.
- **Addition**: `age += 12` adds 12 to the existing value of `age`.

**Example**:

```python
age += 12  # age becomes 25
```

The `+=` operator in Python is called the **"addition assignment operator"** or simply **"compound assignment operator."**

#### 4. **Multiple Assignments**

- You can assign values to multiple variables in a single line.
- **Example**:

```python
A, B = "h", 3  # A gets 'h', B gets 3
```

#### 5. **String Multiplication**

- You can multiply a string by an integer to repeat it multiple times.
- **Example**:

```python
txt = "@"
print((A + txt) * B)  # Result: '@@@'
```

#### 6. **Checking Data Types with `type()`**

- The `type()` function returns the data type of a variable.
- **Example**:

```python
print(type(var))  # Output: <class 'NoneType'>
```

#### 7. **Arithmetic Operations**

- Python supports various arithmetic operations: `+`, `-`, `*`, `/`, `**` (exponentiation), and more.
- **Example**:

```python
print(-6 / 9)  # Output: -0.666...
print(2 ** 4)  # Output: 16 (2 raised to the power of 4)
```

#### 8. **String Input with `input()`**

- The `input()` function allows the user to enter data from the keyboard.
- The entered value is always stored as a string, so use `str()` to explicitly convert it to another type if needed.
- **Example**:

```python
name = str(input("name:"))  # Takes user input
print("my name is", name, "and my age is", age)
```

#### 9. **Boolean Operations (Logical Operators)**

- **`not`**, **`and`**, and **`or`** are logical operators used to perform boolean operations.

**Precedence (Order of Evaluation)**:

- `not` has the highest precedence.
- `and` has higher precedence than `or`.

**Example**:

```python
print(not True and False or True)  # Output: True
```

**Explanation of the Expression**:

1. `not True` evaluates to `False`.
2. `False and False` is `False`.
3. `False or True` is `True`.

#### 10. **Multiline Comments**

- You can write multiline comments using triple quotes `"""` or `'''`.
- These comments are ignored by the interpreter.
- **Example**:

```python
""" This is a multiline comment
    that spans across multiple lines. """
```

---

### Key Points:

- **Data Types**: Numbers, strings, booleans, and `None`.
- **Arithmetic**: `+`, `-`, `*`, `/`, `**` (Exponentiation), and modulus operations.
- **Boolean Operations**: Use `not`, `and`, and `or` for logical operations with precedence rules.
- **String Manipulation**: You can repeat strings using multiplication (`*`).
- **Input/Output**: Get input from the user with `input()` and output with `print()`.
- **Comments**: Use `#` for single-line comments and `"""..."""` for multiline comments.

This should give you a strong foundation for understanding the basics of Python! Keep practicing and experimenting with small code snippets to reinforce these concepts.