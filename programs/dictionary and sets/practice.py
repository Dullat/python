# given a list of subjects for students, we require 1 room for each subjet, find the no of rooms

list1 = ["python", "java", "c++", "python", "javascript", "java", "c++", "c"]
set1 = set(list1)
print(len(set1))

# get subjects and marks and enter in a dic

dic = {}

num = int(input("enter n of subjects:"))

for i in range(num):
    subject = input("enter subject: ")
    marks = int(input("enter marks: "))
    dic.update({subject : marks})

# store 9 and 9.0 as seperate values in set

nine = 9.0
set4 = set()

# set4.add(int(nine))
# set4.add(str(nine))

set4.add(("i", int(nine)))
set4.add(("f",float(nine)))

print(set4)