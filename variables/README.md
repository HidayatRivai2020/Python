# Variables
- The place where the values can be stored
- variables saved in RAM
- variables can store new values
- variables can store the value from other variables
- `variables = 'values'`
- `variables = otherVariables`
- `variables1, variables2, variables3 = values1, values2, values3`

## Naming Convention
- can contain letters (a-zA-z), digits (0-9), and underscore
- can't start with a number
- don't use special characters
- can't be reserved words
- use snake_case for variable names and PascalCase for class names
- don't use words that have special meanings or already defined

## [String](https://github.com/HidayatRivai2020/Python/tree/main/variables/string_variable.py)
- variable with the text values
- using single or double quotes
- sequence of characters
- each character are in index
- started on index 0
- `string[index]`: to get the value of character in `index`
- `string[start:size]`: to get the value of character from index `start` until before index `end`

### [String combination](https://github.com/HidayatRivai2020/Python/tree/main/variables/string_combination.py)
- `string1 + string2`: using `+` symbol between two string
- `f"insert some {string_variable} here`: the value of string_variable will be applied
- `"combine this {} and this {}".format(string1, string2)"`: each string inside format will be applied inside each curly bracket


### [String method](https://github.com/HidayatRivai2020/Python/tree/main/variables/string_variable.py)
- `capitalize()`: Uppercase first character in string
- `format(args, **kwargs)`: apply variable into curly brackets inside string
    - `args`: apply a string variable
    - `**kwargs`(optional): apply more string variable
- `upper()`: Uppercase each character in string
- `split()`: separate string into List

#### [split method](https://github.com/HidayatRivai2020/Python/tree/main/variables/string_split.py)
- `split(separator)`: separate string into List by space character
    - `separator`(optional): separate string into List by `separator`
- get the list result by index --> `List[index]`
- the separator will not be included in list result

## [Boolean](https://github.com/HidayatRivai2020/Python/tree/main/variables/boolean_variable.py)
- basic building block for logic and control flow
- true or false value

## [Integer](https://github.com/HidayatRivai2020/Python/tree/main/variables/integer_variable.py)
- Variable with integers number
- can be used in arithmatic operational

## [Float](https://github.com/HidayatRivai2020/Python/tree/main/variables/float_variable.py)
- Variable with float number
- can be used in arithmatic operational

### [round method](https://github.com/HidayatRivai2020/Python/tree/main/variables/round_method.py)
- `round(number, digits)`: returns a floating point number that is a rounded version of the specified number
    - `number`: The number to be rounded
    - `separator`(optional, default = 0): The number of decimals to use when rounding the numbers

## [variable conversion](https://github.com/HidayatRivai2020/Python/tree/main/variables/variable_conversion.py)
- `new_type(variable)`: convert the variable into new data type
    - `variable`: the variable that want to be converted
