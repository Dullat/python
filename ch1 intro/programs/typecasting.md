``` python
# implicit / conversion
var1 = 2.5
var2 = 2
var3 = var1 + var2
print(var3)

# error
var4 = "2"
# print(var2+ var4) it will give error


# explicit / typecasting
print(var2 + int(var4))
intVar = 2
strVar = str(intVar)

# input typecasting
typ = input("name:") # it will take only str, use typecasting to take other datatypes
typ2 = int(input("age: "))
print(type(typ))
print(type(typ2))
```