print("=== float( Function Examples ===")

# 1. BASIC TYPE CONVERSION
print("\n1. BASIC TYPE CONVERSION")
print("-" * 40)

# Converting from integer to float
integers = [42, 0, -17, 1000]
print("Integer to float conversion:")
for num in integers:
    result = float(num)
    print(f"float({num}) = {result} (type: {type(result).__name__})")

# Converting from string to float
string_numbers = ["3.14", "2.718", "-9.81", "0.001", "123.456"]
print("\nString to float conversion:")
for num_str in string_numbers:
    result = float(num_str)
    print(f'float("{num_str}") = {result}')

# Converting with whitespace (automatically stripped)
whitespace_strings = [" 3.14 ", "\t2.718\t", "\n-9.81\n"]
print("\nString with whitespace:")
for num_str in whitespace_strings:
    result = float(num_str)
    print(f'float("{repr(num_str)}") = {result}')

print("\n" + "=" * 50 + "\n")

# 2. SCIENTIFIC NOTATION
print("2. SCIENTIFIC NOTATION")
print("-" * 40)

# Scientific notation strings
scientific_numbers = ["1e6", "2.5e-3", "6.022e23", "1.602e-19", "-3.14e2"]
print("Scientific notation conversion:")
for sci_str in scientific_numbers:
    result = float(sci_str)
    print(f'float("{sci_str}") = {result}')

# Large and small numbers
print("\nLarge and small number examples:")
examples = [
    ("1e100", "Googol (very large)"),
    ("1e-100", "Very small number"),
    ("6.022e23", "Avogadro's number"),
    ("9.109e-31", "Electron mass (kg)")
]

for num_str, description in examples:
    result = float(num_str)
    print(f'{description}: float("{num_str}") = {result}')

print("\n" + "=" * 50 + "\n")

# 3. SPECIAL VALUES
print("3. SPECIAL VALUES")
print("-" * 40)

# Infinity and NaN
special_values = ["inf", "-inf", "nan", "INF", "NaN", "infinity", "-infinity"]
print("Special float values:")
for special in special_values:
    try:
        result = float(special)
        print(f'float("{special}") = {result}')
    except ValueError as e:
        print(f'float("{special}") → Error: {e}')

# Testing special values
import math
inf_pos = float("inf")
inf_neg = float("-inf")
nan_val = float("nan")

print(f"\nTesting special values:")
print(f"Positive infinity: {inf_pos}")
print(f"Negative infinity: {inf_neg}")
print(f"NaN (Not a Number): {nan_val}")
print(f"Is inf finite? {math.isfinite(inf_pos)}")
print(f"Is inf infinite? {math.isinf(inf_pos)}")
print(f"Is NaN a number? {math.isnan(nan_val)}")

print("\n" + "=" * 50 + "\n")
