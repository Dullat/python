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