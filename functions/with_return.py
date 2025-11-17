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
full_name = get_full_name("james", "bond")
print("hello my name is {}".format(full_name))

# check number
number = check_number(4)
print("number 4 is {}".format(number))
number = check_number(15)
print("number 15 is {}".format(number))

# return will stop the function executions
def test_return_stop():
    print("this is before return")
    return
    print("this is after return")  # this line will not be executed

test_return_stop()