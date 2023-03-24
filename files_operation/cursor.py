# Read with parameter
files = open('configuration.txt', 'r')
content = files.read(2)
print(content)

content = files.read(10)
print(content)

# get cursor
print(files.tell())

# set new cursor
pos = files.seek(5)
print(files.tell())
print(pos)

# Read after set new cursor
content = files.read(20)
print(content)

files.close()
