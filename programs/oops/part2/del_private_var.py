class Account:
    def __init__(self, user, password):
        self.user = user
        self.__password = password # private __var
        
    def print_pass(self):
        print(self.__password)

acc1 = Account("deck", "1234567890")
print(acc1.user)
# print(acc1.password) this will genrate error
acc1.print_pass()
del acc1