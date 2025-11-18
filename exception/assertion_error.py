# AssertionError Examples

print("=== AssertionError Examples ===\n")

# 1. Basic assert statement examples
print("1. Basic assert statement examples:")

# Simple assertion that passes
try:
    x = 5
    assert x > 0  # This passes
    print("Assertion passed: x > 0")
except AssertionError as e:
    print(f"Assertion failed: {e}")

# Simple assertion that fails
try:
    y = -3
    assert y > 0  # This fails
    print("This won't be printed")
except AssertionError as e:
    print(f"Assertion failed: {e}")

# Assertion with custom message
try:
    age = -5
    assert age >= 0, f"Age cannot be negative, got {age}"
except AssertionError as e:
    print(f"Assertion with message: {e}")

# 2. Assert in function validation
print("\n2. Assert in function validation:")

def calculate_square_root(number):
    """Calculate square root with assertion validation"""
    assert isinstance(number, (int, float)), f"Input must be a number, got {type(number).__name__}"
    assert number >= 0, f"Cannot calculate square root of negative number: {number}"
    
    return number ** 0.5

# Test function validation
test_values = [16, -4, "not_a_number", 0, 25.0]

for value in test_values:
    try:
        result = calculate_square_root(value)
        print(f"sqrt({value}) = {result}")
    except AssertionError as e:
        print(f"Input validation failed: {e}")

# 3. Assert for debugging and development
print("\n3. Assert for debugging and development:")

def process_list(items):
    """Process list with debugging assertions"""
    # Pre-condition assertions
    assert isinstance(items, list), "Input must be a list"
    assert len(items) > 0, "List cannot be empty"
    
    # Process the list
    total = 0
    for item in items:
        assert isinstance(item, (int, float)), f"All items must be numbers, found {type(item).__name__}: {item}"
        total += item
    
    # Post-condition assertion
    average = total / len(items)
    assert isinstance(average, (int, float)), "Average calculation failed"
    assert len(items) > 0, "Division by zero should not happen"
    
    return average

# Test list processing
test_lists = [
    [1, 2, 3, 4, 5],
    [],  # Empty list
    [1, 2, "three", 4],  # Mixed types
    [10, 20, 30],
]

for lst in test_lists:
    try:
        avg = process_list(lst)
        print(f"Average of {lst}: {avg}")
    except AssertionError as e:
        print(f"Processing failed: {e}")

# 4. Assert for class invariants
print("\n4. Assert for class invariants:")

class BankAccount:
    """Bank account with assertion-based invariants"""
    
    def __init__(self, initial_balance=0):
        assert initial_balance >= 0, "Initial balance cannot be negative"
        self._balance = initial_balance
        self._transaction_count = 0
    
    def deposit(self, amount):
        assert amount > 0, f"Deposit amount must be positive, got {amount}"
        
        old_balance = self._balance
        self._balance += amount
        self._transaction_count += 1
        
        # Invariant checks
        assert self._balance > old_balance, "Balance should increase after deposit"
        assert self._transaction_count > 0, "Transaction count should be positive"
    
    def withdraw(self, amount):
        assert amount > 0, f"Withdrawal amount must be positive, got {amount}"
        assert amount <= self._balance, f"Insufficient funds: {amount} > {self._balance}"
        
        old_balance = self._balance
        self._balance -= amount
        self._transaction_count += 1
        
        # Invariant checks
        assert self._balance < old_balance, "Balance should decrease after withdrawal"
        assert self._balance >= 0, "Balance cannot be negative after withdrawal"
    
    def get_balance(self):
        assert self._balance >= 0, "Balance invariant violated"
        return self._balance
    
    def get_transaction_count(self):
        assert self._transaction_count >= 0, "Transaction count cannot be negative"
        return self._transaction_count

# Test bank account
account = BankAccount(100)
print(f"Initial balance: {account.get_balance()}")

operations = [
    ("deposit", 50),
    ("withdraw", 30),
    ("withdraw", 200),  # This should fail
    ("deposit", -10),   # This should fail
]

for operation, amount in operations:
    try:
        if operation == "deposit":
            account.deposit(amount)
            print(f"Deposited {amount}, new balance: {account.get_balance()}")
        elif operation == "withdraw":
            account.withdraw(amount)
            print(f"Withdrew {amount}, new balance: {account.get_balance()}")
    except AssertionError as e:
        print(f"Operation failed: {e}")

print(f"Total transactions: {account.get_transaction_count()}")

# 5. Assert in testing scenarios
print("\n5. Assert in testing scenarios:")

