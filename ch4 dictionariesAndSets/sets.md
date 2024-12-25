### **Python Sets: Key Notes**

Sets in Python are a **collection of unordered, unique elements**. They are particularly useful when you need to store a collection of items without duplicates and you don't care about the order of those items.

---

### **1. Basics of Sets**

- A **set** is defined using curly braces `{}` or the `set()` constructor.
- A set cannot have duplicate elements. If you try to add a duplicate element, it will be ignored.
- **Sets are unordered**: the items are not stored in a specific order and cannot be accessed using an index.

**Example:**

```python
set1 = {1, 2, 3, 4, 5, "apple", "apple"}
print(set1)  # Output: {1, 2, 3, 4, 5, 'apple'} - 'apple' is stored only once
print(type(set1))  # Output: <class 'set'>
```

---

### **2. Creating an Empty Set**

- An **empty set** cannot be created using curly braces `{}` because `{}` is interpreted as an empty dictionary.
- Use the `set()` constructor to create an empty set.

**Example:**

```python
set2 = set()  # Creates an empty set
```

---

### **3. Set Operations**

#### **Adding and Removing Elements:**

- **`.add()`**: Adds an element to the set.
    
    ```python
    set2.add(1)  # Adds 1 to the set
    set2.add(34)  # Adds 34 to the set
    ```
    
- **`.remove()`**: Removes an element from the set. If the element does not exist, it raises a `KeyError`.
    
    ```python
    set2.remove(1)  # Removes 1 from the set
    ```
    

#### **Popping a Random Element:**

- **`.pop()`**: Removes and returns a random element from the set. Since sets are unordered, you can't control which item will be removed.
    
    ```python
    print(set2.pop())  # Output will be a random element from the set
    ```
    

#### **Clearing the Set:**

- **`.clear()`**: Removes all elements from the set.
    
    ```python
    set2.clear()  # Clears the set, making it an empty set
    ```
    

---

### **4. Set Operations for Combining and Comparing Sets**

- **Union** (`.union()`): Returns a set that contains all unique elements from both sets.
    
    ```python
    data1 = {1, 2, 3, 4, 5, 6}
    data2 = {1, 2, 5, 6, 7}
    print(data1.union(data2))  # Output: {1, 2, 3, 4, 5, 6, 7}
    ```
    
- **Intersection** (`.intersection()`): Returns a set that contains elements that are present in both sets.
    
    ```python
    print(data1.intersection(data2))  # Output: {1, 2, 5, 6}
    ```
    
- **Difference** (`.difference()`): Returns a set that contains elements present in the first set but not in the second.
    
    ```python
    print(data1.difference(data2))  # Output: {3, 4}
    ```
    
- **Symmetric Difference** (`.symmetric_difference()`): Returns a set that contains elements that are in either of the sets, but not in both.
    
    ```python
    print(data1.symmetric_difference(data2))  # Output: {3, 4, 7}
    ```
    

---

### **5. Set Methods Recap**

Here is a summary of commonly used set methods:

- **`.add(element)`**: Adds an element to the set.
- **`.remove(element)`**: Removes the specified element from the set. If the element does not exist, it raises an error.
- **`.discard(element)`**: Removes the specified element, but does not raise an error if the element does not exist.
- **`.pop()`**: Removes and returns a random element from the set.
- **`.clear()`**: Removes all elements from the set, leaving it empty.
- **`.union(other_set)`**: Returns a new set containing all elements from both sets.
- **`.intersection(other_set)`**: Returns a new set with only the elements that are common in both sets.
- **`.difference(other_set)`**: Returns a new set with elements only in the first set, but not in the second.
- **`.symmetric_difference(other_set)`**: Returns a new set with elements in either of the sets, but not in both.

---

### **6. Example Program Using Sets**

```python
# Creating a set with unique elements
set1 = {1, 2, 3, 4, 5, "apple", "apple"}
print(set1)  # Output: {1, 2, 3, 4, 5, 'apple'}
print(type(set1))  # Output: <class 'set'>

# Creating an empty set
set2 = set()

# Adding and removing elements
set2.add(1)
set2.add(34)
set2.remove(1)  # Removes 1 from the set
set2.add((2, 4, 8))  # Adding a tuple to the set
print(set2)  # Output: {34, (2, 4, 8)}

# Popping a random value from the set
print(set2.pop())  # Output will be a random element removed

# Clearing the set
set2.clear()
print(set2)  # Output: set()

# Set operations
data1 = {1, 2, 3, 4, 5, 6}
data2 = {1, 2, 5, 6, 7}

# Union of two sets
print(data1.union(data2))  # Output: {1, 2, 3, 4, 5, 6, 7}

# Intersection of two sets
print(data1.intersection(data2))  # Output: {1, 2, 5, 6}
```

---

### **Conclusion:**

Today, you learned about **sets** in Python, including:

- How to create, add, remove, and pop elements in a set.
- The unordered nature of sets and how they ignore duplicates.
- Common set operations like **union**, **intersection**, **difference**, and **symmetric difference**.
- Useful methods like `.add()`, `.remove()`, `.pop()`, `.clear()`, `.union()`, `.intersection()`, and `.symmetric_difference()`.

Sets are useful when you need to store unique elements and perform efficient operations like checking for common or distinct elements. Keep practicing these set operations, and experiment with different use cases to deepen your understanding!