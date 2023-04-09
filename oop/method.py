class Rectangle():

    def __init__(self, width, length) -> None:
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length
    
    def show_message(self, msg, value):
        print("{} {}".format(msg, value))

rect = Rectangle(4, 5)
print(rect.area())
rect.show_message("the result of rectangle area is ", rect.area())