print("=== int() Function Examples ===")

# 1. BASIC TYPE CONVERSION
print("\n1. BASIC TYPE CONVERSION")
print("-" * 40)

# Converting from float to int (truncation, not rounding)
float_numbers = [3.14, 3.7, 3.9, -2.1, -2.9]
print("Float to int conversion (truncation):")
for num in float_numbers:
    result = int(num)
    print(f"int({num}) = {result}")

# Converting from string to int
string_numbers = ["42", "123", "-456", "0"]
print("\nString to int conversion:")
for num_str in string_numbers:
    result = int(num_str)
    print(f'int("{num_str}") = {result}')

# Converting with whitespace (automatically stripped)
whitespace_strings = [" 42 ", "\t123\t", "\n456\n"]
print("\nString with whitespace:")
for num_str in whitespace_strings:
    result = int(num_str)
    print(f'int("{repr(num_str)}") = {result}')

print("\n" + "=" * 50 + "\n")

# 2. BASE CONVERSION
print("2. BASE CONVERSION")
print("-" * 40)

# Binary (base 2) to decimal
binary_numbers = ["1010", "1111", "101010", "11111111"]
print("Binary to decimal:")
for binary in binary_numbers:
    decimal = int(binary, 2)
    print(f'int("{binary}", 2) = {decimal}')

# Octal (base 8) to decimal
octal_numbers = ["77", "123", "755", "1000"]
print("\nOctal to decimal:")
for octal in octal_numbers:
    decimal = int(octal, 8)
    print(f'int("{octal}", 8) = {decimal}')

# Hexadecimal (base 16) to decimal
hex_numbers = ["FF", "A0", "1F4", "DEAD", "BEEF"]
print("\nHexadecimal to decimal:")
for hex_num in hex_numbers:
    decimal = int(hex_num, 16)
    print(f'int("{hex_num}", 16) = {decimal}')

# Custom bases
print("\nCustom bases:")
print(f'int("123", 5) = {int("123", 5)}')  # Base 5
print(f'int("ZZ", 36) = {int("ZZ", 36)}')   # Base 36 (0-9, A-Z)

print("\n" + "=" * 50 + "\n")
