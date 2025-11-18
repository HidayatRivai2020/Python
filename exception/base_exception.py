# BaseException Examples

print("=== BaseException Examples ===\n")

# 1. Understanding BaseException hierarchy
print("1. BaseException hierarchy demonstration:")
try:
    # This will raise SystemExit (subclass of BaseException)
    import sys
    sys.exit("Attempting to exit")
except BaseException as e:
    print(f"Caught BaseException: {type(e).__name__}")
    print(f"Message: {e}")

# 2. Difference between Exception and BaseException
print("\n2. Catching BaseException vs Exception:")

def test_exception_catching():
    try:
        # Simulate KeyboardInterrupt (BaseException subclass)
        raise KeyboardInterrupt("Simulated Ctrl+C")
    except Exception:
        print("This won't catch KeyboardInterrupt")
    except BaseException as e:
        print(f"BaseException caught: {type(e).__name__}")

test_exception_catching()

# 3. Why you should rarely catch BaseException
print("\n3. Best practices demonstration:")
try:
    # Normal application exception
    raise ValueError("This is a regular exception")
except Exception as e:
    print(f"Good practice - caught Exception: {e}")

try:
    # System exception
    raise SystemExit(0)
except Exception as e:
    print("This won't execute - SystemExit not caught by Exception")
except BaseException as e:
    print(f"Caught system exception: {type(e).__name__}")
    print("Generally, you should let system exceptions propagate")

# 4. Creating custom exceptions (should inherit from Exception, not BaseException)
print("\n4. Custom exception inheritance:")

# Bad practice (don't do this)
class BadCustomException(BaseException):
    pass

# Good practice
class GoodCustomException(Exception):
    pass

try:
    raise GoodCustomException("This is the recommended way")
except Exception as e:
    print(f"Custom exception caught properly: {e}")

# 5. BaseException attributes
print("\n5. BaseException attributes:")
try:
    raise ValueError("Example error with args")
except BaseException as e:
    print(f"Exception type: {type(e).__name__}")
    print(f"Exception args: {e.args}")
    print(f"String representation: {str(e)}")

print("\n=== BaseException examples completed ===")