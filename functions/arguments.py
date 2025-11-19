print("=== Arguments ===")

# Function with parameter
def say_name(name):
    print("hello " + name)

# Function with keyword parameter (default value)
def give_item(name, item=0):
    print("hello " + name + ", I give you " + str(item) + " items")

# Function calls
say_name("james")

# Function calls with different parameters
give_item("jack")
give_item("john", 10)

