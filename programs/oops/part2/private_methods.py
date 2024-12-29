class Person:
    def __private_print(self): # private fun
        print("im private fun")
    def call_private(self):
        self.__private_print()

p1 = Person()
p1.call_private()