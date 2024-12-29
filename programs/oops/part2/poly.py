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