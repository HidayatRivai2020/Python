# with keyword to open file
with open("configuration.txt", 'r') as file:
    print(file.read())

# closed is true because it automatic
print(file.closed)
