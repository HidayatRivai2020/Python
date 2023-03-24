# Open file
files = open('configuration.txt', 'r')

# Read file
content = files.read()
print(content)

# Close file
print(files.closed)
files.close()
print(files.closed)
