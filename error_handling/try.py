# execute try block
try:
    print("this code will be executed")
except:
    print("error")
finally:
    print("done")


# execute except block
try:
    print("this code will not be executed" + 10)
except:
    print("error! can not add string and integer")
finally:
    print("done")