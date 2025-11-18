# Exception
- Events that disrupt the normal flow of program execution
- Python has built-in exceptions and allows custom exceptions
- Exceptions are raised when errors occur during program execution
- Can be handled using try-except blocks

## [Built-in Exceptions](https://github.com/HidayatRivai2020/Python/tree/main/exception/builtin_exceptions.py)
- Exception that provided by python
- Built-in exceptions type:
    - `ValueError`: raised when a function receives an argument of correct type but inappropriate value
    - `TypeError`: raised when an operation is performed on inappropriate type
    - `IndexError`: raised when trying to access an index that doesn't exist in sequence
    - `KeyError`: raised when trying to access a dictionary key that doesn't exist
    - `ZeroDivisionError`: raised when attempting to divide by zero
    - `FileNotFoundError`: raised when trying to open a file that doesn't exist
    - `AttributeError`: raised when trying to access an attribute that doesn't exist
    - `ImportError`: raised when import statement fails to find or load a module
    - `SyntaxError`: raised when Python parser encounters syntactically incorrect code
    - `AssertionError`: raised when assert statement fails

## [Custom Exceptions](https://github.com/HidayatRivai2020/Python/tree/main/exception/custom_exceptions.py)
- User-defined exceptions that inherit from built-in exception classes
- Allow for more specific error handling in applications
- Created by defining a new class that inherits from Exception or its subclasses

## [Exception Handling](https://github.com/HidayatRivai2020/Python/tree/main/exception/exception_handling.py)
- Mechanism to catch and handle exceptions gracefully
- Prevents programs from crashing when errors occur
- Exception handling blocks:
    - `try`: block of code to be attempted that may lead to an exception
    - `except`: block of code that executes when an exception occurs in try block
    - `else`: block of code that executes only when no exception occurs in try block
    - `finally`: block of code that always executes regardless of whether an exception occurs
- `SyntaxError` can't be executed when raised by python automatically
- `SyntaxError` can be executed with :
    - `raise SyntaxError("message")`: manually raise SyntaxError with custom message
    - `exec("invalid syntax")`: execute string with invalid Python syntax
    - `eval("invalid expression")`: evaluate string with invalid Python expression
    - `compile("invalid code", "filename", "exec")`: compile string with syntax errors

## [Raising Exceptions](https://github.com/HidayatRivai2020/Python/tree/main/exception/raising_exceptions.py)
- Manually triggering exceptions using the raise statement
- Useful for validating input or enforcing business rules
- Can raise built-in or custom exceptions

## Exception Hierarchy
- Python exceptions are organized in a hierarchical structure
- All exceptions inherit from `BaseException` class
- Most user-defined exceptions should inherit from `Exception` class
- Exception hierarchy structure:
    ```
    BaseException
    ├── SystemExit
    ├── KeyboardInterrupt
    ├── GeneratorExit
    └── Exception
        ├── ArithmeticError
        │   ├── ZeroDivisionError
        │   ├── OverflowError
        │   └── FloatingPointError
        ├── LookupError
        │   ├── IndexError
        │   └── KeyError
        ├── OSError
        │   ├── FileNotFoundError
        │   ├── PermissionError
        │   └── ConnectionError
        ├── ValueError
        ├── TypeError
        ├── AttributeError
        ├── ImportError
        ├── SyntaxError
        ├── AssertionError
        └── RuntimeError
    ```
- Benefits of hierarchy:
    - Can catch multiple related exceptions with parent class
    - Allows for granular exception handling
    - Enables proper exception inheritance for custom exceptions
- Example: `except LookupError:` catches both `IndexError` and `KeyError`

### [Base Exception](https://github.com/HidayatRivai2020/Python/tree/main/exception/base_exception.py)
- `BaseException` is the root class for all built-in exceptions in Python
- Used internally by Python
- Template for other more spesific exception types
- Direct subclasses of `BaseException`:
    - `SystemExit`: raised by `sys.exit()` function
    - `KeyboardInterrupt`: raised when user interrupts execution (Ctrl+C)
    - `GeneratorExit`: raised when generator or coroutine is closed
    - `Exception`: base class for all non-system-exiting exceptions
- Best practices:
    - Use `except Exception:` instead of `except BaseException:`
    - Custom exceptions should inherit from `Exception`, not `BaseException`
    - Only catch `BaseException` if you need to catch system exceptions

