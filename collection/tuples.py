print("=== Tuples ===")

# Basic tuple operations
my_tuple = (1, 2, 3)
print(my_tuple)
print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[2])

# Nested structures with tuples
# Tuples inside a tuple
nested_tuple = (1, 2, (3, 4), 5)
print(nested_tuple)  

# Tuples inside a list
tuple_in_list = [1, 2, (3, 4), 5]
print(tuple_in_list)

# List inside a tuple
list_in_tuple = (1, 2, [3, 4], 5)  
print(list_in_tuple)

# tuple without parentheses
tuple_no_parentheses = 1, 2, 3, 4
print(tuple_no_parentheses)
