import csv

# Read CSV
with open("example.csv", 'r') as file:
    reader = csv.reader(file)
    print("Print by row")
    for row in reader:
        print(row)
    print("")

with open("example.csv", 'r') as file:
    reader = csv.reader(file)
    print("Print by column")
    for row in reader:
        print(row[0])
        print(row[1])
    print("")

with open("example.csv", 'r') as file:
    reader = csv.reader(file)
    next(reader)
    print("Skip Header")
    for row in reader:
        print(row)
    print("")


# Custom Delimiter:
with open("custom_delimiter.csv", 'r') as file:
    reader = csv.reader(file, delimiter='\t', lineterminator='\n')
    next(reader)
    print("Custom Delimiter")
    for row in reader:
        print(row)
    print("")
