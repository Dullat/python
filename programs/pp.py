class Person:
    name = "uknown"
    def __init__(self, name):
        self.name = name

    def change_class_attr(self, name):
        Person.name = name

p1 = Person("duck")

print(p1.name, Person.name)

p2 = Person("quack")
print(p2.name, Person.name)
p2.change_class_attr("changed")

print(p2.name, Person.name)

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

class Car:
    def __init__(self, type):
        self.type = type
    @staticmethod
    def start(self):
        print("starting...")
    @staticmethod
    def stop(self):
        print("stopping...")

class Toyota(Car):
    def __init__(self, name, type):
        self.name = name
        super().__init__(type)
        super().start()

c1 = Toyota("fortuner", "petrol")
print(c1.type)


print(1 + 2)
print("hah " + "huhu")
print([1,2,3]+[4,5,6])   # its overloading , here classes has done poly already


# operator overloading / polymorphism
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    def __add__(self, num2):   # dunder functions
        real = self.real + num2.real
        img = self.img + num2.img
        return Complex(real, img)

n1 = Complex(23, 56)
n2 = Complex(23, 56)
n3 = n1 + n2
print(n3.real)


class Circle:
    def __init__(self, r):
        self.r = r

    def Area(self):
        return 3.142 * (self.r * self.r)
    
c1 = Circle(21)
print(c1.Area())

class Order:
    def __init__(self, price):
        self.price = price
    
    def __gt__(self, obj):
        return self.price > obj.price

o1 = Order(237)
o2 = Order(45)

print(o1 > o2)

class Person:
    def __private_print(self): # private fun
        print("im private fun")
    def call_private(self):
        self.__private_print()

p1 = Person()
p1.call_private()

class Marks:
    def __init__(self, math, phy, chem):
        self.math = math
        self.phy = phy
        self.chem = chem

    @property
    def percentage(self):
        return str((self.math + self.phy + self.chem) / 3) + "%"

m1 = Marks(34, 57, 89)
print(m1.percentage)
m1.math = 50
print(m1.percentage)