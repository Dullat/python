import random

def getRandom():
    rand_char = [1,2,3,4,5,6,7,8,9,0,"#","*","$","@","a","b","c","d","A","B","C","D"]
    return random.choice(rand_char)

def generatePass(len):
    password = ""
    for i in range(len+1):
        password += str(getRandom())
        
    return password

l = generatePass(12)

print(l)
