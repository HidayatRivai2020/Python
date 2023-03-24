text = "this method call split string"
split_string = text.split()

print(split_string)
print("this is the index 0: " + split_string[0])
print("this is the index 4: " + split_string[4])

text = "hello, this text, is separated by, comma symbol"
split_string = text.split(",")

print(split_string)
print("this is the index 0: " + split_string[0])
print("this is the index 4: " + split_string[3])

text = "hello, this text is separated by i text"
split_string = text.split("i")
print(split_string)
print("this is the index 0: " + split_string[0])
print("this is the index 4: " + split_string[3])