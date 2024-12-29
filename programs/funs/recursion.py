tup = (1,2,3,4,5,6,7,8,9,0)

def rec(x, i=0):
    if i < len(x):
        print(x[i])
        rec(x, i + 1)

rec(tup)


def fac(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fac(n - 1)


print(fac(5))

def fibonacci(n):
    if n == 1 or n == 2:
        print(1)
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(10)

