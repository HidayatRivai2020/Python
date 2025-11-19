print("=== If Control ===")

# Variable initialization
password = "mypassword"
true_password = "mypassword"
other_password = "other_passwords"

# Simple if statement
if password == true_password:
    print("the password is correct")

# If-else statement
if password == other_password:
    print("the password is correct")
else:
    print("the password is not correct")

is_admin = True

# If-elif-else statement
if password == other_password:
    print("the password is correct")
elif is_admin:
    print("the password is not correct, but status is admin")
else:
    print("the password is not correct")

# Nested if statements
if password == other_password:
    print("the password is correct")
    if is_admin:
        print("status is admin")
    else:
        print("status is guest")
else:
    print("the password is not correct")

# String membership test (fixed typo)
if 'pass' in password:
    print('pass')