# with parameter
def say_name(name):
    print("hello " + name)

# with keyword parameter
def give_item(name, item=0):
    print("hello " + name + ", I give you " + str(item) + " items")

# call say_name function
say_name("james")

# call give_item function
give_item("jack")
give_item("john", 10)

