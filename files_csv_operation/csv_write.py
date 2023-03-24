import csv

# Write CSV
with open("output/write.csv", 'w') as file:
    writer = csv.writer(file)
    data = ('ID', 'Name', 'City')
    writer.writerow(data)
    data = ('1', 'Jack', 'Palawija')
    writer.writerow(data)


# Append CSV
with open("output/append.csv", 'a', newline='') as file:
    writer = csv.writer(file)
    data = ('no', '*2', '*3')
    writer.writerow(data)
    for x in range(1, 5):
        writer.writerow([x, x*2, x*3])

