list = [3, 2, 1, 2, 3]

mid = int(len(list) / 2)

copiedList = list[mid:]
list = list[:mid + 1]

copiedList.reverse()

print(copiedList)
print(list)

if(list == copiedList):
    print("yes")



# ez way
l1 = [3,2,1,2,3]
l2 = l1.copy()
l2.reverse()

l1 == l2 and print("yes it is")

# count students with grande A
grade = ["c", "d", "a", "a", "b"]
print(grade.count("a"))
grade.sort()
print(grade)