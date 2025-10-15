Collection
- `sequence`: special data structure that can store more than one value and can be browsed
- `collection`: data types that can store multiple values in a single variable

## [List](https://github.com/HidayatRivai2020/Python/tree/main/collection/list.py)
- data structure that can hold elements in sequence
- defined by brackets
- each element spaced out by a comma
- `indexing`: access each element by using `list_name[index]`
- `slicing`: access multiple element by using `list_name[start:end]` and return it as a new list
- index start from 0
- minus index will start from the last element

### [List Method](https://github.com/HidayatRivai2020/Python/tree/main/collection/list_method.py)
- `append(value)`: add item into the end of list
    - `value`: the value that will be added into list
- `insert(index, value)`: add item into the index position in list
    - `index`: the location where item will be inserted
    - `value`: the value that will be added into list
- `pop(index)`: remove item and return the removed value
    - `index`(default=last): pop item at specific index
- `reverse()`: reverse the order of the list item
- `sort()`: sort the item list in order ascending

### [Method with list as parameter](https://github.com/HidayatRivai2020/Python/tree/main/collection/method_with_list.py)
- `del list_name`: delete the list
- `del list_name[index]`: delete element at the index
- `sorted(list_name)`: return a new list in ascending of order
    - `list_name`: the old list where the value will be ordered in a new list 