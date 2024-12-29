info = {
    "key": "value",
    "name": "dullat",
    "age": 3,
    "marks": [89,80,75,95],
    "isPass": True
}

print(info)

info["key"] = "value2"
print(info["key"])

null_dict = {}
null_dict["title"] = "i am learning python"
print(null_dict)

# nesting
null_dict["sub_data"] = {
    "topics": ["intro", "datatypes"],
    "learning_rate": "2 topics per day"
}

print(null_dict["sub_data"]["learning_rate"])

list1 = list(null_dict.keys())

print(list1)
print("\n\n")
print(null_dict.values(), "\n\n")
print(list(null_dict.values()),"\n")
print(info.items())

non = info.get("name") #will not give error, it will return Null
print(non)

info.update({"address": "ch"})
print("\n", info["address"])