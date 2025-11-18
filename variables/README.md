# Variables
- The place where the values can be stored for future use
- variables saved in RAM
- variables can store new values
- variables can store the value from other variables
- `variables = 'values'`
- `variables = otherVariables`
- `variables1, variables2, variables3 = values1, values2, values3`
- swapping variables --> `var, var2 = var2, var1`
- data-type automatically based on the last value

## Naming Convention
- can contain letters (a-zA-z), digits (0-9), and underscore
- can't start with a number
- don't use special characters
- can't be reserved words
- use snake_case for variable names and PascalCase for class names
- don't use words that have special meanings or already defined

## [Swap Variable](https://github.com/HidayatRivai2020/Python/tree/main/variables/swap_variable.py)
- technique to exchange the values of two variables
- `var1, var2 = var2, var1`: swapping using multiple assignment

## [Variable Conversion](https://github.com/HidayatRivai2020/Python/tree/main/variables/variable_conversion.py)
- Often called as Type-Casting
- `new_type(variable)`: convert the variable into new data type
    - `variable`: the variable that want to be converted

## [Variable Scope](https://github.com/HidayatRivai2020/Python/tree/main/variables/variable_scope.py)
- local : variable that is defined within a scope and can be recognized only in that scope
- global : variable that can be used through entire script after declared
- shadowing : global variable that has same name with local variable
- use keyword `global` to make the local variable can affect the global variable
- shadowing only affected on assigned value
- using method will affect the global variable too
