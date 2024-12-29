arr = [23, 45, 67, 89, 90, 67]

print(type(arr))
print(arr)

print(arr[3:])
arr[2] = 100
arr.sort()
arr.append(81)
print(arr)
arr.insert(2, 45)
arr.sort(reverse=True)
arr.remove(45)
print(arr)
arr.pop()
print(arr)

list  = ['a', 'b', 'd', 'c']
list.sort()
print(list)

# tuples are immutable

tup = (4, 6, 2, 9)
tup2 = (1,)
tup3 = (1)
print(type(tup2))
print(type(tup3))

print(tup.index(9))
print(tup.count(2))