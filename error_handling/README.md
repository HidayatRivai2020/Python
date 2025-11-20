# [Error Handling](https://github.com/HidayatRivai2020/Python/tree/main/error_handling/error_handling.py)
- to make sure the program can still operate even if an error were to occur
- to create the proper error message
- `try`: Block of code to be attempted (may lead to an error)
- `except`: Block of code that will be executed in case there is an error in `try` block
- `finally`: Final block of code that will be executed
- `try` can have multiple except and the order matter

```
try:
    # attempted code
except:
    # executed code when error
except:
    # executed code when error
finally:
    # executed code regardless of an error
```

## [raise](https://github.com/HidayatRivai2020/Python/tree/main/error_handling/raise_statement.py)
- Statement used to manually trigger (raise) an exception in Python
- Allows control over when and what type of exceptions are raised
- Essential for input validation and enforcing business rules
- `raise ExceptionType("message")`: raise specific exception with message
- `raise ExceptionType()`: raise exception without message
- `raise`: re-raise current exception (only in except blocks)

```
raise ValueError("Custom error message")
raise  # re-raise the same exception
```

## [assert](https://github.com/HidayatRivai2020/Python/tree/main/error_handling/assert_statement.py)
- Statement used for debugging and testing purposes
- Checks if a condition is True, raises AssertionError if False
- Can be disabled with Python optimization flag (`python -O`)
- Should NOT be used for production error handling
- `assert condition`: basic assertion
- `assert condition, "message"`: assertion with custom error message

```
assert b != 0, "Cannot divide by zero"

```