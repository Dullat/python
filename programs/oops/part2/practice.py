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