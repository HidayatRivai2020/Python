print("=== List ===")

# Basic list operations
string_list = ["this", "is", "a", "new", "lsit"]
print(string_list)
print("index 3 of string list"+ string_list[3])

number_list = [1, 2, 3, 5, 3, 6]
print(number_list)
print("index 0:3 of number_list"+ str(number_list[0:3]))

# list comprehension
numbers = [i for i in range(1, 101)]
print(numbers)

even_numbers = [i for i in range(1, 101) if i % 2 == 0]
print(even_numbers)

# Nested list operations
cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
print(cells[0])
print(cells[1][0])
for x in cells:
    print('Element:', x)

for i in cells:
    for j in i:
        print('cell:', j)

# List inside tuple
tuple_with_list = (1, 2, [3, 4], 5) 
print(tuple_with_list)

