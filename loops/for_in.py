# list loop
fruits = ["apple", "banana", "orange"]
for i in fruits:
    print(i)
    
print("----")

# Dictionaries loop
members = {"leader":"Jack", "fighter":"Night", "defender": "Harry", "support": "Stu"}
for i in members:
    print("index: " + i)
    print("member: " + members[i])

print("----")

# Tuples in list loop
mylist = [("a", "b"), ("a", "b"), (1, 2)]
for items1, items2 in mylist:
    print("items 1: {}".format(items1))
    print("items 2: {}".format(items2))