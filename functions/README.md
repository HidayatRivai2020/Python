# [Function](https://github.com/HidayatRivai2020/Python/tree/main/functions/function.py)
- block code that can be executed multiple times
- `def` to declare a function
- `parameters`: value that can be used when call a function
- `function_name(value1, value2, keyword_parameter=value3)`: calling a function
- `return`: send back the result of the function.
- `return` will stop the function executions

## Type of Parameters
- `positional arguments`:
    - arguments that provided to the functions in the order
    - `function_name(value1, value2)`: calling a function
- `keyword arguments`:
    - way to specify arguments for a function call by explicitly stating the parameter name along with its value
    - allow to pass values to specific parameters without worrying about order
    - can assign default value to the parameters
    - `function_name(keyword_arguments2=value1, keyword_arguments1=value2)`: calling a function

```
def function_name(parameter1, parameter2):
    block of code

def function_name_with_return(parameter1, parameter2):
    block of code
    return new_values

function_name(value1, value2)
new_values = function_name_with_return(value1, value2):

```
