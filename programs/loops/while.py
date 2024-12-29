# print square of numbers

var = 1

while var <= 10:
    print(var ** 2)
    var += 1


# searach for numbers in a tuple

tup = (7,9,4,23,6,8)

i = 0

while i < len(tup):
    print(i + 1, "finding..")
    if tup[i] == 23:
        print("found at:",i+1)
        break
    i += 1

# print even nums

j = 0

while j < 100:
    j += 1
    if j % 2 != 0:
        continue
    print(j)
    