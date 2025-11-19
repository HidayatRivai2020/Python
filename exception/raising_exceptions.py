print("=== Raising Exceptions Examples ===")

# 1. Basic raise statement
print("1. Basic raise statement:")
def check_positive(number):
    if number < 0:
        raise ValueError("Number must be positive")
    return number

try:
    check_positive(-5)
except ValueError as e:
    print(f"Exception raised: {e}")

print()

# 2. Raise with custom message
print("2. Raise with custom message:")
def validate_email(email):
    if "@" not in email:
        raise ValueError(f"Invalid email format: '{email}' - missing @ symbol")
    if "." not in email.split("@")[1]:
        raise ValueError(f"Invalid email format: '{email}' - missing domain extension")
    return True

try:
    validate_email("invalid-email")
except ValueError as e:
    print(f"Email validation failed: {e}")

print()

# 3. Re-raising exceptions
print("3. Re-raising exceptions:")
def process_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"Logging: File {filename} not found")
        raise  # Re-raise the same exception

try:
    process_file("nonexistent.txt")
except FileNotFoundError as e:
    print(f"File processing failed: {e}")

print()

# 4. Raise from another exception
print("4. Raise from another exception:")
def convert_to_int(value):
    try:
        return int(value)
    except ValueError as e:
        raise TypeError("Conversion failed") from e

try:
    convert_to_int("hello")
except TypeError as e:
    print(f"Conversion error: {e}")
    print(f"Original cause: {e.__cause__}")

print()

# 5. Conditional raising
print("5. Conditional raising:")
def validate_age_range(age, min_age=0, max_age=120):
    if not isinstance(age, int):
        raise TypeError(f"Age must be an integer, got {type(age).__name__}")
    
    if age < min_age:
        raise ValueError(f"Age {age} is below minimum age {min_age}")
    
    if age > max_age:
        raise ValueError(f"Age {age} is above maximum age {max_age}")
    
    return True

# Test different invalid inputs
test_cases = [25, "30", -5, 150]
for test_age in test_cases:
    try:
        validate_age_range(test_age)
        print(f"Age {test_age} is valid")
    except (TypeError, ValueError) as e:
        print(f"Invalid age {test_age}: {e}")

print()

# 6. Raise without arguments (re-raise last exception)
print("6. Re-raise last exception:")
def risky_operation():
    raise RuntimeError("Something went wrong")

def wrapper_function():
    try:
        risky_operation()
    except RuntimeError:
        print("Caught exception, doing some cleanup...")
        raise  # Re-raises the RuntimeError

try:
    wrapper_function()
except RuntimeError as e:
    print(f"Exception bubbled up: {e}")

print()

# 7. Assert statement (raises AssertionError)
print("7. Assert statement:")
def calculate_factorial(n):
    assert n >= 0, "Factorial is not defined for negative numbers"
    assert isinstance(n, int), "Factorial requires integer input"
    
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

try:
    print(f"Factorial of 5: {calculate_factorial(5)}")
    calculate_factorial(-3)  # This will raise AssertionError
except AssertionError as e:
    print(f"Assertion failed: {e}")

print()

# 8. Raise custom exception with context
print("8. Custom exception with context:")
class ValidationContext:
    def __init__(self, field_name):
        self.field_name = field_name
    
    def validate_required(self, value):
        if not value:
            raise ValueError(f"Field '{self.field_name}' is required")
    
    def validate_length(self, value, min_length):
        if len(value) < min_length:
            raise ValueError(f"Field '{self.field_name}' must be at least {min_length} characters long")

# Example usage
validator = ValidationContext("username")
try:
    username = ""
    validator.validate_required(username)
    validator.validate_length(username, 3)
except ValueError as e:
    print(f"Validation error: {e}")

print("\n=== All raising exceptions examples completed ===")