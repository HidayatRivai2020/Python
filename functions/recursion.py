print("=== Recursion ===")

# Recursive function example - factorial
def factorial(n):
    # base case
    if n <= 1:
        return 1
    else:
        # recursive case
        return n * factorial(n - 1)

# Test the factorial function with different values
number = 5
result = factorial(number)
print("Factorial of {} is {}".format(number, result))

number = 0
result = factorial(number)
print("Factorial of {} is {}".format(number, result))

number = 1
result = factorial(number)
print("Factorial of {} is {}".format(number, result))
