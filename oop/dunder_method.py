class Book():
    def __init__(self, title, author, pages) -> None:
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self) -> str:
        return "{} written by {}".format(self.title, self.author)
    
    def __len__(self):
        return self.pages

x = Book("Palawija City", "Jack", 1000)

print(x)
print(len(x))