def simple_test_framework():
    """Simple testing framework using assertions"""
    
    def test_math_operations():
        print("Testing math operations...")
        
        # Test addition
        result = 2 + 3
        assert result == 5, f"2 + 3 should be 5, got {result}"
        
        # Test multiplication
        result = 4 * 5
        assert result == 20, f"4 * 5 should be 20, got {result}"
        
        # Test division
        result = 10 / 2
        assert result == 5.0, f"10 / 2 should be 5.0, got {result}"
        
        print("All math tests passed!")
    
    def test_string_operations():
        print("Testing string operations...")
        
        # Test string concatenation
        result = "Hello" + " World"
        assert result == "Hello World", f"String concatenation failed: {result}"
        
        # Test string length
        result = len("Python")
        assert result == 6, f"Length of 'Python' should be 6, got {result}"
        
        # Test string upper
        result = "hello".upper()
        assert result == "HELLO", f"Uppercase conversion failed: {result}"
        
        print("All string tests passed!")
    
    def test_list_operations():
        print("Testing list operations...")
        
        # Test list append
        my_list = [1, 2, 3]
        my_list.append(4)
        assert my_list == [1, 2, 3, 4], f"List append failed: {my_list}"
        
        # Test list length
        assert len(my_list) == 4, f"List length should be 4, got {len(my_list)}"
        
        # Intentional failure for demonstration
        try:
            assert my_list[0] == 999, f"First element should be 999, got {my_list[0]}"
        except AssertionError as e:
            print(f"Expected test failure: {e}")
        
        print("List tests completed (one intentional failure)!")
    
    # Run all tests
    tests = [test_math_operations, test_string_operations, test_list_operations]
    
    for test in tests:
        try:
            test()
        except AssertionError as e:
            print(f"Test failed: {e}")

simple_test_framework()

# 6. Assert for algorithm validation
print("\n6. Assert for algorithm validation:")

def binary_search(arr, target):
    """Binary search with assertion validation"""
    # Pre-conditions
    assert isinstance(arr, list), "Input must be a list"
    assert all(isinstance(x, (int, float)) for x in arr), "All elements must be numbers"
    assert arr == sorted(arr), "Array must be sorted for binary search"
    
    left, right = 0, len(arr) - 1
    
    while left <= right:
        # Loop invariants
        assert 0 <= left <= len(arr), f"Left index out of bounds: {left}"
        assert -1 <= right < len(arr), f"Right index out of bounds: {right}"
        
        mid = (left + right) // 2
        assert left <= mid <= right, f"Mid index should be between left and right: {left} <= {mid} <= {right}"
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Test binary search
test_cases = [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5),
    ([1, 3, 5, 7, 9], 4),
    ([2, 4, 6, 8], 6),
    ([5, 3, 1], 3),  # Unsorted array - should fail assertion
]

for arr, target in test_cases:
    try:
        index = binary_search(arr, target)
        if index != -1:
            print(f"Found {target} at index {index} in {arr}")
        else:
            print(f"{target} not found in {arr}")
    except AssertionError as e:
        print(f"Binary search validation failed: {e}")

# 7. Assert with complex conditions
print("\n7. Assert with complex conditions:")

def validate_user_data(user_data):
    """Validate user data with complex assertions"""
    
    # Check data structure
    assert isinstance(user_data, dict), "User data must be a dictionary"
    
    # Required fields
    required_fields = ["name", "email", "age"]
    for field in required_fields:
        assert field in user_data, f"Missing required field: {field}"
    
    # Field type validations
    assert isinstance(user_data["name"], str), "Name must be a string"
    assert isinstance(user_data["email"], str), "Email must be a string"
    assert isinstance(user_data["age"], int), "Age must be an integer"
    
    # Field value validations
    assert len(user_data["name"]) > 0, "Name cannot be empty"
    assert "@" in user_data["email"], "Email must contain @ symbol"
    assert "." in user_data["email"], "Email must contain domain extension"
    assert 0 <= user_data["age"] <= 150, f"Age must be between 0 and 150, got {user_data['age']}"
    
    # Complex validation
    assert len(user_data["name"]) >= 2, "Name must be at least 2 characters"
    assert user_data["email"].count("@") == 1, "Email must contain exactly one @ symbol"
    
    print(f"User data validation passed for: {user_data['name']}")

# Test user data validation
test_users = [
    {"name": "John Doe", "email": "john@example.com", "age": 30},
    {"name": "Jane", "email": "jane.smith@domain.org", "age": 25},
    {"name": "", "email": "empty@test.com", "age": 20},  # Empty name
    {"name": "Bob", "email": "invalid-email", "age": 35},  # Invalid email
    {"name": "Alice", "email": "alice@test.com", "age": 200},  # Invalid age
]

for user in test_users:
    try:
        validate_user_data(user)
    except AssertionError as e:
        print(f"User validation failed: {e}")

