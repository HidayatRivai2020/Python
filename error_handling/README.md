# Error Handling
- to make sure the program can still operate even if an error were to occur
- to create the proper error message
- `try`: Block of code to be attempted (may leat to an error)
- `except`: Block of code that will be executed in case there is an error in `try` block
- `finally`: Final block of code that will be executed

```
try:
    # attempted code
except:
    # executed code when error
finally:
    # executed code regardless of an error