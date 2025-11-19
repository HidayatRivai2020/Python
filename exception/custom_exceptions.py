# Custom Exceptions Examples

print("=== Custom Exceptions Examples ===")

# 1. Basic Custom Exception
class CustomError(Exception):
    """A basic custom exception"""
    pass

print("1. Basic Custom Exception:")
try:
    raise CustomError("This is a custom error message")
except CustomError as e:
    print(f"CustomError caught: {e}")

print()

# 2. Custom Exception with additional attributes
class ValidationError(Exception):
    """Custom exception for validation errors"""
    def __init__(self, message, error_code=None):
        super().__init__(message)
        self.error_code = error_code

print("2. Custom Exception with attributes:")
try:
    raise ValidationError("Invalid email format", error_code=400)
except ValidationError as e:
    print(f"ValidationError caught: {e}")
    print(f"Error code: {e.error_code}")

print()
