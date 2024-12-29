# set is collection of unordered items , where each item is unique and immutable

set1 = {1,2,3,4,5, "apple", "apple"} #it will ignore 1 apple
print(set1) # unordered
print(type(set1))

# empty set / not valid set = {} <= its a dictionary
set2 = set()

set2.add(1)
set2.add(34)
set2.remove(1)
set2.add((2,4,8))
print(set2.pop()) # pops random value
set2.clear() # clears whole ser

print(set2)


data1 = {1,2,3,4,5,6}
data2 = {1,2,5,6,7}
print(data1.union(data2))
print(data1.intersection(data2))