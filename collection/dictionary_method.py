my_dict = {"key": "a", "another-key": "another", "random-key": "random-value"}

print("key-values in tuple format: {}".format(my_dict.items()))
print("only keys: {}".format(my_dict.keys()))
print("only values: {}".format(my_dict.values()))

# updating values
my_dict.update({"key": "updated-value", "another-key": "new-value"})
print("after update: {}".format(my_dict))