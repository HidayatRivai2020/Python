# ValueError Examples

print("=== ValueError Examples ===\n")

import math

# 1. Basic ValueError examples
print("1. Basic ValueError examples:")

# Invalid string to int conversion
try:
    number = int("abc")
except ValueError as e:
    print(f"String conversion error: {e}")

# Invalid string to float conversion
try:
    number = float("not_a_number")
except ValueError as e:
    print(f"Float conversion error: {e}")

# Invalid base conversion
try:
    number = int("123", base=2)  # "123" is not valid binary
except ValueError as e:
    print(f"Base conversion error: {e}")

# 2. Math domain errors
print("\n2. Math domain errors:")

# Square root of negative number
try:
    result = math.sqrt(-1)
except ValueError as e:
    print(f"Square root domain error: {e}")

# Logarithm of zero or negative number
try:
    result = math.log(0)
except ValueError as e:
    print(f"Logarithm domain error: {e}")

try:
    result = math.log(-5)
except ValueError as e:
    print(f"Negative logarithm error: {e}")

# Arc cosine out of domain
try:
    result = math.acos(2)  # acos domain is [-1, 1]
except ValueError as e:
    print(f"Arccosine domain error: {e}")

# 3. Empty sequence operations
print("\n3. Empty sequence operations:")

# max() on empty sequence
try:
    result = max([])
except ValueError as e:
    print(f"Empty sequence max error: {e}")

# min() on empty sequence
try:
    result = min([])
except ValueError as e:
    print(f"Empty sequence min error: {e}")

# statistics on empty data
try:
    import statistics
    result = statistics.mean([])
except ValueError as e:
    print(f"Empty statistics error: {e}")

# 4. Time and date parsing errors
print("\n4. Time and date parsing errors:")

from datetime import datetime

# Invalid date format
try:
    date = datetime.strptime("2023-13-45", "%Y-%m-%d")  # Invalid month/day
except ValueError as e:
    print(f"Date parsing error: {e}")

# Invalid time format
try:
    date = datetime.strptime("25:99:99", "%H:%M:%S")  # Invalid time
except ValueError as e:
    print(f"Time parsing error: {e}")

# 5. List operations
print("\n5. List operations:")

# Remove from list - value not found
my_list = [1, 2, 3, 4, 5]
try:
    my_list.remove(10)  # 10 is not in the list
except ValueError as e:
    print(f"List remove error: {e}")

# Index of value not in list
try:
    index = my_list.index(10)
except ValueError as e:
    print(f"List index error: {e}")

# 6. Custom ValueError for business logic
print("\n6. Custom ValueError for business logic:")

def validate_age(age_str):
    """Validate age with custom ValueError messages"""
    try:
        age = int(age_str)
    except ValueError:
        raise ValueError(f"Age must be a number, got: '{age_str}'")
    
    if age < 0:
        raise ValueError(f"Age cannot be negative: {age}")
    if age > 150:
        raise ValueError(f"Age seems unrealistic: {age}")
    
    return age

def validate_email(email):
    """Simple email validation"""
    if "@" not in email:
        raise ValueError(f"Invalid email format: missing '@' in '{email}'")
    if "." not in email.split("@")[1]:
        raise ValueError(f"Invalid email format: missing domain extension in '{email}'")
    return email

# Test custom validations
test_ages = ["25", "-5", "200", "abc"]
for age_str in test_ages:
    try:
        age = validate_age(age_str)
        print(f"Valid age: {age}")
    except ValueError as e:
        print(f"Age validation error: {e}")

test_emails = ["user@domain.com", "invalid_email", "user@domain"]
for email in test_emails:
    try:
        valid_email = validate_email(email)
        print(f"Valid email: {valid_email}")
    except ValueError as e:
        print(f"Email validation error: {e}")

# 7. ValueError in data processing
print("\n7. ValueError in data processing:")

def process_csv_row(row_data):
    """Process CSV row data with validation"""
    try:
        # Expected format: "name,age,salary"
        if len(row_data.split(',')) != 3:
            raise ValueError(f"Row must have 3 columns, got {len(row_data.split(','))}")
        
        name, age_str, salary_str = row_data.split(',')
        
        if not name.strip():
            raise ValueError("Name cannot be empty")
        
        try:
            age = int(age_str.strip())
        except ValueError:
            raise ValueError(f"Age must be integer: '{age_str.strip()}'")
        
        try:
            salary = float(salary_str.strip())
        except ValueError:
            raise ValueError(f"Salary must be number: '{salary_str.strip()}'")
        
        if age < 18:
            raise ValueError(f"Age must be 18 or older: {age}")
        
        if salary < 0:
            raise ValueError(f"Salary cannot be negative: {salary}")
        
        return {"name": name.strip(), "age": age, "salary": salary}
        
    except ValueError as e:
        print(f"CSV processing error: {e}")
        return None

# Test CSV processing
test_rows = [
    "John Doe,30,50000",
    "Jane Smith,25,abc",  # Invalid salary
    "Bob Wilson,16,30000",  # Too young
    "Alice,35",  # Missing column
    ",40,60000",  # Empty name
]

for row in test_rows:
    result = process_csv_row(row)
    if result:
        print(f"Processed: {result}")

# 8. ValueError with type conversion
print("\n8. ValueError with type conversion:")

def safe_convert(value, target_type):
    """Safely convert value to target type"""
    try:
        if target_type == int:
            return int(value)
        elif target_type == float:
            return float(value)
        elif target_type == bool:
            if str(value).lower() in ('true', '1', 'yes', 'on'):
                return True
            elif str(value).lower() in ('false', '0', 'no', 'off'):
                return False
            else:
                raise ValueError(f"Cannot convert '{value}' to boolean")
        else:
            raise ValueError(f"Unsupported target type: {target_type}")
    
    except ValueError as e:
        print(f"Conversion error: {e}")
        return None

# Test type conversions
test_conversions = [
    ("123", int),
    ("12.5", float),
    ("abc", int),
    ("true", bool),
    ("maybe", bool),
    ("45.6", int),  # This will fail - float string to int
]

for value, target_type in test_conversions:
    result = safe_convert(value, target_type)
    print(f"Convert '{value}' to {target_type.__name__}: {result}")

# 9. ValueError in configuration parsing
print("\n9. ValueError in configuration parsing:")

def parse_config(config_string):
    """Parse configuration string with validation"""
    config = {}
    
    try:
        for line in config_string.strip().split('\n'):
            line = line.strip()
            if not line or line.startswith('#'):
                continue
                
            if '=' not in line:
                raise ValueError(f"Invalid config line (missing '='): '{line}'")
            
            key, value = line.split('=', 1)
            key = key.strip()
            value = value.strip()
            
            if not key:
                raise ValueError(f"Empty config key in line: '{line}'")
            
            # Type inference based on value
            if value.isdigit():
                config[key] = int(value)
            elif value.replace('.', '').isdigit() and value.count('.') == 1:
                config[key] = float(value)
            elif value.lower() in ('true', 'false'):
                config[key] = value.lower() == 'true'
            else:
                config[key] = value
        
        return config
        
    except ValueError as e:
        print(f"Config parsing error: {e}")
        return None

# Test configuration parsing
config_text = """
# Database configuration
host=localhost
port=5432
timeout=30.5
ssl_enabled=true
=invalid_line
"""

result = parse_config(config_text)
print(f"Parsed config: {result}")

print("\n=== ValueError examples completed ===")