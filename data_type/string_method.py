print("=== String Method ===")

# upper() method converts all characters to uppercase
uppercase_string = "this string call method upper"
print(uppercase_string.upper())

# capitalize() method capitalizes the first character of the string
capitalize_string = "this string call method capitalize"
print(capitalize_string.capitalize())

# lower() method converts all characters to lowercase
lowercase_string = "THIS STRING CALL METHOD lower"
print(lowercase_string.lower())

# split() method splits the string into a list of words
split_string = "this string call method split"
print(split_string.split())

# isnumeric() method returns True if all characters are numeric
numeric_string = "12345"
print(numeric_string.isnumeric())

# Example with mixed characters (letters and numbers)
non_numeric_string = "hello123"
print(non_numeric_string.isnumeric())

# islower() method returns True if all characters are lowercase
lowercase_check_string = "hello world"
print(lowercase_check_string.islower())

# Example with mixed case (uppercase and lowercase)
mixed_case_string = "Hello World"
print(mixed_case_string.islower())

