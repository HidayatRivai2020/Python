print("=== For In ===")

# Looping through list
fruits = ["apple", "banana", "orange"]
for i in fruits:
    print(i)
    
print("----")

# Looping through dictionary
members = {"leader":"Jack", "fighter":"Night", "defender": "Harry", "support": "Stu"}
for i in members:
    print("index: " + i)
    print("member: " + members[i])

print("----")

# Looping through tuples in list
mylist = [("a", "b"), ("c", "d"), (1, 2)]
for items1, items2 in mylist:
    print("items 1: {}".format(items1))
    print("items 2: {}".format(items2))