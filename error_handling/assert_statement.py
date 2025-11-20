print("=== Assert Statement Examples ===")

# 1. Basic assert statements
print("1. Basic assert statements:")

def basic_math(x, y):
    assert isinstance(x, (int, float)), "x must be a number"
    assert isinstance(y, (int, float)), "y must be a number"
    assert y != 0, "y cannot be zero for division"
    
    return x / y

try:
    result = basic_math(10, 2)
    print(f"Division result: {result}")
except AssertionError as e:
    print(f"Assertion failed: {e}")

try:
    result = basic_math("10", 2)
except AssertionError as e:
    print(f"Assertion failed: {e}")

try:
    result = basic_math(10, 0)
except AssertionError as e:
    print(f"Assertion failed: {e}")

# 2. Assert for input validation
print("\n2. Input validation with assert:")

def calculate_average(numbers):
    assert isinstance(numbers, list), "Input must be a list"
    assert len(numbers) > 0, "List cannot be empty"
    assert all(isinstance(n, (int, float)) for n in numbers), "All items must be numbers"
    
    return sum(numbers) / len(numbers)

try:
    avg = calculate_average([1, 2, 3, 4, 5])
    print(f"Average: {avg}")
except AssertionError as e:
    print(f"Assertion failed: {e}")

try:
    avg = calculate_average([])
except AssertionError as e:
    print(f"Assertion failed: {e}")

try:
    avg = calculate_average([1, 2, "3", 4])
except AssertionError as e:
    print(f"Assertion failed: {e}")

# 3. Assert for preconditions and postconditions
print("\n3. Function preconditions and postconditions:")

def factorial(n):
    # Precondition
    assert isinstance(n, int), "n must be an integer"
    assert n >= 0, "n must be non-negative"
    
    if n == 0 or n == 1:
        result = 1
    else:
        result = n * factorial(n - 1)
    
    # Postcondition
    assert result > 0, "Factorial result must be positive"
    assert isinstance(result, int), "Factorial result must be an integer"
    
    return result

try:
    fact = factorial(5)
    print(f"Factorial of 5: {fact}")
except AssertionError as e:
    print(f"Assertion failed: {e}")

try:
    fact = factorial(-3)
except AssertionError as e:
    print(f"Assertion failed: {e}")

# 4. Assert for debugging assumptions
print("\n4. Debugging with assert:")

def process_data(data):
    assert data is not None, "Data should not be None at this point"
    
    # Simulate processing
    processed = []
    for item in data:
        assert item is not None, f"Found None item in data: {data}"
        processed.append(item * 2)
    
    assert len(processed) == len(data), "Processed data length mismatch"
    return processed

try:
    result = process_data([1, 2, 3, 4])
    print(f"Processed data: {result}")
except AssertionError as e:
    print(f"Assertion failed: {e}")

try:
    result = process_data([1, None, 3])
except AssertionError as e:
    print(f"Assertion failed: {e}")

# 5. Assert with complex conditions
print("\n5. Complex assert conditions:")

def create_user_account(username, password, email):
    # Username validation
    assert isinstance(username, str) and len(username) >= 3, "Username must be string with at least 3 characters"
    assert username.isalnum(), "Username must contain only letters and numbers"
    
    # Password validation
    assert isinstance(password, str) and len(password) >= 8, "Password must be string with at least 8 characters"
    assert any(c.isupper() for c in password), "Password must contain at least one uppercase letter"
    assert any(c.islower() for c in password), "Password must contain at least one lowercase letter"
    assert any(c.isdigit() for c in password), "Password must contain at least one digit"
    
    # Email validation
    assert isinstance(email, str) and '@' in email and '.' in email, "Email must be valid format"
    
    return {"username": username, "password": "***", "email": email}

try:
    user = create_user_account("johndoe", "SecurePass123", "john@example.com")
    print(f"User created: {user}")
except AssertionError as e:
    print(f"User creation failed: {e}")

try:
    user = create_user_account("jo", "weak", "invalid-email")
except AssertionError as e:
    print(f"User creation failed: {e}")

# 6. Assert vs raise comparison
print("\n6. When to use assert vs raise:")

def example_function(value):
    # Use assert for debugging and development checks
    assert value is not None, "Development check: value should not be None"
    
    # Use raise for production error handling
    if not isinstance(value, (int, float)):
        raise TypeError("Production error: value must be a number")
    
    if value < 0:
        raise ValueError("Production error: value must be non-negative")
    
    return value ** 2

try:
    result = example_function(4)
    print(f"Square: {result}")
except (AssertionError, TypeError, ValueError) as e:
    print(f"Error: {type(e).__name__}: {e}")

# 7. Assert in different contexts
print("\n7. Assert in different contexts:")

class BankAccount:
    def __init__(self, initial_balance=0):
        assert initial_balance >= 0, "Initial balance cannot be negative"
        self.balance = initial_balance
    
    def deposit(self, amount):
        assert amount > 0, "Deposit amount must be positive"
        old_balance = self.balance
        self.balance += amount
        assert self.balance == old_balance + amount, "Balance calculation error"
    
    def withdraw(self, amount):
        assert amount > 0, "Withdrawal amount must be positive"
        assert amount <= self.balance, "Insufficient funds"
        old_balance = self.balance
        self.balance -= amount
        assert self.balance == old_balance - amount, "Balance calculation error"

try:
    account = BankAccount(100)
    account.deposit(50)
    print(f"Balance after deposit: {account.balance}")
    account.withdraw(30)
    print(f"Balance after withdrawal: {account.balance}")
except AssertionError as e:
    print(f"Bank operation failed: {e}")

# 8. Disabling assertions
print("\n8. Note about disabling assertions:")
print("Assertions can be disabled with 'python -O script.py'")
print("This is why assertions should NOT be used for production error handling")
print("Use assertions for debugging and development checks only")

# Example of what happens when assertions are disabled
def debug_function():
    assert False, "This assertion will be ignored with -O flag"
    print("This line will execute when assertions are disabled")

print("\nTo test assertion disabling:")
print("Run: python -O assert_statement.py")
print("The assertion will be ignored and the function will complete normally")

print("\n=== Assert statement examples completed ===")