### Python Functions – Notes

Since you already have a solid understanding of functions in **C++** and **JavaScript**, we’ll focus on the key differences and Python-specific features while covering the basic concepts as well.

---

### 1. **Basic Function Definition in Python**

In Python, functions are defined using the `def` keyword. A function is a block of code that only runs when it is called.

#### Syntax:

```python
def function_name(parameters):
    # function body
    return value
```

- **`function_name`**: Name of the function.
- **`parameters`**: Optional, the inputs the function takes (like arguments in C++/JavaScript).
- **`return`**: The function can return a value. If no `return` is used, the function returns `None` by default.

#### Example:

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
```

**Output:**

```
Hello, Alice!
```

### 2. **Function Arguments**

#### Positional Arguments:

Just like in C++ and JavaScript, Python allows you to pass arguments by position.

```python
def add(a, b):
    return a + b

result = add(3, 4)  # Positional arguments
print(result)
```

**Output:**

```
7
```

#### Default Arguments:

One feature that is unique to Python is **default arguments**. If an argument is not passed, the function will use the default value.

```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()        # Uses default value
greet("John")  # Overrides default value
```

**Output:**

```
Hello, Guest!
Hello, John!
```

#### Keyword Arguments:

You can pass arguments by explicitly specifying their name.

```python
def greet(name, age):
    print(f"Hello, {name}. You are {age} years old.")

greet(name="Alice", age=30)  # Using keyword arguments
```

**Output:**

```
Hello, Alice. You are 30 years old.
```

#### Arbitrary Arguments (Using `*args` and `**kwargs`):

Python provides the `*args` and `**kwargs` to handle an arbitrary number of arguments.

- `*args`: Used for **non-keyword arguments** (variable number of positional arguments).
- `**kwargs`: Used for **keyword arguments** (variable number of named arguments).

##### Example of `*args`:

```python
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4, 5))  # Passes any number of positional arguments
```

**Output:**

```
15
```

##### Example of `**kwargs`:

```python
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Alice", age=30, city="Wonderland")
```

**Output:**

```
name: Alice
age: 30
city: Wonderland
```

---

### 3. **Returning Values**

In Python, you can return any object from a function, including lists, tuples, dictionaries, or even other functions.

#### Example:

```python
def get_square_and_cube(x):
    return x**2, x**3  # Returning a tuple

square, cube = get_square_and_cube(4)
print(f"Square: {square}, Cube: {cube}")
```

**Output:**

```
Square: 16, Cube: 64
```

---

### 4. **Lambda Functions (Anonymous Functions)**

A **lambda function** is a small anonymous function that can take any number of arguments, but can only have one expression. It is useful for small, one-time tasks.

#### Syntax:

```python
lambda arguments: expression
```

#### Example:

```python
square = lambda x: x ** 2
print(square(5))
```

**Output:**

```
25
```

---

### 5. **Scope and Lifetime of Variables**

In Python, the scope of a variable determines where it can be accessed.

- **Global Scope**: Variables declared outside any function are global and can be accessed anywhere in the program.
- **Local Scope**: Variables declared inside a function are local and can only be accessed within that function.

#### Example:

```python
x = 10  # Global variable

def foo():
    y = 20  # Local variable
    print(f"Inside foo, x={x}, y={y}")

foo()
# print(y)  # This will raise an error since y is local to foo()
```

**Output:**

```
Inside foo, x=10, y=20
```

---

### 6. **Global and Nonlocal Keywords**

In Python, you can modify variables that are in the global scope from within a function using the `global` keyword. Similarly, you can modify variables in an enclosing function’s scope using the `nonlocal` keyword.

#### Example with `global`:

```python
x = 10

def change_global():
    global x
    x = 20

change_global()
print(x)  # Now x is 20
```

**Output:**

```
20
```

#### Example with `nonlocal`:

```python
def outer_function():
    x = 10
    
    def inner_function():
        nonlocal x
        x = 20
    
    inner_function()
    print(x)

outer_function()
```

**Output:**

```
20
```

---

### 7. **Recursive Functions**

Python also supports **recursion**, where a function calls itself.

#### Example:

```python
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))
```

**Output:**

```
120
```

Recursion is powerful, but be cautious of stack overflow errors for very large recursion depths.

---

### 8. **Difference Between Python Functions and Functions in C++/JavaScript**

#### 1. **No Need for Type Declarations**:

In Python, you don’t need to declare the types of the parameters or the return type explicitly (unlike C++ or JavaScript). Python uses dynamic typing.

#### 2. **Return is Optional**:

Functions in Python do not require a return statement. If there is no return statement, `None` is returned by default.

#### 3. **First-Class Functions**:

Functions in Python are first-class objects, meaning they can be assigned to variables, passed as arguments, or returned from other functions.

#### 4. **Function Overloading**:

Python doesn’t support function overloading like C++. Instead, it uses default arguments, `*args`, and `**kwargs` to achieve similar behavior.

#### 5. **Anonymous Functions (Lambda)**:

Python’s lambda functions are syntactically different from JavaScript’s anonymous functions and C++'s lambda expressions, though they serve a similar purpose.

---

### Example Program Using Functions in Python

```python
# A simple function that adds two numbers
def add(a, b):
    return a + b

# A function with default argument
def greet(name="Guest"):
    print(f"Hello, {name}!")

# A function with arbitrary number of arguments
def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

# A recursive function to calculate factorial
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Main execution
if __name__ == "__main__":
    print(add(10, 5))           # Outputs 15
    greet("Alice")              # Outputs "Hello, Alice!"
    greet()                     # Outputs "Hello, Guest!"
    print(multiply(2, 3, 4))    # Outputs 24
    print(factorial(5))         # Outputs 120
```

**Output:**

```
15
Hello, Alice!
Hello, Guest!
24
120
```

---

### Summary of Python Functions

- Functions are defined using `def`.
- Python functions support default, arbitrary, and keyword arguments.
- Functions return `None` by default if no `return` is used.
- Python supports anonymous functions via `lambda`.
- You can use `global` and `nonlocal` to modify variable scopes.
- Python functions are more flexible and concise compared to C++/JavaScript, with dynamic typing and easy handling of variable arguments.

Let me know if you need further elaboration on any point!