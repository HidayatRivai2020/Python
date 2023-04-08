# without parameter
def say_hello():
    print("hello")

# with parameter
def say_name(name):
    print("hello " + name)

# with return
def get_full_name(name1, name2):
    return name1 + " " + name2

# block of code
def check_number(number):
    if number < 10:
        return "pass"
    else:
        return "over"

# call the function
say_hello()
say_name("james")
full_name = get_full_name("james", "bond")
print("hello my name is {}".format(full_name))

number = check_number(4)
print("number 4 is {}".format(number))
number = check_number(15)
print("number 15 is {}".format(number))