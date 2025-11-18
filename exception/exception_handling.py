# Exception Handling Examples

print("=== Exception Handling Examples ===\n")

# 1. Basic try-except
print("1. Basic try-except:")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# 2. Catching specific exceptions
print("2. Multiple specific exceptions:")
def process_data(data):
    try:
        # Convert to integer
        number = int(data)
        # Divide by a random divisor
        result = 100 / number
        # Access list element
        my_list = [1, 2, 3]
        value = my_list[number]
        return result, value
    except ValueError:
        print("Invalid data: cannot convert to integer")
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except IndexError:
        print("Index out of range")

process_data("hello")  # ValueError
process_data("0")      # ZeroDivisionError
process_data("5")      # IndexError

# 3. Catching multiple exceptions in one except block
print("3. Multiple exceptions in one block:")
try:
    data = input("Enter a number (or press Enter for empty): ") or "abc"
    number = int(data)
    result = 10 / number
    print(f"Result: {result}")
except (ValueError, ZeroDivisionError) as e:
    print(f"Error occurred: {type(e).__name__} - {e}")

# 4. try-except-else
print("4. try-except-else:")
try:
    number = int("42")  # This will succeed
except ValueError:
    print("Invalid number")
else:
    print(f"Successfully converted number: {number}")

# 5. try-except-finally
print("5. try-except-finally:")
try:
    file = open("example.txt", "w")
    file.write("Hello World")
    # Simulate an error
    result = 1 / 0
except ZeroDivisionError:
    print("Error occurred while processing file")
finally:
    try:
        file.close()
        print("File closed in finally block")
    except:
        print("File was not opened")

# 6. try-except-else-finally (complete structure)
print("6. Complete try-except-else-finally:")
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None
    except TypeError:
        print("Invalid data types for division")
        return None
    else:
        print(f"Division successful: {a} / {b} = {result}")
        return result
    finally:
        print("Division operation completed")

safe_divide(10, 2)   # Success case
safe_divide(10, 0)   # Error case

# 7. Nested exception handling
print("7. Nested exception handling:")
try:
    try:
        numbers = [1, 2, 3]
        index = int(input("Enter an index (or press Enter for '5'): ") or "5")
        value = numbers[index]
        print(f"Value at index {index}: {value}")
    except ValueError:
        print("Inner exception: Invalid index format")
        raise  # Re-raise the exception
    except IndexError:
        print("Inner exception: Index out of range")
except ValueError:
    print("Outer exception: Handling re-raised ValueError")

# 8. Exception information
print("8. Getting exception information:")
import sys

try:
    1 / 0
except Exception as e:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print(f"Exception type: {exc_type.__name__}")
    print(f"Exception value: {exc_value}")
    print(f"Exception occurred in: {exc_traceback.tb_frame.f_code.co_filename}")

# 9. SyntaxError handling
print("9. SyntaxError handling:")
try:
    # Using exec() with invalid syntax
    code_string = "print('Hello World'"  # Missing closing parenthesis
    exec(code_string)
except SyntaxError as e:
    print(f"Syntax error detected: {e}")
    print(f"Error at line {e.lineno}, position {e.offset}")

try:
    # Using eval() with invalid expression
    expression = "2 + * 3"  # Invalid syntax
    result = eval(expression)
except SyntaxError as e:
    print(f"Invalid expression syntax: {e}")

try:
    # Using compile() to check syntax
    code = "if True\n    print('Missing colon')"  # Missing colon
    compile(code, '<string>', 'exec')
except SyntaxError as e:
    print(f"Compilation error: {e}")
    print(f"Problem text: {e.text}")

print("\n=== All exception handling examples completed ===")