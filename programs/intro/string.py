str1 = 'this is python'
str2 = "this is guru's python"
str3 = """this is idk what is this"""

strLineBreak = " this is a break here \nup there. see in terminal not here"

print(strLineBreak)

# concat
strLineBreak = "haha" + " " +  str2

print(strLineBreak)
print(len(strLineBreak))
print(strLineBreak[2])


# slicing
print(str1[0:8]) # str[:8]
print(str1[5:])

#negative slicing
print(str1[-5:-1])

#upper does not change original it just return
print(str1.upper())
print(str1.capitalize())
str1 = str1.upper()
print(str1.replace("O", "a"))
print(str1.find("O"))