password = "mypassword"
true_password = "mypassword"
other_password = "other_passwords"

if password == true_password:
    print("the password is correct")

if password == other_password:
    print("the password is correct")
else:
    print("the password is not correct")

is_admin = True

if password == other_password:
    print("the password is correct")
elif is_admin:
    print("the password is not correct, but status is admin")
else:
    print("the password is not correct")