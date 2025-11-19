print("=== SystemExit Examples ===")

import sys

# 1. Basic SystemExit usage
print("1. Basic sys.exit() usage:")
try:
    print("About to exit with code 0")
    sys.exit(0)  # Success exit
except SystemExit as e:
    print(f"SystemExit caught: {e}")
    print(f"Exit code: {e.code}")

# 2. Exit with error code
print("\n2. Exit with error code:")
try:
    print("About to exit with error code")
    sys.exit(1)  # Error exit
except SystemExit as e:
    print(f"SystemExit caught: {e}")
    print(f"Exit code: {e.code}")

# 3. Exit with message
print("\n3. Exit with custom message:")
try:
    sys.exit("Something went wrong!")
except SystemExit as e:
    print(f"SystemExit caught: {e}")
    print(f"Exit code: {e.code}")
    print(f"Message: {e}")

# 4. Conditional exit
print("\n4. Conditional exit based on validation:")
def validate_age(age):
    try:
        age_int = int(age)
        if age_int < 0:
            sys.exit("Error: Age cannot be negative")
        elif age_int > 150:
            sys.exit("Error: Age seems unrealistic")
        else:
            return age_int
    except ValueError:
        sys.exit("Error: Age must be a number")
    except SystemExit as e:
        print(f"Validation failed: {e}")
        return None

# Test validation
result = validate_age("25")
print(f"Valid age: {result}")

result = validate_age("-5")
print(f"Result for invalid age: {result}")

# 5. SystemExit in functions
print("\n5. SystemExit propagation in functions:")
def risky_function():
    try:
        sys.exit("Function wants to exit")
    except SystemExit as e:
        print(f"Function caught SystemExit: {e}")
        # Re-raise to allow program termination if needed
        # raise  # Uncomment this to allow exit to propagate

try:
    risky_function()
except SystemExit as e:
    print(f"Main caught SystemExit: {e}")

# 6. Exit codes convention
print("\n6. Exit codes convention:")
EXIT_SUCCESS = 0
EXIT_FAILURE = 1
EXIT_INVALID_ARGUMENT = 2

def exit_with_code(condition):
    try:
        if condition == "success":
            sys.exit(EXIT_SUCCESS)
        elif condition == "failure":
            sys.exit(EXIT_FAILURE)
        elif condition == "invalid":
            sys.exit(EXIT_INVALID_ARGUMENT)
    except SystemExit as e:
        print(f"Exit code {e.code}: {['Success', 'General failure', 'Invalid argument'][e.code]}")

exit_with_code("success")
exit_with_code("failure")
exit_with_code("invalid")

# 7. Cleanup before exit
print("\n7. Cleanup operations before exit:")
import atexit

def cleanup():
    print("Performing cleanup operations...")

# Register cleanup function
atexit.register(cleanup)

try:
    print("About to exit with cleanup")
    sys.exit("Exiting gracefully")
except SystemExit as e:
    print(f"SystemExit caught: {e}")
    # In real scenarios, cleanup would be automatically called

print("\n=== SystemExit examples completed ===")