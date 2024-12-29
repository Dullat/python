#### ez way ###

import string

def getRandPass():
    pass_range = 16
    password = ""
    charValues = string.ascii_letters + string.digits + string.punctuation
    for i in range(pass_range + 1):
        password += random.choice(charValues)

    return password

print(getRandPass())