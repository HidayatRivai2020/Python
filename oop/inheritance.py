class Person():
    age = 20

    def __init__(self, name) -> None:
        self.name = name

    def hello(self):
        print("hello")

    def introduce(self):
        print("my name is {}".format(self.name))
    
class Member(Person):
    role = ""

    def __init__(self, name, alias) -> None:
        super().__init__(name)
        self.alias = "Hari"

    def check_role(self):
        print("my role is {}".format(self.role))
    
    def introduce(self):
        print("my name is {} alias {}, and my role is {}".format(self.name, self.alias, self.role))

x = Person("Jack")
x.hello()
x.introduce()
print(x.age)

x2 = Member("Harry", "Hari")
x2.hello()
x2.role = "Support"
x2.check_role()
x2.introduce()
print(x2.age)