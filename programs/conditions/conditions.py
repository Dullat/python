age = 12

if age > 18:
    print(f"age is {age} cant apply")
elif age > 50:
    print(f"age is {age}, need eyesight test")
else:
    print(f"{age} really?, you better be driving in video games")


a,b,c = 7,22,22

if a >= b:
    if a >= c:
        print("a")
    else:
        print("c")
elif b >= c:
    print("b")
else:
    print("c")


if a >= b and a >= c:
    print("a")
elif b >= c:
    print("b")
else:
    print("c")