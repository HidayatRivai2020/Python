# Write
with open("output/write.txt", 'w') as file:
    file.write('this is a new text')

# Write override
with open("output/override.txt", 'w') as file:
    file.write('this is a text')

with open("output/override.txt", 'w') as file:
    file.write('replace this text\n')
    file.write('this is a another text')

# Append
with open("output/append.txt", 'w') as file:
    file.write('this is a new text')

with open("output/append.txt", 'a') as file:
    file.write('\nappend another text\n')
    file.write('this is the last text')

# Read and write
with open("output/read_write.txt", 'w') as file:
    file.write('this is a new text,\nI need this to read and write')

with open("output/read_write.txt", 'r+') as file:
    file.write('updated')
    file.seek(15)
    file.write('updated too')