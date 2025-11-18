# [Function](https://github.com/HidayatRivai2020/Python/tree/main/functions/function.py)
- part of code used to cause an effect or evaluate a value
- block code that can be executed multiple times
- `def` to declare a function
- `parameters`: value that can be used when call a function
- `arguments`: value that assigned to parameters when function called
- `function_name(value1, value2, keyword_parameter=value3)`: calling a function
- call `function(arguments)` to execute the command inside function

## Function Execution
1. checks function name
2. checks arguments passed
3. jumps into the function
4. executes the function
5. returns to the code
6. resume executions

## Function Part

### [Arguments](https://github.com/HidayatRivai2020/Python/tree/main/functions/arguments.py)
- `positional arguments`:
    - arguments that provided to the functions in the order
    - `function_name(value1, value2)`: calling a function
- `keyword arguments`:
    - way to specify arguments for a function call by explicitly stating the parameter name along with its value
    - allow to pass values to specific parameters without worrying about order
    - can assign default value to the parameters
    - `function_name(keyword_arguments2=value1, keyword_arguments1=value2)`: calling a function
- All positional arguments must appear before any named arguments

```
def function_name(parameter1, parameter2):
    block of code

function_name(value1, value2)

```

### [Return](https://github.com/HidayatRivai2020/Python/tree/main/functions/with_return.py)
- `return` will stop the function executions
- `return new_value`: send back the result of the function.
- function without `return` will return `none`

```
def function_name_with_return(parameter1, parameter2):
    block of code
    return

def function_name_with_return_new_values(parameter1, parameter2):
    block of code
    return new_values

function_name(value1, value2)
new_values = function_name_with_return_values(value1, value2):
```

## [Recursion](https://github.com/HidayatRivai2020/Python/tree/main/functions/recursion.py)
- function that call itself
- need condition to stop the recursive part
