It looks like you're seeing a lot of redundant prints and calculations, which typically happens in a recursive approach to the Fibonacci sequence if you're not carefully managing your recursion. Based on the output you've posted, it seems like multiple recursive calls are causing repetitive prints.

### Issue:

The Fibonacci function you've written is printing the sequence multiple times because it's recursively calculating and printing intermediate values (which are redundant for every call). This is an issue commonly seen in recursive Fibonacci implementations without proper handling.

### Solution:

If you're trying to **print each Fibonacci number** as the recursive function calculates it, the recursive nature of the function will still cause multiple prints due to the repeated calculations. Instead, we can either:

1. Use **memoization** (to store intermediate results).
2. Use **iteration** (which is much more efficient and avoids redundant calculations).

But first, let me explain **why** your recursive approach is causing such output.

### Why Your Output is So Repetitive:

In the recursive Fibonacci function you provided, when you call `fibonacci(n - 1)` and `fibonacci(n - 2)`, both calls internally make their own recursive calls to calculate smaller Fibonacci numbers. These recursive calls for smaller Fibonacci values are repeated many times, which leads to the redundant printing of intermediate results.

### Efficient Solution: Memoization

One of the best ways to handle this in Python is to use **memoization**, which stores the result of each Fibonacci calculation as it’s computed, preventing redundant recalculations.

Here's how you can do it:

### Fibonacci with Memoization:

```python
def fibonacci(n, memo=None):
    if memo is None:
        memo = {}
    
    # Base cases
    if n == 1 or n == 2:
        return 1
    
    # Check if result already in memo
    if n in memo:
        return memo[n]
    
    # Recursive call and store result in memo
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

# To print the Fibonacci sequence up to n
n = 10
for i in range(1, n + 1):
    print(fibonacci(i))
```

### Explanation:

1. **Memoization**: We use a dictionary `memo` to store previously calculated Fibonacci numbers so that each number is only calculated once.
2. **Base Cases**: If `n` is 1 or 2, the function directly returns 1.
3. **Recursive Case**: If the Fibonacci number has already been calculated and stored in `memo`, it is returned directly, avoiding redundant calculations.

### Output for `fibonacci(10)`:

```python
1
1
2
3
5
8
13
21
34
55
```

### Why This is Better:

- **Efficiency**: By storing the result of each Fibonacci calculation (`memo`), the function avoids recalculating the same Fibonacci values multiple times.
- **Reduced Recursion Depth**: This approach reduces the recursion depth significantly, making it more efficient for larger `n`.

### Alternative Solution: Iterative Approach

If you don’t mind using an iterative approach, it’s even simpler and more efficient:

```python
def fibonacci_iterative(n):
    a, b = 0, 1
    for i in range(n):
        print(b, end=" ")
        a, b = b, a + b

fibonacci_iterative(10)
```

### Output:

```python
1 1 2 3 5 8 13 21 34 55
```

### Why the Iterative Approach is Ideal:

- **Efficiency**: The iterative approach avoids recursion and performs in O(n) time.
- **Simplicity**: It is simpler to understand and implement than recursion, especially for tasks like printing Fibonacci numbers in order.

---

### Summary:

- If you want to print the Fibonacci sequence, **memoization** improves the recursive approach by preventing redundant calculations.
- The **iterative approach** is simpler, avoids recursion depth problems, and is generally more efficient for this problem.

If you still prefer recursion, go ahead with memoization for efficiency. Let me know if you need further clarification!