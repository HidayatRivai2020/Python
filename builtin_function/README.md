# Built-in Function
- Functions that are always available in Python without importing any modules
- Part of Python's core language and can be used directly
- Provide essential functionality for common programming tasks
- Total of 69 built-in functions in Python 3.x
- No need to define or import - ready to use immediately

## [float](https://github.com/HidayatRivai2020/Python/tree/main/builtin_function/float_function.py)
- Convert a value to a floating-point number (decimal number)
- Essential for mathematical calculations requiring precision
- Format: `float(x)`
  - `x`: value to convert (string, number, or bytes-like object)
- Returns a float object
- Raises ValueError if conversion is not possible
- Supports special values: 'inf', '-inf', 'nan'
- Preserves decimal precision: `float("3.14159")` → 3.14159
- Converts integers without loss: `float(42)` → 42.0
- Handles scientific notation: `float("1e6")` → 1000000.0
- Whitespace is automatically stripped: `float(" 3.14 ")` → 3.14
- Empty strings raise ValueError: `float("")` is invalid
- Floating-point arithmetic may have precision limitations

## [input](https://github.com/HidayatRivai2020/Python/tree/main/builtin_function/input.py)
- `input(prompt)`: function that allows user input
    - `prompt`: default message before the input
- always return a string value

## [int](https://github.com/HidayatRivai2020/Python/tree/main/builtin_function/int_function.py)
- Convert a value to an integer (whole number)
- One of the most commonly used type conversion functions
- Can convert from strings, floats, and other numeric types
- Format: `int(x, base=10)`
  - `x`: value to convert (string, number, or bytes-like object)
  - `base` (optional): number base for string conversion (default is 10)
- Returns an integer object
- Raises ValueError if conversion is not possible
- Truncates decimal part when converting from float (doesn't round)
- Truncates toward zero: `int(3.7)` → 3, `int(-3.7)` → -3
- Cannot convert strings with decimal points directly: `int("3.7")` raises ValueError
- Empty strings raise ValueError: `int("")` is invalid
- Whitespace is automatically stripped: `int(" 42 ")` → 42

## [len](https://github.com/HidayatRivai2020/Python/tree/main/builtin_function/len_function.py)
- Return the length (the number of items) of an object.
- The argument may be a sequence (such as a string, bytes, tuple, list, or range) or a collection (such as a dictionary, set, or frozen set).
- Raises OverflowError on lengths larger than sys.maxsize
- format: `len(object)`
  - `object`: sequence or collection

## [print](https://github.com/HidayatRivai2020/Python/tree/main/builtin_function/print_function.py)
- Print objects to the text stream file
- Format : `print(*objects, sep=' ', end='\n', file=None, flush=False)`
  - `*objects` : parameters that will be printed in the text stream file
  - `sep` : Specify how to separate the objects, if there is more than one
  - `end` : Specify what to print at the end
  - `file` : An object with a write method
  - `flush` : Specifying if the output is flushed (True) or buffered (False)


/**
abs()
aiter()
all()
anext()
any()
ascii()

B
bin()
bool()
breakpoint()
bytearray()
bytes()

C
callable()
chr()
classmethod()
compile()
complex()

D
delattr()
dict()
dir()
divmod()

E
enumerate()
eval()
exec()

F
filter()
float()
format()
frozenset()

G
getattr()
globals()

H
hasattr()
hash()
help()
hex()

I
id()
isinstance()
issubclass()
iter()
L
len()
list()
locals()

M
map()
max()
memoryview()
min()

N
next()

O
object()
oct()
open()
ord()

P
pow()

property()




R
range()
repr()
reversed()
round()

S
set()
setattr()
slice()
sorted()
staticmethod()
str()
sum()
super()

T
tuple()
type()

V
vars()

Z
zip()

_
__import__()

**/
