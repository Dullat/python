def fun():
    num = ""
    list1 = []
    with open("./list.txt", "r") as file:
        data = file.read()
        for i in range(len(data)):
            if data[i] == ",":
                list1.append(int(num))
                num = ""
            else:
                num += data[i]
        list1.append(num)
        print(list1)

fun()