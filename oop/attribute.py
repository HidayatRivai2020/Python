class Member():
    name = "Default Name"

    def __init__(self):
        pass

x = Member()
print(x.name)
x.name = "New Name"
print(x.name)
