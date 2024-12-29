class student:
    college_name = "GNC"

    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)

    @staticmethod
    def static_meh(value):
        print(student.college_name, f"is a {value} college")

s1 = student("some guy")
s1.print_name()
s1.static_meh("good")