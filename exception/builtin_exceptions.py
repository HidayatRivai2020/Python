# Built-in Exceptions Examples

print("=== Built-in Exceptions Examples ===\n")

# 1. ValueError - When a function receives an argument of correct type but inappropriate value
print("1. ValueError Example:")
try:
    number = int("hello")  # Cannot convert "hello" to integer
except ValueError as e:
    print(f"ValueError caught: {e}")

# 2. TypeError - When an operation is performed on inappropriate type
print("2. TypeError Example:")
try:
    result = "hello" + 5  # Cannot add string and integer
except TypeError as e:
    print(f"TypeError caught: {e}")

# 3. IndexError - When trying to access an index that doesn't exist
print("3. IndexError Example:")
try:
    my_list = [1, 2, 3]
    value = my_list[10]  # Index 10 doesn't exist
except IndexError as e:
    print(f"IndexError caught: {e}")

# 4. KeyError - When trying to access a dictionary key that doesn't exist
print("4. KeyError Example:")
try:
    my_dict = {"name": "John", "age": 30}
    value = my_dict["address"]  # Key "address" doesn't exist
except KeyError as e:
    print(f"KeyError caught: {e}")

# 5. ZeroDivisionError - When dividing by zero
print("5. ZeroDivisionError Example:")
try:
    result = 10 / 0  # Division by zero
except ZeroDivisionError as e:
    print(f"ZeroDivisionError caught: {e}")

# 6. FileNotFoundError - When trying to open a file that doesn't exist
print("6. FileNotFoundError Example:")
try:
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError as e:
    print(f"FileNotFoundError caught: {e}")

# 7. AttributeError - When trying to access an attribute that doesn't exist
print("7. AttributeError Example:")
try:
    my_string = "hello"
    my_string.nonexistent_method()  # Method doesn't exist
except AttributeError as e:
    print(f"AttributeError caught: {e}")

# 8. ImportError - When import statement fails
print("8. ImportError Example:")
try:
    import nonexistent_module  # Module doesn't exist
except ImportError as e:
    print(f"ImportError caught: {e}")

print("\n=== All built-in exception examples completed ===")