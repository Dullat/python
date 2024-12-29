class Student:
    name = "none"                   # obj attr
    college = "guru nanak college"  # class attr

    def __init__(self, name, roll_no, class_code):
        self.name = name
        self.roll_no = roll_no
        self.class_code = class_code

s1 = Student("idk", 221, "MCA1")
print(s1.name)