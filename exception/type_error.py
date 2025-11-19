print("=== TypeError Examples ===")

# 1. Basic TypeError examples
print("1. Basic TypeError examples:")

# Unsupported operand types
try:
    result = "hello" + 123
except TypeError as e:
    print(f"Type mismatch error: {e}")

# Multiplication type error
try:
    result = "text" * "another"
except TypeError as e:
    print(f"Multiplication type error: {e}")

# Comparison type error
try:
    result = 5 > "hello"
except TypeError as e:
    print(f"Comparison type error: {e}")

# 2. Function call errors
print("\n2. Function call errors:")

# Wrong number of arguments
def greet(name, age):
    return f"Hello {name}, you are {age} years old"

try:
    result = greet("Alice")  # Missing age argument
except TypeError as e:
    print(f"Missing argument error: {e}")

# Too many arguments
try:
    result = greet("Alice", 25, "Engineer")  # Extra argument
except TypeError as e:
    print(f"Too many arguments error: {e}")

# Calling non-callable object
try:
    my_string = "hello"
    result = my_string()  # Strings are not callable
except TypeError as e:
    print(f"Non-callable error: {e}")

# 3. Indexing and slicing errors
print("\n3. Indexing and slicing errors:")

# Indexing non-sequence
try:
    number = 123
    digit = number[0]  # Numbers don't support indexing
except TypeError as e:
    print(f"Indexing error: {e}")

# Slicing with wrong type
try:
    my_list = [1, 2, 3, 4, 5]
    subset = my_list["1":"3"]  # Slice indices must be integers
except TypeError as e:
    print(f"Slicing error: {e}")

# 4. Dictionary key errors
print("\n4. Dictionary key errors:")

# Unhashable type as dictionary key
try:
    my_dict = {[1, 2, 3]: "value"}  # Lists are not hashable
except TypeError as e:
    print(f"Unhashable key error: {e}")

# Dictionary as key
try:
    my_dict = {{"nested": "dict"}: "value"}  # Dicts are not hashable
except TypeError as e:
    print(f"Dictionary key error: {e}")

# 5. Iteration errors
print("\n5. Iteration errors:")

# Iterating over non-iterable
try:
    for item in 123:  # Numbers are not iterable
        print(item)
except TypeError as e:
    print(f"Iteration error: {e}")

# join() with wrong type
try:
    result = ", ".join(123)  # join() needs iterable of strings
except TypeError as e:
    print(f"Join error: {e}")

try:
    result = ", ".join([1, 2, 3])  # join() needs strings, not integers
except TypeError as e:
    print(f"Join type error: {e}")

# 6. Method attribute errors vs TypeError
print("\n6. Method and attribute access:")

# Wrong method call on string
try:
    text = "hello world"
    result = text.append("!")  # Strings don't have append method
except AttributeError as e:
    print(f"AttributeError (not TypeError): {e}")

# Calling method with wrong argument types
try:
    text = "hello"
    result = text.replace(123, "world")  # replace() needs strings
except TypeError as e:
    print(f"Method argument type error: {e}")

# 7. Type checking and prevention
print("\n7. Type checking and prevention:")

def safe_add(a, b):
    """Safely add two values with type checking"""
    try:
        # Check if both operands support addition
        return a + b
    except TypeError as e:
        print(f"Addition failed: {e}")
        
        # Try type conversion
        try:
            if isinstance(a, str) or isinstance(b, str):
                return str(a) + str(b)
            else:
                return float(a) + float(b)
        except (TypeError, ValueError) as conversion_error:
            print(f"Conversion also failed: {conversion_error}")
            return None

# Test safe addition
test_pairs = [
    (5, 3),
    ("hello", " world"),
    (5, "text"),
    ([1, 2], [3, 4]),
    ({"a": 1}, {"b": 2}),  # This will fail
]

for a, b in test_pairs:
    result = safe_add(a, b)
    print(f"{a} + {b} = {result}")

# 8. Custom TypeError for type validation
print("\n8. Custom TypeError for type validation:")

def validate_types(func):
    """Decorator to validate function argument types"""
    def wrapper(*args, **kwargs):
        # Get function annotations
        annotations = func.__annotations__
        
        # Check positional arguments
        param_names = list(func.__code__.co_varnames[:func.__code__.co_argcount])
        
        for i, (arg, param_name) in enumerate(zip(args, param_names)):
            if param_name in annotations:
                expected_type = annotations[param_name]
                if not isinstance(arg, expected_type):
                    raise TypeError(
                        f"Argument '{param_name}' must be {expected_type.__name__}, "
                        f"got {type(arg).__name__}"
                    )
        
        # Check keyword arguments
        for param_name, arg in kwargs.items():
            if param_name in annotations:
                expected_type = annotations[param_name]
                if not isinstance(arg, expected_type):
                    raise TypeError(
                        f"Argument '{param_name}' must be {expected_type.__name__}, "
                        f"got {type(arg).__name__}"
                    )
        
        return func(*args, **kwargs)
    return wrapper

@validate_types
def calculate_area(length: float, width: float) -> float:
    """Calculate rectangle area with type validation"""
    return length * width

@validate_types
def format_name(first: str, last: str) -> str:
    """Format full name with type validation"""
    return f"{first} {last}"

# Test type validation
try:
    area = calculate_area(5.0, 3.0)
    print(f"Valid area calculation: {area}")
except TypeError as e:
    print(f"Type validation error: {e}")

try:
    area = calculate_area("5", 3.0)  # Wrong type
    print(f"Area: {area}")
except TypeError as e:
    print(f"Type validation error: {e}")

try:
    name = format_name("John", "Doe")
    print(f"Valid name: {name}")
except TypeError as e:
    print(f"Type validation error: {e}")

try:
    name = format_name("John", 123)  # Wrong type
    print(f"Name: {name}")
except TypeError as e:
    print(f"Type validation error: {e}")

# 9. TypeError in data structures
print("\n9. TypeError in data structures:")

def safe_data_operation(data, operation):
    """Perform operations on data with type safety"""
    try:
        if operation == "sort":
            return sorted(data)
        elif operation == "sum":
            return sum(data)
        elif operation == "max":
            return max(data)
        elif operation == "join":
            return "".join(data)
        elif operation == "reverse":
            return data[::-1]
    except TypeError as e:
        print(f"Operation '{operation}' failed: {e}")
        return None

# Test different data types and operations
test_data = [
    ([3, 1, 4, 1, 5], "sort"),
    ([1, 2, 3, 4, 5], "sum"),
    (["a", "b", "c"], "join"),
    ([1, "2", 3], "sum"),  # Mixed types - will fail
    ("hello", "reverse"),
    (123, "reverse"),  # Not subscriptable - will fail
]

for data, operation in test_data:
    result = safe_data_operation(data, operation)
    print(f"{operation}({data}) = {result}")

# 10. TypeError with class instances
print("\n10. TypeError with class instances:")

class Calculator:
    def add(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError(f"Calculator only works with numbers, got {type(a).__name__} and {type(b).__name__}")
        return a + b

calc = Calculator()

# Test with valid types
try:
    result = calc.add(5, 3)
    print(f"Calculator result: {result}")
except TypeError as e:
    print(f"Calculator error: {e}")

# Test with invalid types
try:
    result = calc.add("5", 3)
    print(f"Calculator result: {result}")
except TypeError as e:
    print(f"Calculator error: {e}")

# Trying to add instances incorrectly
try:
    result = calc + 5  # Calculator doesn't support addition operator
except TypeError as e:
    print(f"Object operation error: {e}")

print("\n=== TypeError examples completed ===")