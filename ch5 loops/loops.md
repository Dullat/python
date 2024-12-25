### Python Loops Notes (Simplified)

1. **What is a Loop?**
    
    - A loop allows you to execute a block of code repeatedly.
    - Common types: `while` loop, `for` loop.
2. **`while` Loop**
    
    - The loop runs as long as the condition is `True`.
    - Syntax:
        
        ```python
        while condition:
            # block of code
        ```
        
3. **`for` Loop** (Not covered in your example but worth knowing)
    
    - Iterates over a sequence (like a list or range).
    - Syntax:
        
        ```python
        for item in iterable:
            # block of code
        ```
        
4. **Breaking Out of Loops**
    
    - `break`: Exits the loop immediately, regardless of the condition.
    - `continue`: Skips the rest of the current iteration and moves to the next.
5. **Using `else` with Loops**
    
    - The `else` block is executed if the loop runs to completion (i.e., without hitting `break`).
        
        ```python
        while condition:
            # code
        else:
            # executed if loop ends normally
        ```
        

---

### Your Program Code with Explanations

#### 1. **Print the Square of Numbers from 1 to 10**

```python
var = 1

while var <= 10:
    print(var ** 2)   # Prints square of var
    var += 1          # Increments var by 1
```

- This `while` loop starts at `var = 1` and prints the square of each number until `var` exceeds 10.
- The `var += 1` increments `var` by 1 in each iteration.

#### 2. **Search for a Number in a Tuple**

```python
tup = (7, 9, 4, 23, 6, 8)

i = 0

while i < len(tup):
    print(i + 1, "finding..")
    if tup[i] == 23:
        print("found at:", i + 1)
        break
    i += 1
```

- The `while` loop iterates through each index of the tuple.
- If the number `23` is found, it prints its position and exits the loop using `break`.
- The `i += 1` moves the loop to the next index.

#### 3. **Print Even Numbers from 1 to 100**

```python
j = 0

while j < 100:
    j += 1
    if j % 2 != 0:  # Check if the number is odd
        continue      # Skip the rest of the loop for odd numbers
    print(j)           # Print even numbers
```

- The loop increments `j` from 1 to 100.
- The `if j % 2 != 0` checks if `j` is odd; if true, `continue` skips the rest of the loop, printing only even numbers.

---

### Key Takeaways:

- **`while` loops** are controlled by a condition.
- Use **`break`** to exit a loop early.
- Use **`continue`** to skip to the next iteration.
- Use **`i += 1`** or similar to move to the next iteration in your loop.