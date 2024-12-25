### **Python Dictionaries: Key Notes**

Dictionaries are one of the most important data structures in Python. They store data in **key-value pairs** and are mutable, meaning you can modify them after creation.

---

### **1. Basics of Dictionaries**

- A **dictionary** in Python is created using curly braces `{}` with **key-value** pairs separated by a colon `:`.
- **Keys** must be immutable (like strings, numbers, or tuples), and each key must be unique.
- **Values** can be of any data type: numbers, lists, strings, other dictionaries, etc.

**Example:**

```python
info = {
    "key": "value",
    "name": "dullat",
    "age": 3,
    "marks": [89, 80, 75, 95],
    "isPass": True
}
```

In this example:

- `"key"`, `"name"`, `"age"`, `"marks"`, and `"isPass"` are keys.
- `"value"`, `"dullat"`, `3`, `[89, 80, 75, 95]`, and `True` are corresponding values.

---

### **2. Commonly Used Dictionary Methods**

#### **Accessing Values:**

- **Access a value by key:**
    
    ```python
    print(info["name"])  # Output: dullat
    ```
    
- **Using `.get()` to access a value:**
    
    - The `.get()` method will return `None` if the key does not exist (instead of raising an error).
    
    ```python
    print(info.get("age"))  # Output: 3
    print(info.get("address"))  # Output: None
    ```
    

#### **Adding or Modifying Entries:**

- **Add or update a key-value pair:**
    
    ```python
    info["key"] = "value2"
    print(info["key"])  # Output: value2
    ```
    
- **Using `.update()` to add multiple key-value pairs:**
    
    - `.update()` can add multiple items or update existing ones.
    
    ```python
    info.update({"address": "ch"})
    print(info["address"])  # Output: ch
    ```
    

#### **Removing Elements:**

- **Using `.pop()` to remove a specific key and return its value:**
    
    ```python
    removed_value = info.pop("age")
    print(removed_value)  # Output: 3
    print(info)  # The 'age' key is removed from the dictionary.
    ```
    
- **Using `.popitem()` to remove and return the last key-value pair:**
    
    ```python
    last_item = info.popitem()
    print(last_item)  # Output: ('isPass', True)
    ```
    
- **Using `del` to remove a key-value pair:**
    
    ```python
    del info["marks"]
    print(info)  # The 'marks' key is removed.
    ```
    

#### **Keys, Values, and Items:**

- **Get all keys:**
    
    ```python
    keys = info.keys()
    print(keys)  # Output: dict_keys(['key', 'name', 'marks', 'isPass'])
    ```
    
- **Get all values:**
    
    ```python
    values = info.values()
    print(values)  # Output: dict_values(['value2', 'dullat', [89, 80, 75, 95], True])
    ```
    
- **Get all key-value pairs (items):**
    
    ```python
    items = info.items()
    print(items)  # Output: dict_items([('key', 'value2'), ('name', 'dullat'), ('marks', [89, 80, 75, 95]), ('isPass', True)])
    ```
    

---

### **3. Nested Dictionaries**

- You can **nest dictionaries** within other dictionaries. For example, you can store lists or other dictionaries as values.

**Example:**

```python
null_dict = {}
null_dict["title"] = "I am learning Python"
null_dict["sub_data"] = {
    "topics": ["intro", "datatypes"],
    "learning_rate": "2 topics per day"
}
```

- In this example, `null_dict["sub_data"]` is another dictionary with its own keys (`"topics"`, `"learning_rate"`).

To access the nested dictionary:

```python
print(null_dict["sub_data"]["learning_rate"])  # Output: 2 topics per day
```

---

### **4. Conversion Between Lists and Dictionaries**

- **Convert dictionary keys to a list:**
    
    ```python
    list_keys = list(null_dict.keys())
    print(list_keys)  # Output: ['title', 'sub_data']
    ```
    
- **Convert dictionary values to a list:**
    
    ```python
    list_values = list(null_dict.values())
    print(list_values)  # Output: ['I am learning Python', {'topics': ['intro', 'datatypes'], 'learning_rate': '2 topics per day'}]
    ```
    
- **Convert dictionary items (key-value pairs) to a list:**
    
    ```python
    list_items = list(info.items())
    print(list_items)  # Output: [('key', 'value2'), ('name', 'dullat'), ('marks', [89, 80, 75, 95]), ('isPass', True)]
    ```
    

---

### **5. Dictionary Methods Recap**

Here’s a summary of the most commonly used dictionary methods:

- **`.keys()`** – Returns a view object of all the dictionary’s keys.
- **`.values()`** – Returns a view object of all the dictionary’s values.
- **`.items()`** – Returns a view object of all the dictionary’s key-value pairs as tuples.
- **`.get(key)`** – Returns the value associated with `key`, or `None` if the key is not found.
- **`.update(dict)`** – Adds key-value pairs from `dict` to the dictionary.
- **`.pop(key)`** – Removes the key-value pair with the specified key and returns the value.
- **`.popitem()`** – Removes and returns the last inserted key-value pair.
- **`.clear()`** – Removes all items from the dictionary.
- **`.setdefault(key, default)`** – Returns the value of the key if it exists, otherwise sets the key to the default value.

---

### **6. Example Program Using Dictionaries**

```python
info = {
    "key": "value",
    "name": "dullat",
    "age": 3,
    "marks": [89, 80, 75, 95],
    "isPass": True
}

# Printing the whole dictionary
print(info)

# Modifying a value for an existing key
info["key"] = "value2"
print(info["key"])

# Creating an empty dictionary and adding elements
null_dict = {}
null_dict["title"] = "I am learning Python"
print(null_dict)

# Nested dictionary
null_dict["sub_data"] = {
    "topics": ["intro", "datatypes"],
    "learning_rate": "2 topics per day"
}

# Accessing nested dictionary values
print(null_dict["sub_data"]["learning_rate"])

# Convert dictionary keys to list
list1 = list(null_dict.keys())
print(list1)

# Convert dictionary values to list
print(null_dict.values(), "\n\n")
print(list(null_dict.values()), "\n")

# Printing key-value pairs of the dictionary
print(info.items())

# Using .get() to avoid errors
non = info.get("name")  # Will not give an error if key does not exist
print(non)

# Using update() to add new key-value pairs
info.update({"address": "ch"})
print("\n", info["address"])  # Output: ch
```

---

### **Conclusion:**

Today, you have learned about **dictionaries** in Python, including:

- How to create, access, modify, and delete key-value pairs.
- Using useful methods like `.keys()`, `.values()`, `.items()`, `.get()`, `.update()`, and `.pop()`.
- Nesting dictionaries and converting between dictionaries and lists.

Dictionaries are a versatile and efficient way to store and manipulate data in Python. Keep practicing using dictionaries, and experiment with methods to further enhance your understanding.