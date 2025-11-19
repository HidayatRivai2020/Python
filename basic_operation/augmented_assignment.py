print("=== Arithmetic Augmented Assignment Operators ===")

# Addition assignment (+=)
x = 10
print(f"Initial value: x = {x}")
x += 5
print(f"After x += 5: x = {x}")

# Subtraction assignment (-=)
x -= 3
print(f"After x -= 3: x = {x}")

# Multiplication assignment (*=)
x *= 2
print(f"After x *= 2: x = {x}")

# Division assignment (/=)
x /= 4
print(f"After x /= 4: x = {x}")

# Floor division assignment (//=)
x //= 2
print(f"After x //= 2: x = {x}")

# Exponentiation assignment (**=)
x **= 3
print(f"After x **= 3: x = {x}")

# Modulo assignment (%=)
x %= 5
print(f"After x %= 5: x = {x}")

print("\n=== String Augmented Assignment ===")

# String concatenation with +=
text = "Hello"
print(f"Initial text: '{text}'")
text += " World"
print(f"After text += ' World': '{text}'")

text += "!"
print(f"After text += '!': '{text}'")

print("\n=== List Augmented Assignment ===")

# List extension with +=
numbers = [1, 2, 3]
print(f"Initial list: {numbers}")
numbers += [4, 5]
print(f"After numbers += [4, 5]: {numbers}")

# Multiplication with lists
letters = ['a', 'b']
print(f"Initial letters: {letters}")
letters *= 3
print(f"After letters *= 3: {letters}")

print("\n=== Bitwise Augmented Assignment Operators ===")

# Bitwise AND assignment (&=)
a = 12  # Binary: 1100
b = 10  # Binary: 1010
print(f"a = {a} (binary: {bin(a)})")
print(f"b = {b} (binary: {bin(b)})")

a &= b
print(f"After a &= b: a = {a} (binary: {bin(a)})")

# Bitwise OR assignment (|=)
a = 12  # Binary: 1100
a |= 3  # Binary: 0011
print(f"After a |= 3: a = {a} (binary: {bin(a)})")

# Bitwise XOR assignment (^=)
a ^= 7  # Binary: 0111
print(f"After a ^= 7: a = {a} (binary: {bin(a)})")

# Left shift assignment (<<=)
a = 5  # Binary: 101
print(f"a = {a} (binary: {bin(a)})")
a <<= 2
print(f"After a <<= 2: a = {a} (binary: {bin(a)})")

# Right shift assignment (>>=)
a >>= 1
print(f"After a >>= 1: a = {a} (binary: {bin(a)})")
