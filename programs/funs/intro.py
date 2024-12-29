# find factorial

def fac(n):
    temp = 1
    for i in range(2, n + 1):
        temp *= i
    print(temp)

fac(5)

# keyboard args

def greet(name, age):
    print(f"Hello, {name}. You are {age} years old.")

greet(age=30, name="Alice")  # Using keyword arguments


# usd to inr

def converter(usd_val):
    print(usd_val * 85)

converter(1)