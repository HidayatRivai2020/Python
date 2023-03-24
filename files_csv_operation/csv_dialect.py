import csv

print(csv.list_dialects())

csv.register_dialect('semicolon', delimiter=';', quoting=csv.QUOTE_NONE, lineterminator='\n')

with open("output/dialect.csv", 'w') as file:
    writer = csv.writer(file, dialect='semicolon')
    data = ('ID', 'Name', 'City')
    writer.writerow(data)
    data = ('1', 'Jack', 'Palawija')
    data2 = ('2', 'Stu', 'Agraris')
    data3 = ('3', 'Harry', 'BluePark')
    writer.writerow(data)
    writer.writerow(data2)
    writer.writerow(data3)


with open("output/dialect.csv", 'r') as file:
    reader = csv.reader(file, dialect='semicolon')
    print("Print by row")
    for row in reader:
        print(row)
    print("")