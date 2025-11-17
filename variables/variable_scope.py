# global variable
x = "global x"
def outer_function():
    print(x)  # prints "global x"
outer_function()


# local variable
def inner_function(): 
    y = "local y"
    print(y)  # prints "local y"
inner_function()

# variable shadowing
z = "global z"
def shadow_function():
    z = "local z"
    print(z)  # prints "local z"
shadow_function()
print(z)  # prints "global z"

# modifying global variable
a = "global a"
def modify_global():
    global a
    a = "modified global a"
modify_global()
print(a)  # prints "modified global a"

# shadowing with method call
b = ["hello world"]
def shadow_with_method():
    b.append("test")  # shadows global b with local b
    print(b)  # prints "HELLO WORLD"
shadow_with_method()
print(b)  # prints "hello world"