tup = (1,2,3,4,5,6,7,8,9,0)

for i in tup:
    print(i)


# deletion from list
list1 = [1,2,3,4,5,6,7,8,9,0]

index = 5

for i in range(index, len(list1) - 1):
    list1[i] = list1[i+1]
else:
    list1.pop()
    print(list1)

# or just do
del list1[index]
print(list1)


for i in range(len(list1)):
    print(list1.pop())

print(list1)


for i in range(100, 0, -1): # starting, ending, step
    print(i)



temp = 0
n = 5
for i in range(n+1):
    temp += i
else:
    print("total sum",temp)