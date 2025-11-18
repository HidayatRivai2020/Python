# Custom Exceptions Examples

print("=== Custom Exceptions Examples ===\n")

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

# 3. Age Validation Custom Exception
class InvalidAgeError(ValueError):
    """Custom exception for invalid age values"""
    def __init__(self, age, message="Age must be between 0 and 150"):
        self.age = age
        self.message = message
        super().__init__(self.message)
        
    def __str__(self):
        return f"Invalid age {self.age}: {self.message}"

def validate_age(age):
    if age < 0 or age > 150:
        raise InvalidAgeError(age)
    return True

print("3. Age Validation Exception:")
try:
    validate_age(200)
except InvalidAgeError as e:
    print(f"InvalidAgeError caught: {e}")

print()

# 4. Banking Custom Exceptions
class InsufficientFundsError(Exception):
    """Raised when account has insufficient funds"""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        message = f"Insufficient funds. Balance: ${balance}, Attempted withdrawal: ${amount}"
        super().__init__(message)

class Account:
    def __init__(self, balance=0):
        self.balance = balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return self.balance

print("4. Banking Exception:")
account = Account(100)
try:
    account.withdraw(150)
except InsufficientFundsError as e:
    print(f"Banking error: {e}")

print()

# 5. Multiple Custom Exception Hierarchy
class DatabaseError(Exception):
    """Base exception for database operations"""
    pass

class ConnectionError(DatabaseError):
    """Exception for database connection issues"""
    pass

class QueryError(DatabaseError):
    """Exception for SQL query issues"""
    pass

print("5. Exception Hierarchy:")
try:
    raise ConnectionError("Failed to connect to database")
except DatabaseError as e:  # Catches any DatabaseError subclass
    print(f"Database operation failed: {e}")
    print(f"Exception type: {type(e).__name__}")

print("\n=== All custom exception examples completed ===")