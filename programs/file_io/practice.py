import os

f = open("./practice.txt","r")

data = f.read()
newData = data.replace("Java", "Python")

f.close()

w = open("./practice.txt", "w")

w.write(newData)

f.close()

print(newData)