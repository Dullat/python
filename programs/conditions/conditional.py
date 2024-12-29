var = False

var2 = "welcome back" if var == True else None

shouldPrint = True

#print(var2) if shouldPrint == True else " "

(print(var2), "")[shouldPrint == True]

# better approach

shouldPrint and print(var2)


# more

var3 = shouldPrint and 13

print(var3)