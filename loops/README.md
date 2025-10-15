# Loops
- loops type
    - for in range
    - for in
    - while
- can be used on iterable object
- indentation is crucial
- execute command as long as the the loop condition is true
- `infinite loops`: loop where the condition always true
- `incrementation`: increase the value of variable by one
- `iteration`: entering a loops block once
- `nested loops`: loops inside of a loop

## [For in range](https://github.com/HidayatRivai2020/Python/tree/main/loops/for_in_range.py)
- `for`: loops keyword
- `i`: control variable, object of each item
- `in`: keyword to introduce the range of possible values or the sequence
- `range(start, end, increase amount)`: 
    - `start`: default value is 0, start the loop from this index 
    - `end`: end the loop before this index
    - `increase_amount`: default value is one, increase the value with some amount 
- for loops can not be empty

```
for i in range(start, end):
    execute_command
```

## [For in](https://github.com/HidayatRivai2020/Python/tree/main/loops/for_in.py)
- `for`: loops keyword
- `item_name`: object of each item
- `in`: keyword to introduce the range of possible values or the sequence
- `my_iterable`: the iterable object 
- for loops can not be empty

```
for item_name in my_iterable:
    execute_command
```

## [while](https://github.com/HidayatRivai2020/Python/tree/main/loops/while.py)
- `while`: loops keyword
- `condition`: boolean to check if command should be executed
- `else`: optional keyword, loop while execute else once except break statement

```
while condition:
    execute_command
```

## [loop statement](https://github.com/HidayatRivai2020/Python/tree/main/loops/loop_statement.py)
- `pass` : statement so loop will not be empty
- `continue`: skip the loop
- `break`: stop the loop