# AssertionError Examples

print("=== AssertionError Examples ===")

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