### [System Exit](https://github.com/HidayatRivai2020/Python/tree/main/exception/system_exit.py)
- Raised by the `sys.exit()` function
- Used to request termination of Python interpreter
- Inherits directly from `BaseException`
- Characteristics:
    - Can carry an exit code (integer) or message (string)
    - Exit code 0 indicates successful termination
    - Non-zero exit codes indicate error conditions
    - If uncaught, causes the interpreter to exit
- Best practices:
    - Don't catch `SystemExit` unless you need to prevent program termination
    - Use appropriate exit codes (0 for success, 1-255 for errors)
    - Prefer `sys.exit()` over `quit()` or `exit()` in scripts
- Not caught by `except Exception:` clauses

### [Keyboard Interrupt](https://github.com/HidayatRivai2020/Python/tree/main/exception/keyboard_interrupt.py)
- `KeyboardInterrupt` is raised when user interrupts program execution
- Typically triggered by pressing Ctrl+C (or Ctrl+Break on Windows)
- Inherits directly from `BaseException`
- Purpose:
    - Allows users to gracefully stop running programs
    - Provides a way to handle user interruption requests
    - Enables cleanup operations before program termination
- Best practices:
    - Always handle `KeyboardInterrupt` in long-running programs
    - Use it for graceful cleanup and resource deallocation
    - Don't suppress `KeyboardInterrupt` unless absolutely necessary
    - Log the interruption for debugging purposes
- Signal handling:
    - On Unix systems, maps to SIGINT signal
    - Can be customized using the `signal` module
    - Default behavior is to raise `KeyboardInterrupt`
- Not caught by `except Exception:` clauses

