# Read the file and use splitlines()
with open("configuration.txt") as file:
    content = file.read()
    my_list = content.splitlines()
    print(my_list)

# Use readlines()
with open("configuration.txt") as file:
    my_list = file.readlines()
    print(my_list)

# Use readlines() with hint
with open("configuration.txt") as file:
    my_list = file.readlines(2)
    print(my_list)

# Use readlines() with hint
with open("configuration.txt") as file:
    my_list = file.readlines(30)
    print(my_list)

# Use readline()
with open("configuration.txt") as file:
    first = file.readline()
    second = file.readline(5)
    print(first)
    print(second)

# Loop the file
with open("configuration.txt") as file:
    for line in file:
        print(line)
