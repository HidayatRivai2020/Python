print("=== Function ===")

# Function without parameter
def say_hello():
    print("hello")

# Function with parameter
def say_name(name):
    print("hello " + name)

# Function with return value
def get_full_name(name1, name2):
    return name1 + " " + name2

# Function with conditional logic
def check_number(number):
    if number < 10:
        return "pass"
    else:
        return "over"

# Function with default parameter
def give_item(name, item=0):
    print("hello " + name + ", I give you " + str(item) + " items")

# Function calls
say_hello()
say_name("james")
full_name = get_full_name("james", "bond")
print("hello my name is {}".format(full_name))

number = check_number(4)
print("number 4 is {}".format(number))
number = check_number(15)
print("number 15 is {}".format(number))

give_item("jack")
give_item("john", 10)
