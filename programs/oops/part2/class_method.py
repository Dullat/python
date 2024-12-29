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