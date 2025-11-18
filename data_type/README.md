# Data Type
- Different types of data that can be stored and manipulated in Python
- Python automatically determines data type based on the assigned value
- Each data type has specific properties and methods

## [String](https://github.com/HidayatRivai2020/Python/tree/main/data_type/string.py)
- variable with the text values
- using single or double quotes
- sequence of characters
- each character are in index
- started on index 0
- `string[index]`: to get the value of character in `index`
- `string[start:size]`: to get the value of character from index `start` until before index `end`
- `escape character`: represented by a backlash (\) to introduce special character within string that imposible to include directly

### [String combination](https://github.com/HidayatRivai2020/Python/tree/main/data_type/string_combination.py)
- `string1 + string2`: using `+` symbol between two string
- `f"insert some {string_variable} here`: the value of string_variable will be applied
- `"combine this {} and this {}".format(string1, string2)"`: each string inside format will be applied inside each curly bracket

### [String method](https://github.com/HidayatRivai2020/Python/tree/main/data_type/string_method.py)
- `capitalize()`: Uppercase first character in string
- `format(args, **kwargs)`: apply variable into curly brackets inside string
    - `args`: apply a string variable
    - `**kwargs`(optional): apply more string variable
- `islower()`: check if the string are lower-case only
- `isnumeric()`: check if the string are numeric only
- `upper()`: Uppercase each character in string
- `split()`: separate string into List

#### [split method](https://github.com/HidayatRivai2020/Python/tree/main/data_type/string_split.py)
- `split(separator)`: separate string into List by space character
    - `separator`(optional): separate string into List by `separator`
- get the list result by index --> `List[index]`
- the separator will not be included in list result

## [Boolean](https://github.com/HidayatRivai2020/Python/tree/main/data_type/boolean.py)
- basic building block for logic and control flow
- True or False value

## [Integer](https://github.com/HidayatRivai2020/Python/tree/main/data_type/integer.py)
- Variable with integers number
- can be used in arithmetic operations
- underscore (_) can be used in integer and it does not change the meaning of the numbers (python 3.6 or higher)
- scientific notation: using `e-(total_of_zero)`
- octal numbers: using `0o(number)`
- hexadecimal numbers: using `0x(number)`

## [Float](https://github.com/HidayatRivai2020/Python/tree/main/data_type/float.py)
- Variable with float number
- can be used in arithmetic operations
- separated by dots (.)

### Floating Precision
- The precision float number in python is limited
- Float numbers are not 100% correct
- Cause:
    - Eveything is represented in the binary system at the lowest level of computer
    - float numbers are stored in memory as very long chains of zeros and ones
    - most float cannot be represented exactly as binary fractions
    - as a consequence, the floats are approximated and rounded when they are stored as binary numbers
- This is not bug in python or code, but this is how computer works nowadays

### [round method](https://github.com/HidayatRivai2020/Python/tree/main/data_type/round_method.py)
- `round(number, digits)`: returns a floating point number that is a rounded version of the specified number
    - `number`: The number to be rounded
    - `digits`(optional, default = 0): The number of decimals to use when rounding the numbers

## [None](https://github.com/HidayatRivai2020/Python/tree/main/data_type/none.py)
- special data type
- represent the absence of value or a null value

## [Generator](https://github.com/HidayatRivai2020/Python/tree/main/data_type/generator.py)
- special type of iterator that generates values on-the-fly
- memory efficient for large datasets
- created using generator functions with `yield` keyword
- can be created using generator expressions
- values are computed lazily (only when needed)