### [Generator Exit](https://github.com/HidayatRivai2020/Python/tree/main/exception/generator_exit.py)
- `GeneratorExit` is raised when a generator or coroutine is closed
- Inherits directly from `BaseException
- Triggered by:
    - Calling `generator.close()` method
    - Generator object being garbage collected
    - Generator context manager exiting
- Purpose:
    - Allows generators to perform cleanup operations
    - Signals that generator should terminate gracefully
    - Cannot be ignored or suppressed within generator
- Important notes:
    - Must not be caught and ignored in generator functions
    - If caught, it must be re-raised
    - Not caught by `except Exception:` clauses

### [Arithmetic Error](https://github.com/HidayatRivai2020/Python/tree/main/exception/arithmetic_error.py)
- `ArithmeticError` is the base class for arithmetic-related exceptions
- Inherits from `Exception` class
- Subclasses include:
    - `ZeroDivisionError`: division or modulo by zero
    - `OverflowError`: arithmetic operation result too large
    - `FloatingPointError`: floating point operation failed
- Benefits:
    - Catch all math-related errors with single except clause
    - Useful for mathematical libraries and calculations
    - Allows specific handling of calculation failures

### [Lookup Error](https://github.com/HidayatRivai2020/Python/tree/main/exception/lookup_error.py)
- `LookupError` is the base class for lookup-related exceptions
- Inherits from `Exception` class
- Raised when key or index used on mapping or sequence is invalid
- Subclasses include:
    - `IndexError`: sequence index out of range
- Benefits:
    - Unified handling for data access errors
    - Useful for data processing and container operations
    - Simplifies exception handling for similar error types

### [OS Error](https://github.com/HidayatRivai2020/Python/tree/main/exception/os_error.py)
- `OSError` is the base class for operating system related exceptions
- Inherits from `Exception` class
- Raised when system operation causes system-related error
- Common subclasses:
    - `FileNotFoundError`: file or directory not found (errno 2)
    - `PermissionError`: insufficient permissions (errno 13)
    - `FileExistsError`: file already exists (errno 17)
    - `IsADirectoryError`: expected file but found directory (errno 21)
    - `NotADirectoryError`: expected directory but found file (errno 20)
    - `ConnectionError`: network connection issues
- Attributes:
    - `errno`: numeric error code from system
    - `strerror`: string error message from system
    - `filename`: filename related to error (if applicable)
- Benefits:
    - Comprehensive handling of system-level errors
    - Access to detailed error information
    - Cross-platform error handling

### [Value Error](https://github.com/HidayatRivai2020/Python/tree/main/exception/value_error.py)
- `ValueError` is raised when function receives argument of correct type but inappropriate value
- Inherits from `Exception` class
- Common scenarios:
    - Converting string to number with invalid format: `int("abc")`
    - Math operations with invalid domain: `math.sqrt(-1)`
    - Invalid literal for base conversion: `int("ff", 10)`
    - Empty sequences where value expected: `max([])`
- Best practices:
    - Validate input before processing
    - Provide clear error messages
    - Use for business logic validation

### [Type Error](https://github.com/HidayatRivai2020/Python/tree/main/exception/type_error.py)
- `TypeError` is raised when operation is performed on inappropriate type
- Inherits from `Exception` class
- Common scenarios:
    - Unsupported operand types: `"string" + 123`
    - Wrong number of arguments: `len()` with no arguments
    - Unhashable types as dict keys: `{[1, 2]: "value"}`
    - Incorrect function call: `"hello"()`
- Prevention:
    - Use type hints and checking
    - Validate argument types
    - Use isinstance() for type checking

### [Attribute Error](https://github.com/HidayatRivai2020/Python/tree/main/exception/attribute_error.py)
- `AttributeError` is raised when trying to access non-existent attribute
- Inherits from `Exception` class
- Common scenarios:
    - Accessing undefined attributes: `obj.nonexistent_attr`
    - Module attributes not found: `math.invalid_function`
    - Method calls on wrong types: `"string".append("x")`
    - Accessing attributes after object deletion
- Prevention:
    - Use hasattr() to check attribute existence
    - Use getattr() with default values
    - Implement __getattr__ for dynamic attributes

### [Import Error](https://github.com/HidayatRivai2020/Python/tree/main/exception/import_error.py)
- `ImportError` is raised when import statement fails to find or load module
- Inherits from `Exception` class
- Related exception: `ModuleNotFoundError` (subclass of ImportError)
- Common scenarios:
    - Module not installed: `import nonexistent_module`
    - Circular imports between modules
    - Missing dependencies or wrong Python path
    - Syntax errors in imported module
- Best practices:
    - Handle optional dependencies gracefully
    - Provide fallback implementations
    - Use try-except at module level for optional imports

### [Syntax Error](https://github.com/HidayatRivai2020/Python/tree/main/exception/syntax_error.py)
- `SyntaxError` is raised when Python parser encounters syntactically incorrect code
- Inherits from `Exception` class
- Usually occurs at compile time, not runtime
- Common scenarios:
    - Missing colons: `if condition` (missing `:`)
    - Unmatched parentheses: `print("hello"`
    - Invalid indentation: mixing tabs and spaces
    - Invalid syntax in dynamic code execution
- Prevention:
    - Use proper IDE with syntax highlighting
    - Validate dynamic code before execution
    - Use AST parsing for code analysis

### [Runtime Error](https://github.com/HidayatRivai2020/Python/tree/main/exception/runtime_error.py)
- `RuntimeError` is raised when error doesn't fall into other categories
- Inherits from `Exception` class
- Generic exception for runtime problems
- Common scenarios:
    - Maximum recursion depth exceeded
    - Improper use of certain built-in functions
    - Runtime state inconsistencies
    - Generic error conditions in libraries
- Related exceptions:
    - `RecursionError`: specific subclass for recursion limit
    - `NotImplementedError`: for unimplemented abstract methods
- Best practices:
    - Use more specific exceptions when possible
    - Implement proper base cases for recursion
    - Monitor system resources and limits

### [Assertion Error](https://github.com/HidayatRivai2020/Python/tree/main/exception/assertion_error.py)
- `AssertionError` is raised when an assert statement fails
- Inherits from `Exception` class
- Used for debugging and testing purposes
- Common scenarios:
    - Failed assert statements during development
    - Debugging conditions that should never be false
    - Testing invariants and preconditions
    - Validation of assumptions in code
- Characteristics:
    - Can be disabled with `-O` (optimize) flag
    - Should not be caught in normal program flow
    - Used primarily for debugging, not error handling
- Best practices:
    - Use for debugging and development assertions
    - Don't rely on assertions for production error handling
    - Include descriptive messages in assert statements
    - Use for documenting and validating assumptions

