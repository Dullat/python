f = open("./message.txt", "r")

line1 = f.readline()
print(line1)

line2 = f.readlrne()
print(line2)

f.close()

t = open("./message.txt", "w")

t.write("hello world \ni am learning python")
t.close()

# os module
import os

print(os.listdir())