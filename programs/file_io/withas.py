with open("practice.txt", "r") as file:
    content = file.read()
    print(content.count("Python"))
    print(content)
    file.close()

def find_in_line():
    data = True
    line = 1
    word = "language"
    with open("practice.txt", "r") as file:
        while data:
            data = file.readline()
            if word in data:
                print("found in line: ", line)
                
            line += 1

find_in_line()