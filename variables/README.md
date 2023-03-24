# Variables
- The place where the values can be stored
- `variables = 'values'`

## String
- variable with the text values
- using single or double quotes
- sequence of characters
- each character are in index
- started on index 0
- `string[index]`: to get the value of character in `index`
- `string[start:size]`: to get the value of character from index `start` until before index `end`

### String combination
- `string1 + string2`: using `+` symbol between two string
- `f"insert some {string_variable} here`: the value of string_variable will be applied
- `"combine this {} and this {}".format(string1, string2)"`: each string inside format will be applied inside each curly bracket


### String method
- `capitalize()`: Uppercase first character in string
- `format(args)`: apply args into curly brackets inside string
- `upper()`: Uppercase each character in string
- `split()`: separate string into List

#### split method
- `split()`: separate string into List by space character
- `split(separator)`: separate string into List by `separator`
- get the list result by index --> `List[index]`
- the separator will not be included in list result