# OOP
- Object Oriented Programming
- everything are object in python


```
class ClassName(ParentClass):

    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2
    
    def method_name(self, x):
        # do some action

my_object = ClassName(param1, param2)
my_object.param1
my_object.method_name(x)
```

## [Constructor](https://github.com/HidayatRivai2020/Python/tree/main/oop/constructor.py)
- `constructor`: method that will be called when object created
- `init`: the keyword for constructor
- `self`: keyword to access the value of the object itself

## [Class](https://github.com/HidayatRivai2020/Python/tree/main/oop/class_type.py)
- `type(variable)`: method to check the class type of variable
- `class`: has method and attribute
- `object`: created from `class`

## [Attribute](https://github.com/HidayatRivai2020/Python/tree/main/oop/attribute.py)
- `attribute`: property inside the class

## [Method](https://github.com/HidayatRivai2020/Python/tree/main/oop/method.py)
- `method`: function inside the class

## [Inheritance](https://github.com/HidayatRivai2020/Python/tree/main/oop/inheritance.py)
- `inheritance`: inherit method and attribute from parent class
- `override`: overwrite some method from parent class in child class
- `def ChildClass(ParentClass)`: how to inheritance from parent class into child class

## Special Methods
- Sometimes called dunder method
- python has built in predefined function
- object can interact with built in function
- `__method__` to set the command when built in called for self defined object

### [Dunder Method](https://github.com/HidayatRivai2020/Python/tree/main/oop/dunder_method.py)
- `__init__`: constructor
- `__str__`: execute command when `print()` called
- `__len__`: execute command when `len()` called