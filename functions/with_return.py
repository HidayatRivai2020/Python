print("=== With Return ===")

# Function with return value
def get_full_name(name1, name2):
    return name1 + " " + name2

# Function with conditional return
def check_number(number):
    if number < 10:
        return "pass"
    else:
        return "over"

# Function calls and using return values
full_name = get_full_name("james", "bond")
print("hello my name is {}".format(full_name))

# Testing conditional returns
number = check_number(4)
print("number 4 is {}".format(number))
number = check_number(15)
print("number 15 is {}".format(number))

# Return statement stops function execution
def test_return_stop():
    print("this is before return")
    return
    print("this is after return")  # this line will not be executed

test_return_stop()