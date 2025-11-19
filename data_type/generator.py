print("=== Generator ===")

# Generator examples in Python

# Generator function with yield keyword
def number_generator():
    print("Starting generator")
    yield 1
    print("Continuing generator")
    yield 2
    print("Finishing generator")
    yield 3

# Create generator object
gen = number_generator()
print("Generator created")

# Get values one by one
print("Getting first value:", next(gen))
print("Getting second value:", next(gen))
print("Getting third value:", next(gen))

print("\n" + "="*50 + "\n")

# Generator function that generates a range of numbers
def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1

# Using the generator in a loop
print("Using generator in for loop:")
for num in my_range(1, 5):
    print(f"Generated number: {num}")

print("\n" + "="*50 + "\n")

# Generator expression (similar to list comprehension but with parentheses)
print("Generator expression:")
squares_gen = (x**2 for x in range(5))
print("Generator object:", squares_gen)

print("Generated squares:")
for square in squares_gen:
    print(f"Square: {square}")

print("\n" + "="*50 + "\n")

# Generator for Fibonacci sequence
def fibonacci_generator(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

print("Fibonacci sequence using generator:")
fib_gen = fibonacci_generator(8)
for fib_num in fib_gen:
    print(f"Fibonacci: {fib_num}")

print("\n" + "="*50 + "\n")

# Memory efficiency demonstration
print("Memory efficiency example:")
# Generator expression (memory efficient)
large_gen = (x for x in range(1000000))
print(f"Generator object size is minimal: {type(large_gen)}")

# List comprehension would use much more memory
# large_list = [x for x in range(1000000)]  # This would use a lot of memory

print("Generator allows processing large datasets with minimal memory usage")