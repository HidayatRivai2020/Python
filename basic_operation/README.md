# Operation
- specific action that is performed on one or more operands using operators
- Operator: Symbol that represent operations
- Operands: the values or variables involved in the operations

## [Arithmetic Operation](https://github.com/HidayatRivai2020/Python/tree/main/basic_operation/arithmetic_operation.py)
- Operation that can be used for number
- Operator:
    - Plus --> `+`
    - Minus --> `-`
    - Times --> `*`
    - Standard Division --> `/`
    - Integer Division --> `//`
    - Square --> `**`
    - Modulo --> `%`
    - Paranthesis --> ()
- Standard division between number will return **Float**
- Integer division between number will return
    - **the nearest whole number rounded down**
    - if both of numbers are integer, it will return **Integer**
    - if one of the numbers are float is float, it will return **Float**
- Exponentation operator (`**`) uses the right-sided binding
 
### Arithmetic Operators Type
- Binary Operators
    - Work with two operands
    - Operator: + - * / // ** %
- Unary Operators
    - Work with one operands
    - operator: + and -
    - default value: +

## [Bitwise operation](https://github.com/HidayatRivai2020/Python/tree/main/basic_operation/bitwise_operation.py)
- Manipulate data at the binary level
- Operator:
    - Ampersand
        - `&`
        - Performs AND operation
        - return 1 if both bits are 1 
    - Bar
        - `|`
        - Performs OR operation
        - return 1 if at least one bits are 1 
    - Caret
        - `^`
        - Performs Exclusive OR operation (XOR)
        - return 1 if one bits are 1 and the other is 0 
    - Tilde
        - `~`
        - logical not or logical negation
        - flipping the bits (0 becomes 1 and vice versa)
        - ~x = -x-1
    - Left shift
        - `<<`
        - shift bits to the left
        - effectively multiplying the number by powers of two
    - Right shift
        - `>>`
        - shift bits to the right
        - effectively dividing the number by powers of two
    
## [comparison operator](https://github.com/HidayatRivai2020/Python/tree/main/basic_operation/comparison_operator.py)
- compare values and return boolean
- comparison start from the left to the right
- operator
    - `==`: equals
    - `!=`: not equals
    - `<` : less than
    - `<=`: equals or less than
    - `>` : greater than
    - `>=`: equals or greater than

## [logical operator](https://github.com/HidayatRivai2020/Python/tree/main/basic_operation/logical_operator.py)
- combine conditional statement and return boolean
- operator
    - `and`: return True if both values are true
    - `or` : return True if one values are true
    ~ `not`: revert the result
 
## [Operator Precedence](https://github.com/HidayatRivai2020/Python/tree/main/basic_operation/operator_precedence.py)
- Operator precedence describes the order in which operations are performed
- Precendence order:
- `()` --> Parentheses	
- `**` --> Exponentiation	
- `+x`, `-x`, `~x` --> Unary plus, unary minus, and bitwise NOT	
- `*`, `/`, `//`, `%` --> Multiplication, division, floor division, and modulus	
- `+`, `-` --> Addition and subtraction	
- `<<`, `>>` --> Bitwise left and right shifts	
- `&` --> Bitwise AND	
- `^` --> Bitwise XOR	
- `|` --> Bitwise OR	
- `==`, `!=`, `>`, `>=`, `<`, `<=`, `is`, `is not`, `in`, `not in` --> Comparisons, identity, and membership operators	
- `not` --> Logical NOT
- `and` --> AND
- `or` --> OR