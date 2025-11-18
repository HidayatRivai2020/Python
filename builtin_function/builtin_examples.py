print("=== Python Built-in Functions Examples ===\n")

# 1. INPUT/OUTPUT FUNCTIONS
print("1. INPUT/OUTPUT FUNCTIONS")
print("-" * 40)

# print() - Output function
print("Hello, World!")
print("Multiple", "values", "separated", "by", "space")
print("Custom separator:", 1, 2, 3, sep=" - ")
print("Custom ending", end=" --> ")
print("continues here")

# input() - would be used for user input (commented to avoid blocking)
# name = input("Enter your name: ")
# print(f"Hello, {name}!")

print("\n" + "=" * 50 + "\n")

# 2. MATHEMATICAL FUNCTIONS
print("2. MATHEMATICAL FUNCTIONS")
print("-" * 40)

numbers = [-5, 3.7, 2, 8, 1]
print(f"Numbers: {numbers}")

# abs() - Absolute value
print(f"abs(-5) = {abs(-5)}")
print(f"abs(3.7) = {abs(3.7)}")

# max() and min()
print(f"max({numbers}) = {max(numbers)}")
print(f"min({numbers}) = {min(numbers)}")

# round()
pi = 3.14159
print(f"round(3.14159) = {round(pi)}")
print(f"round(3.14159, 2) = {round(pi, 2)}")

# sum()
print(f"sum({numbers}) = {sum(numbers)}")

# pow()
print(f"pow(2, 3) = {pow(2, 3)}")
print(f"pow(2, 3, 5) = {pow(2, 3, 5)}")  # (2^3) % 5

print("\n" + "=" * 50 + "\n")

# 3. TYPE CONVERSION FUNCTIONS
print("3. TYPE CONVERSION FUNCTIONS")
print("-" * 40)

# int()
print(f'int("42") = {int("42")}')
print(f"int(3.8) = {int(3.8)}")
print(f'int("1010", 2) = {int("1010", 2)}')  # Binary to decimal

# float()
print(f'float("3.14") = {float("3.14")}')
print(f"float(42) = {float(42)}")

# str()
print(f"str(42) = '{str(42)}'")
print(f"str([1, 2, 3]) = '{str([1, 2, 3])}'")

# bool()
print(f"bool(1) = {bool(1)}")
print(f"bool(0) = {bool(0)}")
print(f'bool("hello") = {bool("hello")}')
print(f'bool("") = {bool("")}')

# list(), tuple(), set()
text = "hello"
print(f'list("{text}") = {list(text)}')
print(f'tuple("{text}") = {tuple(text)}')
print(f'set("{text}") = {set(text)}')

print("\n" + "=" * 50 + "\n")

# 4. SEQUENCE AND COLLECTION FUNCTIONS
print("4. SEQUENCE AND COLLECTION FUNCTIONS")
print("-" * 40)

data = [1, 2, 3, 4, 5]
text_data = "Python"

# len()
print(f"len({data}) = {len(data)}")
print(f'len("{text_data}") = {len(text_data)}')

# range()
print(f"list(range(5)) = {list(range(5))}")
print(f"list(range(2, 8)) = {list(range(2, 8))}")
print(f"list(range(0, 10, 2)) = {list(range(0, 10, 2))}")

# enumerate()
fruits = ["apple", "banana", "cherry"]
print(f"enumerate({fruits}):")
for index, fruit in enumerate(fruits):
    print(f"  {index}: {fruit}")

# zip()
colors = ["red", "green", "blue"]
sizes = ["small", "medium", "large"]
print(f"zip({colors}, {sizes}):")
for color, size in zip(colors, sizes):
    print(f"  {color} {size}")

# sorted()
unsorted_numbers = [3, 1, 4, 1, 5, 9, 2]
print(f"sorted({unsorted_numbers}) = {sorted(unsorted_numbers)}")
print(f"sorted({unsorted_numbers}, reverse=True) = {sorted(unsorted_numbers, reverse=True)}")

# reversed()
print(f"list(reversed({data})) = {list(reversed(data))}")

print("\n" + "=" * 50 + "\n")

# 5. OBJECT INSPECTION FUNCTIONS
print("5. OBJECT INSPECTION FUNCTIONS")
print("-" * 40)

sample_data = [1, 2, 3]

# type()
print(f"type(42) = {type(42)}")
print(f"type(3.14) = {type(3.14)}")
print(f"type('hello') = {type('hello')}")
print(f"type({sample_data}) = {type(sample_data)}")

# id()
print(f"id({sample_data}) = {id(sample_data)}")

# dir() - show first few attributes
print(f"First 5 attributes of list: {dir(sample_data)[:5]}")

print("\n" + "=" * 50 + "\n")

# 6. LOGICAL FUNCTIONS
print("6. LOGICAL FUNCTIONS")
print("-" * 40)

bool_list_true = [True, True, True]
bool_list_mixed = [True, False, True]
bool_list_false = [False, False, False]

# all()
print(f"all({bool_list_true}) = {all(bool_list_true)}")
print(f"all({bool_list_mixed}) = {all(bool_list_mixed)}")
print(f"all({bool_list_false}) = {all(bool_list_false)}")

# any()
print(f"any({bool_list_true}) = {any(bool_list_true)}")
print(f"any({bool_list_mixed}) = {any(bool_list_mixed)}")
print(f"any({bool_list_false}) = {any(bool_list_false)}")

print("\n" + "=" * 50 + "\n")

# 7. ADVANCED FUNCTIONS
print("7. ADVANCED FUNCTIONS")
print("-" * 40)

# filter()
numbers_to_filter = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers_to_filter))
print(f"filter(even, {numbers_to_filter}) = {even_numbers}")

# map()
squares = list(map(lambda x: x**2, [1, 2, 3, 4, 5]))
print(f"map(square, [1, 2, 3, 4, 5]) = {squares}")

# eval() and exec() - be careful with these in real applications
expression = "2 + 3 * 4"
result = eval(expression)
print(f'eval("{expression}") = {result}')

# exec() example
code = "result = 5 * 6"
exec(code)
print(f'exec("{code}") creates: result = {locals().get("result", "not found")}')

print("\n" + "=" * 50 + "\n")
