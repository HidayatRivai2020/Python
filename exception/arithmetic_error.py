# ArithmeticError Examples

print("=== ArithmeticError Examples ===\n")

import math

# 1. Catching all arithmetic errors with ArithmeticError
print("1. Catching all arithmetic errors:")
def safe_math_operation(operation, a, b=None):
    try:
        if operation == "divide":
            return a / b
        elif operation == "power":
            return a ** b
        elif operation == "sqrt":
            return math.sqrt(a)
        elif operation == "overflow":
            # Simulate overflow (Python handles big numbers well, so this is conceptual)
            return float('inf') * 2
    except ArithmeticError as e:
        print(f"Arithmetic error in {operation}: {type(e).__name__} - {e}")
        return None

# Test different arithmetic errors
result = safe_math_operation("divide", 10, 0)  # ZeroDivisionError
print(f"Division result: {result}")

result = safe_math_operation("sqrt", -1)  # Would be ValueError, not ArithmeticError
print(f"Square root result: {result}")

# 2. ZeroDivisionError examples
print("\n2. ZeroDivisionError examples:")

# Division by zero
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Division by zero: {e}")

# Modulo by zero
try:
    result = 10 % 0
except ZeroDivisionError as e:
    print(f"Modulo by zero: {e}")

# Floor division by zero
try:
    result = 10 // 0
except ZeroDivisionError as e:
    print(f"Floor division by zero: {e}")

# divmod by zero
try:
    result = divmod(10, 0)
except ZeroDivisionError as e:
    print(f"divmod by zero: {e}")

# 3. OverflowError examples (rare in Python 3)
print("\n3. OverflowError examples:")

# Python 3 handles large integers automatically, but floats can overflow
try:
    # Force float overflow
    result = 10.0 ** 308  # This is fine
    print(f"Large number: {result}")
    
    result = 10.0 ** 309  # This might overflow
    print(f"Very large number: {result}")
    
    # Force overflow with math operations
    huge_number = 1.8e308
    result = huge_number * 10  # Should overflow
    print(f"Overflow result: {result}")
    
except OverflowError as e:
    print(f"OverflowError: {e}")

# 4. FloatingPointError examples (platform dependent)
print("\n4. FloatingPointError examples:")

# This is rare and platform-dependent
# Usually occurs with special floating point configurations
try:
    # Simulate floating point error conditions
    import sys
    print("FloatingPointError is rare in modern Python")
    print("It occurs with specific floating point configurations")
    
    # Example of operations that might trigger it
    result = float('nan') + 1
    print(f"NaN operation result: {result}")
    
    result = float('inf') - float('inf')
    print(f"Infinity operation result: {result}")
    
except FloatingPointError as e:
    print(f"FloatingPointError: {e}")

# 5. Creating custom arithmetic errors
print("\n5. Creating custom arithmetic errors:")

class CustomArithmeticError(ArithmeticError):
    """Custom arithmetic error for specific business logic"""
    pass

def business_calculation(value):
    try:
        if value < 0:
            raise CustomArithmeticError("Business rule: Value cannot be negative")
        if value > 1000000:
            raise CustomArithmeticError("Business rule: Value too large for calculation")
        
        # Perform calculation
        result = value * 1.05  # 5% increase
        return result
        
    except ArithmeticError as e:
        print(f"Arithmetic error in business calculation: {e}")
        return None

# Test custom arithmetic error
result = business_calculation(-100)
print(f"Business calculation result: {result}")

result = business_calculation(2000000)
print(f"Business calculation result: {result}")

result = business_calculation(500)
print(f"Business calculation result: {result}")

# 6. Handling multiple arithmetic errors specifically
print("\n6. Handling multiple arithmetic error types:")

def comprehensive_math_function(operation, x, y=None):
    try:
        if operation == "divide":
            if y == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return x / y
        
        elif operation == "power":
            if x == 0 and y < 0:
                raise ZeroDivisionError("0 raised to negative power")
            result = x ** y
            if result == float('inf'):
                raise OverflowError("Power operation resulted in overflow")
            return result
        
        elif operation == "log":
            if x <= 0:
                raise ValueError("Logarithm of non-positive number")
            return math.log(x)
            
    except ZeroDivisionError as e:
        print(f"Zero division error: {e}")
    except OverflowError as e:
        print(f"Overflow error: {e}")
    except ArithmeticError as e:
        print(f"Other arithmetic error: {e}")
    except ValueError as e:
        print(f"Value error (not arithmetic): {e}")
    
    return None

# Test comprehensive function
comprehensive_math_function("divide", 10, 0)
comprehensive_math_function("power", 0, -1)
comprehensive_math_function("power", 10, 1000)  # Might overflow
comprehensive_math_function("log", -5)

# 7. Safe arithmetic operations wrapper
print("\n7. Safe arithmetic operations wrapper:")

class SafeMath:
    @staticmethod
    def safe_divide(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            print(f"Cannot divide {a} by {b}: division by zero")
            return float('inf') if a > 0 else float('-inf')
    
    @staticmethod
    def safe_power(base, exponent):
        try:
            result = base ** exponent
            if result == float('inf') or result == float('-inf'):
                raise OverflowError("Power operation overflow")
            return result
        except (ZeroDivisionError, OverflowError) as e:
            print(f"Power operation failed: {e}")
            return None
    
    @staticmethod
    def safe_operation(func, *args):
        try:
            return func(*args)
        except ArithmeticError as e:
            print(f"Arithmetic operation failed: {type(e).__name__} - {e}")
            return None

# Test safe math operations
safe_math = SafeMath()
print(f"Safe divide: {safe_math.safe_divide(10, 0)}")
print(f"Safe power: {safe_math.safe_power(2, 1000)}")
print(f"Safe operation: {safe_math.safe_operation(lambda: 5/0)}")

print("\n=== ArithmeticError examples completed ===")