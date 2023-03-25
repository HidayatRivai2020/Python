# list
my_list = [100, 200, 250, 350, 400]
print(f"my_list: {my_list}")

# append
my_list.append(700)
print(f"append 700 to my_list: {my_list}")

# insert
my_list.insert(2,320)
print(f"insert 320 to my_list in index 2: {my_list}")

# pop
removed_value =my_list.pop()
print("remove the last item from my_list")
print(f"removed_value: {removed_value}")
print(f"my_list: {my_list}")

removed_value =my_list.pop(2)
print("remove item on index from my_list")
print(f"removed_value: {removed_value}")
print(f"my_list: {my_list}")

# reverse
my_list.reverse()
print(f"reversed my_list: {my_list}")

# sort
number_list = [1, 2, 5, 1, 6, 6 ,2 ,3, 4, 8,  4, 9]
print(f"number_list: {number_list}")
number_list.sort()
print(f"number_list in ascending order: {number_list}")
number_list.sort(reverse=True)
print(f"number_list in descending order: {number_list}")

string_list = ["this", "is", "a", "new", "string", "list"]
print(f"string_list: {string_list}")
string_list.sort()
print(f"string_list in ascending order: {string_list}")
string_list.sort(reverse=True)
print(f"string_list in descending order: {string_list}")


