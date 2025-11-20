print("=== Raise Statement Examples ===")

# 1. Basic raise with built-in exceptions
print("1. Basic raise with built-in exceptions:")

def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems unrealistic")
    return age

try:
    validate_age(-5)
except ValueError as e:
    print(f"Validation error: {e}")

try:
    validate_age(200)
except ValueError as e:
    print(f"Validation error: {e}")

# 2. Raise different exception types
print("\n2. Different exception types:")

def process_user_input(data):
    if not isinstance(data, str):
        raise TypeError(f"Expected string, got {type(data).__name__}")
    
    if not data:
        raise ValueError("Input cannot be empty")
    
    if len(data) < 3:
        raise ValueError("Input must be at least 3 characters long")
    
    return data.upper()

try:
    process_user_input(123)
except TypeError as e:
    print(f"Type error: {e}")

try:
    process_user_input("")
except ValueError as e:
    print(f"Value error: {e}")

try:
    process_user_input("Hi")
except ValueError as e:
    print(f"Value error: {e}")

# 3. Re-raising exceptions
print("\n3. Re-raising exceptions:")

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Logging: Division by zero attempted")
        raise  # Re-raise the same exception

try:
    result = safe_divide(10, 0)
except ZeroDivisionError:
    print("Caught re-raised ZeroDivisionError")

# 4. Raising exceptions in except blocks
print("\n4. Raising different exceptions in except blocks:")

def read_file_content(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        raise RuntimeError(f"Configuration file {filename} is missing")
    except PermissionError:
        raise RuntimeError(f"No permission to read {filename}")

try:
    content = read_file_content("nonexistent.txt")
except RuntimeError as e:
    print(f"Runtime error: {e}")

# 5. Conditional raising
print("\n5. Conditional raising:")

def withdraw_money(balance, amount):
    if amount <= 0:
        raise ValueError("Withdrawal amount must be positive")
    
    if amount > balance:
        raise ValueError(f"Insufficient funds. Balance: ${balance}, Requested: ${amount}")
    
    return balance - amount

try:
    new_balance = withdraw_money(100, 150)
except ValueError as e:
    print(f"Transaction failed: {e}")

# 6. Raising without arguments (only in except blocks)
print("\n6. Re-raising current exception:")

def risky_operation():
    return 1 / 0

def logged_operation():
    try:
        return risky_operation()
    except:
        print("Operation failed, logging error...")
        raise  # Re-raise current exception without arguments

try:
    logged_operation()
except ZeroDivisionError:
    print("Caught the re-raised exception")

# 7. Custom exception classes with raise
print("\n7. Custom exceptions:")

class CustomError(Exception):
    """Custom exception for specific business logic"""
    def __init__(self, message, error_code=None):
        super().__init__(message)
        self.error_code = error_code

class ValidationError(CustomError):
    """Specific validation error"""
    pass

def validate_email(email):
    if '@' not in email:
        raise ValidationError("Email must contain @ symbol", error_code="INVALID_FORMAT")
    
    if not email.endswith('.com'):
        raise ValidationError("Email must end with .com", error_code="INVALID_DOMAIN")

try:
    validate_email("invalid-email")
except ValidationError as e:
    print(f"Validation failed: {e} (Code: {e.error_code})")

try:
    validate_email("test@example.org")
except ValidationError as e:
    print(f"Validation failed: {e} (Code: {e.error_code})")

# 8. Raise with exception chaining
print("\n8. Exception chaining:")

def parse_config(config_str):
    try:
        return eval(config_str)  # Dangerous, just for example
    except SyntaxError as e:
        raise ValueError("Invalid configuration format") from e

try:
    parse_config("{'key': invalid_syntax}")
except ValueError as e:
    print(f"Main error: {e}")
    print(f"Caused by: {e.__cause__}")

print("\n=== Raise statement examples completed ===")