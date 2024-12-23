### **Python Strings: Notes and Operations**

In Python, **strings** are sequences of characters, and they are one of the most commonly used data types. Strings can be enclosed in single quotes (`'`) or double quotes (`"`), and they are immutable, meaning their content cannot be changed after creation.  [[intro program]]

### **1. String Declaration**

You can declare strings using single quotes, double quotes, or triple quotes (for multi-line strings).

- **Single Quotes**:
    
    ```python
    my_string = 'Hello'
    ```
    
- **Double Quotes**:
    
    ```python
    my_string = "Hello"
    ```
    
- **Triple Quotes** (for multi-line strings):
    
    ```python
    my_string = '''Hello,
    this is a multi-line string.'''
    ```
    

### **2. String Concatenation**

You can combine strings using the **`+`** operator.

- **Example**:
    
    ```python
    greeting = "Hello"
    name = "Alice"
    message = greeting + " " + name  # Concatenates strings with a space in between
    print(message)  # Output: Hello Alice
    ```
    

### **3. String Repetition**

You can repeat a string using the **`*`** operator.

- **Example**:
    
    ```python
    word = "Hi"
    repeated_word = word * 3  # Repeats "Hi" three times
    print(repeated_word)  # Output: HiHiHi
    ```
    

### **4. Accessing Characters (Indexing)**

Strings in Python are indexed starting from `0`. You can access individual characters of a string using square brackets `[]` with the index.

- **Example**:
    
    ```python
    my_string = "Python"
    print(my_string[0])  # Output: P (first character)
    print(my_string[3])  # Output: h (fourth character)
    ```
    

You can also use **negative indexing** to access characters from the end of the string.

- **Example**:
    
    ```python
    print(my_string[-1])  # Output: n (last character)
    print(my_string[-2])  # Output: o (second-to-last character)
    ```
    

### **5. Slicing Strings**

You can extract a substring (slice) from a string by specifying a range of indices. The syntax is `string[start:end]`, where `start` is the starting index (inclusive) and `end` is the ending index (exclusive).

- **Example**:
    
    ```python
    my_string = "Python"
    print(my_string[0:3])  # Output: Pyt (from index 0 to 2)
    print(my_string[2:])   # Output: thon (from index 2 to the end)
    print(my_string[:4])   # Output: Pyth (from the start to index 3)
    print(my_string[-3:])  # Output: hon (last 3 characters)
    ```
    

### **6. String Length**

To find the length of a string, use the built-in function `len()`.

- **Example**:
    
    ```python
    my_string = "Python"
    print(len(my_string))  # Output: 6 (length of the string)
    ```
    

### **7. String Methods**

Python provides a variety of **string methods** to perform operations on strings.

- **`lower()`**: Converts all characters to lowercase.
    
    ```python
    my_string = "HELLO"
    print(my_string.lower())  # Output: hello
    ```
    
- **`upper()`**: Converts all characters to uppercase.
    
    ```python
    my_string = "hello"
    print(my_string.upper())  # Output: HELLO
    ```
    
- **`capitalize()`**: Capitalizes the first character of the string.
    
    ```python
    my_string = "hello"
    print(my_string.capitalize())  # Output: Hello
    ```
    
- **`title()`**: Capitalizes the first character of each word.
    
    ```python
    my_string = "hello world"
    print(my_string.title())  # Output: Hello World
    ```
    
- **`strip()`**: Removes leading and trailing whitespace.
    
    ```python
    my_string = "  Hello World  "
    print(my_string.strip())  # Output: Hello World
    ```
    
- **`replace(old, new)`**: Replaces all occurrences of the substring `old` with `new`.
    
    ```python
    my_string = "Hello World"
    print(my_string.replace("World", "Python"))  # Output: Hello Python
    ```
    
- **`split(delimiter)`**: Splits the string into a list based on a delimiter (space by default).
    
    ```python
    my_string = "Hello World"
    print(my_string.split())  # Output: ['Hello', 'World']
    ```
    
- **`join(iterable)`**: Joins elements of an iterable (list, tuple) into a string, using the string as a separator.
    
    ```python
    my_list = ['Hello', 'World']
    print(" ".join(my_list))  # Output: Hello World
    ```
    
- **`find(substring)`**: Returns the index of the first occurrence of the substring (returns `-1` if not found).
    
    ```python
    my_string = "Hello World"
    print(my_string.find("World"))  # Output: 6
    ```
    
- **`count(substring)`**: Counts how many times the substring appears in the string.
    
    ```python
    my_string = "Hello World"
    print(my_string.count("o"))  # Output: 2
    ```
    
- **`startswith(prefix)`**: Checks if the string starts with the given prefix.
    
    ```python
    my_string = "Hello World"
    print(my_string.startswith("Hello"))  # Output: True
    ```
    
- **`endswith(suffix)`**: Checks if the string ends with the given suffix.
    
    ```python
    my_string = "Hello World"
    print(my_string.endswith("World"))  # Output: True
    ```
    

### **8. String Formatting**

String formatting allows you to insert variables into a string.

#### **Using `f-strings` (Python 3.6 and above)**:

```python
name = "Alice"
age = 25
message = f"My name is {name} and I am {age} years old."
print(message)  # Output: My name is Alice and I am 25 years old.
```

#### **Using `format()` method**:

```python
name = "Alice"
age = 25
message = "My name is {} and I am {} years old.".format(name, age)
print(message)  # Output: My name is Alice and I am 25 years old.
```

#### **Using `%` operator** (older style):

```python
name = "Alice"
age = 25
message = "My name is %s and I am %d years old." % (name, age)
print(message)  # Output: My name is Alice and I am 25 years old.
```

### **9. Escape Characters**

You can use escape sequences to include special characters in strings:

- `\n` – Newline
- `\t` – Tab
- `\\` – Backslash
- `\'` – Single quote
- `\"` – Double quote

#### Example:

```python
my_string = "Hello\nWorld\t!"
print(my_string)
```

#### Output:

```
Hello
World	!
```

### **10. String Immutability**

Strings in Python are **immutable**, meaning you cannot modify a string in place once it's created. However, you can create a new string by modifying or concatenating existing ones.

#### Example:

```python
my_string = "Hello"
# Attempting to modify a string will raise an error
# my_string[0] = "h"  # Error: 'str' object does not support item assignment

# You can create a new string though
my_string = "h" + my_string[1:]
print(my_string)  # Output: hello
```

### **11. String Encoding and Decoding**

Python strings are sequences of Unicode characters. You can convert a string to bytes using the `encode()` method, and you can convert bytes back to a string using the `decode()` method.

#### Example:

```python
my_string = "Hello"
encoded_string = my_string.encode('utf-8')  # Convert to bytes
print(encoded_string)  # Output: b'Hello'

decoded_string = encoded_string.decode('utf-8')  # Convert back to string
print(decoded_string)  # Output: Hello
```

---

### **Conclusion**

Strings are one of the most versatile and commonly used data types in Python. Understanding string operations such as concatenation, slicing, and using string methods is fundamental for manipulating text in Python. Additionally, string formatting allows for dynamic creation of messages, and methods like `replace()`, `split()`, and `find()` make it easy to search and modify strings.