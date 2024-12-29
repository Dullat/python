class Student:
    num = None

    # def __init__(self): #default constructor
    #     print("default constructor \nso init num with value: 10")
    #     self.num = 10   
    # this is not c++, here prev con is overridden

    def __init__(self, x, y): # parametrized
        self.num = x + y
    
    # def __init__(self, obj):  # copy con
    #     self.num = obj.num

    def print_name(self):
        print(self.num)


s1 = Student(23,56)
#s2 = Student(s1)

s1.print_name()
#s2.print_name()