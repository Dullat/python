### Python Loops - Notes

In Python, loops are used to execute a block of code repeatedly. There are two main types of loops: **`for` loops** and **`while` loops**.

---

### 1. **For Loop**

A `for` loop is used to iterate over a sequence (like a list, tuple, string, or range). It allows you to execute a block of code for each element in the sequence.

#### Syntax:

```python
for variable in sequence:
    # code to execute
```

- `variable` is a placeholder for each element in the sequence.
- `sequence` can be any iterable (like a list, string, range, etc.).

#### Example 1: Iterating through a tuple

```python
tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

for i in tup:
    print(i)
```

**Output:**

```
1
2
3
4
5
6
7
8
9
0
```

This loop will print each number from the tuple `tup`.

---

### 2. **For Loop with `range()` Function**

The `range()` function generates a sequence of numbers, which can be used with a `for` loop to repeat an action multiple times.

#### Syntax:

```python
for i in range(start, stop, step):
    # code to execute
```

- `start` is the number where the sequence starts (inclusive).
- `stop` is the number where the sequence ends (exclusive).
- `step` is the increment value (default is 1).

#### Example 2: Using `range()` with a `for` loop

```python
for i in range(100, 0, -1):
    print(i)
```

**Output:**

```
100
99
98
...
2
1
```

In this example, the loop starts from 100 and decrements by 1 each time, stopping before it reaches 0.

---

### 3. **While Loop**

A `while` loop repeatedly executes a block of code as long as the condition is `True`.

#### Syntax:

```python
while condition:
    # code to execute
```

- The condition is checked before each iteration. If it's `True`, the loop continues; if `False`, the loop stops.

---

### 4. **Looping with `else`**

In Python, `for` and `while` loops can have an `else` block. The `else` block is executed after the loop finishes normally (not terminated by a `break`).

#### Example 3: Using `else` with a `for` loop

```python
temp = 0
n = 5
for i in range(n + 1):
    temp += i
else:
    print("Total sum:", temp)
```

**Output:**

```
Total sum: 15
```

In this example, the loop adds up all the numbers from 0 to 5 and then prints the total sum after the loop finishes.

---

### 5. **Deleting Elements from a List in a Loop**

In Python, you can remove elements from a list by either modifying the list in-place or using methods like `pop()` and `del`.

#### Example 4: Deleting an element from a list using a `for` loop

```python
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
index = 5

for i in range(index, len(list1) - 1):
    list1[i] = list1[i + 1]
else:
    list1.pop()
    print(list1)
```

**Output:**

```
[1, 2, 3, 4, 6, 7, 8, 9, 0]
```

Here, the `for` loop shifts each element to the left to "delete" the element at index 5. The `pop()` method is then used to remove the last duplicated element.

#### Alternative method:

```python
del list1[index]
print(list1)
```

**Output:**

```
[1, 2, 3, 4, 6, 7, 8, 9, 0]
```

The `del` statement directly deletes the element at the specified index.

---

### 6. **Popping All Elements from a List**

You can use a `for` loop to pop all elements from a list one by one. Here's an example:

#### Example 5: Popping all elements from a list

```python
for i in range(len(list1)):
    print(list1.pop())

print(list1)
```

**Output:**

```
9
0
8
7
6
5
4
3
2
1
[]
```

Here, `pop()` removes and returns the last element of the list during each iteration. After all elements are popped, the list becomes empty.

---

### 7. **Summary of Python Loops**

- **`for` loop**: Used to iterate over a sequence or range of numbers.
- **`while` loop**: Used to repeat a block of code as long as a condition is `True`.
- **`else` with loops**: The `else` block is executed if the loop completes normally (not interrupted by `break`).
- **`range()` function**: Generates a sequence of numbers for iteration in `for` loops.
- **`pop()` and `del`**: Methods to remove elements from a list. `pop()` also returns the removed element, while `del` just removes it.

This concludes the basic concepts of loops in Python.