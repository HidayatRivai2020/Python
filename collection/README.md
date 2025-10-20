Collection
- `sequence`: special data structure that can store more than one value and can be browsed
- `collection`: data types that can store multiple values in a single variable'
- `nested collection`: collection as data-type inside of collection

## [List](https://github.com/HidayatRivai2020/Python/tree/main/collection/list.py)
- data structure that can hold elements in sequence
- defined by brackets
- each element spaced out by a comma
- `indexing`: access each element by using `list_name[index]`
- `slicing`: access multiple element by using `list_name[start:end]` and return it as a new list
- index start from 0
- minus index will start from the last element
- `list comprehension`: `var1 = [one line loop or if]`
- `adding list`: use `+` to combine two values of list together
- `multiplying list`: use `*` to repeat the value of list multiple times

### [List Method](https://github.com/HidayatRivai2020/Python/tree/main/collection/list_method.py)
- function in list object
- affected the original list
- `append(value)`: add item into the end of list
    - `value`: the value that will be added into list
- `insert(index, value)`: add item into the index position in list
    - `index`: the location where item will be inserted
    - `value`: the value that will be added into list
- `pop(index)`: remove item and return the removed value
    - `index`(default=last): pop item at specific index
- `reverse()`: reverse the order of the list item
- `sort(reverse=True)`: sort the item list in order ascending
    - ``reverse`: sort item descending

### [Method with list as parameter](https://github.com/HidayatRivai2020/Python/tree/main/collection/method_with_list.py)
- method with list as it parameters
- gives back a new list and keep the original unchanged
- `del list_name`: delete the list
- `del list_name[index]`: delete element at the index
- `sorted(list_name)`: return a new list in ascending of order
    - `list_name`: the old list where the value will be ordered in a new list 

## [Copying Collection](https://github.com/HidayatRivai2020/Python/tree/main/collection/copying_collection.py)
- `references`: assigning a collection into new variable will copy the memory location where the collection is stored
- changing the old list will change the new list value as well
- `coll_new = coll_original[:]`: use slicing to make an independent collection
