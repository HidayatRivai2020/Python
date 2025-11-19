print("=== Copying Collection ===")

# Reference copy (shallow - changes affect both lists)
list_original = [1, 2, 3]
list_new = list_original
list_original[0] = -5
print('original:', list_original, '\nnew:', list_new)

# Deep copy using slice notation
another_list_original = [1, 2, 3]
another_list_new = another_list_original[:]
another_list_original[0] = -5
print('original:', another_list_original, '\nnew:', another_list_new)