# 8. Assert optimization demonstration
print("\n8. Assert optimization demonstration:")

def demonstrate_assert_optimization():
    """Demonstrate that assertions can be optimized away"""
    
    print("Assertions are enabled in this run")
    print("Note: Run with 'python -O script.py' to disable assertions")
    
    # This assertion will be removed with -O flag
    debug_mode = True
    assert debug_mode, "Debug mode should be enabled"
    
    if __debug__:
        print("__debug__ is True - assertions are active")
    else:
        print("__debug__ is False - assertions are optimized away")
    
    # Code that relies on assertions for debugging
    data = [1, 2, 3, 4, 5]
    
    def process_item(item):
        assert isinstance(item, int), f"Item must be integer: {item}"
        # This assertion helps during development but is removed in production
        return item * 2
    
    try:
        results = [process_item(x) for x in data]
        print(f"Processed data: {results}")
    except AssertionError as e:
        print(f"Processing assertion failed: {e}")

demonstrate_assert_optimization()

# 9. Assert vs exceptions comparison
print("\n9. Assert vs exceptions comparison:")

def compare_assert_vs_exception():
    """Compare when to use assert vs raising exceptions"""
    
    def function_with_assert(value):
        """Use assert for debugging and development checks"""
        assert isinstance(value, int), "Development check: value should be int"
        assert value >= 0, "Development check: value should be non-negative"
        return value ** 2
    
    def function_with_exception(value):
        """Use exceptions for runtime error handling"""
        if not isinstance(value, int):
            raise TypeError(f"Value must be integer, got {type(value).__name__}")
        if value < 0:
            raise ValueError(f"Value must be non-negative, got {value}")
        return value ** 2
    
    test_values = [4, -2, "string", 0]
    
    print("Testing with assertions (for debugging):")
    for val in test_values:
        try:
            result = function_with_assert(val)
            print(f"Assert function({val}) = {result}")
        except AssertionError as e:
            print(f"Assert failed: {e}")
    
    print("\nTesting with exceptions (for runtime handling):")
    for val in test_values:
        try:
            result = function_with_exception(val)
            print(f"Exception function({val}) = {result}")
        except (TypeError, ValueError) as e:
            print(f"Runtime error: {e}")

compare_assert_vs_exception()

# 10. Best practices for assertions
print("\n10. Best practices for assertions:")

def assertion_best_practices():
    """Demonstrate best practices for using assertions"""
    
    # ✅ Good: Use assertions for debugging and documenting assumptions
    def calculate_average(numbers):
        assert isinstance(numbers, list), "Input should be a list"
        assert len(numbers) > 0, "Cannot calculate average of empty list"
        assert all(isinstance(n, (int, float)) for n in numbers), "All elements should be numbers"
        
        total = sum(numbers)
        avg = total / len(numbers)
        
        # Document post-conditions
        assert isinstance(avg, (int, float)), "Average should be a number"
        return avg
    
    # ✅ Good: Use descriptive messages
    def withdraw_money(balance, amount):
        assert amount > 0, f"Withdrawal amount must be positive, got {amount}"
        assert amount <= balance, f"Insufficient funds: trying to withdraw {amount} from balance {balance}"
        return balance - amount
    
    # ❌ Bad: Don't use assertions for user input validation in production
    def bad_user_validation(email):
        # This is wrong - user input should use proper exceptions
        assert "@" in email, "Email must contain @"  # Don't do this!
        return True
    
    # ✅ Good: Proper user input validation
    def good_user_validation(email):
        if "@" not in email:
            raise ValueError("Email must contain @ symbol")
        return True
    
    # Test examples
    print("Good practices examples:")
    
    # Test average calculation
    try:
        avg = calculate_average([1, 2, 3, 4, 5])
        print(f"Average calculation: {avg}")
    except AssertionError as e:
        print(f"Average calculation assertion: {e}")
    
    # Test money withdrawal
    try:
        new_balance = withdraw_money(100, 50)
        print(f"Withdrawal successful: new balance = {new_balance}")
    except AssertionError as e:
        print(f"Withdrawal assertion: {e}")
    
    # Test validation approaches
    print("\nValidation comparison:")
    
    try:
        bad_user_validation("invalid_email")
    except AssertionError as e:
        print(f"Bad validation (assertion): {e}")
    
    try:
        good_user_validation("invalid_email")
    except ValueError as e:
        print(f"Good validation (exception): {e}")

assertion_best_practices()

print("\n=== AssertionError examples completed ===")
print("\nKey takeaways:")
print("1. Use assert for debugging and documenting assumptions")
print("2. Use exceptions for runtime error handling")
print("3. Assertions can be disabled with -O flag")
print("4. Include descriptive messages in assert statements")
print("5. Don't rely on assertions for production error handling")