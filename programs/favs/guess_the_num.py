import random

randNum = random.randint(1,10)


def guessTheNum(x):
    userNum = int(input("enter 1 to 10:"))

    if randNum == userNum:
        return True


    if randNum > userNum:
        print("smaller, try again")
        return guessTheNum(x)
    if randNum < userNum:
        print("bigger, try again")
        return guessTheNum(x)

# print(guessTheNum(randNum))


# ezz way
def useWhile(x):

    while True:
        userNum = int(input("enter from 1 to 10:"))
        if userNum < x:
            print("smaller , choose bigger")
        if userNum > x:
            print("bigger , choose smaller")

        if userNum == x:
            print("good guess...")
            break

useWhile(randNum)


