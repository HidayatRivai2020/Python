class Member():

    def __init__(self, name, position):
        self.name = name
        self.position = position

x = Member("Jack", "Leader")
x2 = Member("Harry", "Support")
print(x.name)
print(x.position)
print(x2.name)
print(x2.position)