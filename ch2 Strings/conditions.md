### **Python Conditional Statements: Notes**

Conditional statements allow you to execute different blocks of code based on certain conditions. In Python, these are primarily implemented using `if`, `elif`, and `else` statements. [[condition program]]

### **1. `if` Statement**

The `if` statement is used to test a condition. If the condition is **True**, the code block under the `if` statement will be executed.

- **Syntax**:
    
    ```python
    if condition:
        # code to execute if condition is True
    ```
    
- **Example**:
    
    ```python
    age = 18
    if age >= 18:
        print("You are an adult.")
    ```
    

#### Output:

```
You are an adult.
```

### **2. `else` Statement**

The `else` statement is used to execute a block of code if the `if` condition is **False**. It is optional but must follow an `if` statement or an `elif` statement.

- **Syntax**:
    
    ```python
    if condition:
        # code to execute if condition is True
    else:
        # code to execute if condition is False
    ```
    
- **Example**:
    
    ```python
    age = 16
    if age >= 18:
        print("You are an adult.")
    else:
        print("You are a minor.")
    ```
    

#### Output:

```
You are a minor.
```

### **3. `elif` Statement**

`elif` stands for "else if". It allows you to check multiple conditions. If the first `if` condition is **False**, Python will check the `elif` condition. If that’s also **False**, it will check the next `elif` (if any), and so on. If none of the `if` or `elif` conditions are met, the `else` block will be executed.

- **Syntax**:
    
    ```python
    if condition1:
        # code if condition1 is True
    elif condition2:
        # code if condition2 is True
    else:
        # code if none of the conditions are True
    ```
    
- **Example**:
    
    ```python
    age = 20
    if age >= 65:
        print("You are a senior citizen.")
    elif age >= 18:
        print("You are an adult.")
    else:
        print("You are a minor.")
    ```
    

#### Output:

```
You are an adult.
```

### **4. **Comparison Operators**

Conditional statements often involve comparing values. Python provides several **comparison operators** to compare values:

- **`==`**: Equal to
- **`!=`**: Not equal to
- **`>`**: Greater than
- **`<`**: Less than
- **`>=`**: Greater than or equal to
- **`<=`**: Less than or equal to

#### Example:

```python
x = 5
if x == 5:
    print("x is equal to 5")
elif x != 5:
    print("x is not equal to 5")
```

#### Output:

```
x is equal to 5
```

### **5. Logical Operators**

You can combine multiple conditions using **logical operators**:

- **`and`**: Returns `True` if both conditions are true
- **`or`**: Returns `True` if at least one condition is true
- **`not`**: Inverts the result of the condition (True becomes False, and vice versa)

#### Examples:

- **`and` Operator**:
    
    ```python
    age = 25
    if age >= 18 and age <= 30:
        print("You are between 18 and 30 years old.")
    ```
    
    #### Output:
    
    ```
    You are between 18 and 30 years old.
    ```
    
- **`or` Operator**:
    
    ```python
    age = 16
    if age < 18 or age > 65:
        print("You are eligible for a discount.")
    ```
    
    #### Output:
    
    ```
    You are eligible for a discount.
    ```
    
- **`not` Operator**:
    
    ```python
    age = 20
    if not age < 18:
        print("You are an adult.")
    ```
    
    #### Output:
    
    ```
    You are an adult.
    ```
    

### **6. Nested Conditional Statements**

You can place conditional statements inside other conditional statements. This is known as **nested conditionals**.

- **Example**:
    
    ```python
    age = 25
    if age >= 18:
        print("You are an adult.")
        if age >= 65:
            print("You are a senior citizen.")
        else:
            print("You are a middle-aged adult.")
    else:
        print("You are a minor.")
    ```
    

#### Output:

```
You are an adult.
You are a middle-aged adult.
```

### **7. Short-circuit Evaluation**

When using logical operators like `and` and `or`, Python evaluates the conditions from left to right and stops as soon as the result is determined. This is known as **short-circuit evaluation**.

- **For `and`**: If the first condition is `False`, Python won't check the second condition because the overall result will be `False` anyway.
    
- **For `or`**: If the first condition is `True`, Python won't check the second condition because the overall result will be `True` anyway.
    

#### Example:

```python
x = 5
y = 0
if x > 0 and y > 0:
    print("Both x and y are positive.")
else:
    print("At least one of x or y is not positive.")
```

#### Output:

```
At least one of x or y is not positive.
```

### **8. Conditional Expressions (Ternary Operator)**

In Python, you can use a shorthand for `if`-`else` using a **ternary operator**. It allows you to assign a value based on a condition.

- **Syntax**:
    
    ```python
    result = value_if_true if condition else value_if_false
    ```
    
- **Example**:
    
    ```python
    age = 20
    status = "Adult" if age >= 18 else "Minor"
    print(status)
    ```
    

#### Output:

```
Adult
```

### **9. Membership Operators**

Membership operators are used to test if a sequence (like a string, list, or tuple) contains a certain element.

- **`in`**: Returns `True` if the element is found in the sequence.
- **`not in`**: Returns `True` if the element is **not** found in the sequence.

#### Example:

```python
fruit = "apple"
if "a" in fruit:
    print("The letter 'a' is in apple.")
```

#### Output:

```
The letter 'a' is in apple.
```

### **10. Identity Operators**

Identity operators are used to compare the **memory location** of two objects, not their values.

- **`is`**: Returns `True` if both variables point to the same object in memory.
- **`is not`**: Returns `True` if both variables point to different objects in memory.

#### Example:

```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # True, because a and b refer to the same object in memory
print(a is c)  # False, because a and c are two different objects in memory
```

#### Output:

```
True
False
```

---

### **Conclusion**

- **`if`**, **`elif`**, and **`else`** allow for branching logic.
- **Comparison operators** (`==`, `!=`, `>`, `<`, etc.) are used to compare values.
- **Logical operators** (`and`, `or`, `not`) help combine multiple conditions.
- **Membership** and **identity operators** provide additional ways to test for inclusion and object identity.
- Conditional expressions (ternary operator) provide a compact way to write conditional assignments.

Understanding how and when to use these conditional structures will enable you to control the flow of your program effectively.