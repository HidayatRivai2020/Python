# LookupError Examples

print("=== LookupError Examples ===\n")

# 1. Catching both IndexError and KeyError with LookupError
print("1. Unified lookup error handling:")
def safe_access(container, key_or_index):
    try:
        return container[key_or_index]
    except LookupError as e:
        print(f"Lookup failed: {type(e).__name__} - {e}")
        return None

# Test with list (IndexError)
my_list = [1, 2, 3, 4, 5]
result = safe_access(my_list, 10)  # IndexError
print(f"List access result: {result}")

# Test with dictionary (KeyError)
my_dict = {"a": 1, "b": 2, "c": 3}
result = safe_access(my_dict, "z")  # KeyError
print(f"Dictionary access result: {result}")

# Successful access
result = safe_access(my_list, 2)
print(f"Successful list access: {result}")

# 2. IndexError examples
print("\n2. IndexError examples:")

# List index out of range
my_list = ["apple", "banana", "cherry"]
try:
    item = my_list[5]
except IndexError as e:
    print(f"List IndexError: {e}")

# Negative index out of range
try:
    item = my_list[-10]
except IndexError as e:
    print(f"Negative index error: {e}")

# Empty list access
empty_list = []
try:
    item = empty_list[0]
except IndexError as e:
    print(f"Empty list access error: {e}")

# String index out of range
text = "Hello"
try:
    char = text[10]
except IndexError as e:
    print(f"String index error: {e}")

# Tuple index out of range
my_tuple = (1, 2, 3)
try:
    item = my_tuple[5]
except IndexError as e:
    print(f"Tuple index error: {e}")

# 3. KeyError examples
print("\n3. KeyError examples:")

# Dictionary key not found
person = {"name": "John", "age": 30, "city": "New York"}
try:
    country = person["country"]
except KeyError as e:
    print(f"Dictionary KeyError: {e}")

# Nested dictionary key error
data = {"user": {"profile": {"name": "Alice"}}}
try:
    email = data["user"]["profile"]["email"]
except KeyError as e:
    print(f"Nested dictionary KeyError: {e}")

# Set operations (sets don't support indexing, but can have lookup errors)
my_set = {1, 2, 3, 4, 5}
# Sets don't support indexing, this would be TypeError, not LookupError
# But we can demonstrate with set operations

# 4. Safe lookup patterns
print("\n4. Safe lookup patterns:")

def safe_list_get(lst, index, default=None):
    """Safe list access with default value"""
    try:
        return lst[index]
    except IndexError:
        return default

def safe_dict_get(dictionary, key, default=None):
    """Safe dictionary access with default value"""
    try:
        return dictionary[key]
    except KeyError:
        return default

# Test safe patterns
my_list = [10, 20, 30]
print(f"Safe list access: {safe_list_get(my_list, 10, 'Not found')}")
print(f"Safe list access: {safe_list_get(my_list, 1, 'Not found')}")

my_dict = {"x": 100, "y": 200}
print(f"Safe dict access: {safe_dict_get(my_dict, 'z', 'Not found')}")
print(f"Safe dict access: {safe_dict_get(my_dict, 'x', 'Not found')}")

# 5. LookupError in data processing
print("\n5. LookupError in data processing:")

def process_data_records(records, field_mapping):
    """Process records with field mapping, handle lookup errors gracefully"""
    processed = []
    
    for i, record in enumerate(records):
        try:
            # Try to map fields
            processed_record = {}
            for new_field, old_field in field_mapping.items():
                processed_record[new_field] = record[old_field]
            processed.append(processed_record)
            
        except LookupError as e:
            print(f"Record {i} processing failed: {type(e).__name__} - {e}")
            print(f"Skipping record: {record}")
            continue
    
    return processed

# Test data processing
records = [
    {"first_name": "John", "last_name": "Doe", "age": 30},
    {"first_name": "Jane", "last_name": "Smith"},  # Missing age
    {"name": "Bob Wilson", "age": 25},  # Different structure
]

field_mapping = {
    "full_name": "first_name",  # This will fail for third record
    "surname": "last_name",
    "years": "age"  # This will fail for second record
}

processed_records = process_data_records(records, field_mapping)
print(f"Processed records: {processed_records}")

# 6. Custom LookupError
print("\n6. Custom LookupError:")

class DatabaseLookupError(LookupError):
    """Custom lookup error for database operations"""
    def __init__(self, table, key, message=None):
        self.table = table
        self.key = key
        if message is None:
            message = f"Record not found in table '{table}' with key '{key}'"
        super().__init__(message)

def database_lookup(table, key):
    """Simulate database lookup"""
    database = {
        "users": {"1": "John", "2": "Jane", "3": "Bob"},
        "products": {"A1": "Laptop", "A2": "Mouse", "A3": "Keyboard"}
    }
    
    try:
        if table not in database:
            raise DatabaseLookupError(table, key, f"Table '{table}' does not exist")
        
        if key not in database[table]:
            raise DatabaseLookupError(table, key)
        
        return database[table][key]
        
    except LookupError as e:
        print(f"Database lookup failed: {e}")
        return None

# Test custom lookup error
result = database_lookup("users", "4")
print(f"Database lookup result: {result}")

result = database_lookup("orders", "1")
print(f"Database lookup result: {result}")

result = database_lookup("users", "2")
print(f"Database lookup result: {result}")

# 7. Comprehensive lookup error handling
print("\n7. Comprehensive lookup error handling:")

class DataAccessor:
    """Comprehensive data accessor with error handling"""
    
    def __init__(self):
        self.data = {
            "list_data": [1, 2, 3, 4, 5],
            "dict_data": {"a": 10, "b": 20, "c": 30},
            "nested_data": {
                "level1": {
                    "level2": ["x", "y", "z"]
                }
            }
        }
    
    def get_data(self, path):
        """Get data using dot notation path"""
        try:
            current = self.data
            for key in path.split('.'):
                if key.isdigit():
                    current = current[int(key)]
                else:
                    current = current[key]
            return current
        except LookupError as e:
            print(f"Data access failed for path '{path}': {type(e).__name__}")
            return None
    
    def safe_get_with_fallback(self, path, fallback_path=None, default=None):
        """Get data with fallback path and default"""
        result = self.get_data(path)
        if result is None and fallback_path:
            result = self.get_data(fallback_path)
        return result if result is not None else default

# Test comprehensive accessor
accessor = DataAccessor()

# Successful access
print(f"List access: {accessor.get_data('list_data.2')}")
print(f"Dict access: {accessor.get_data('dict_data.b')}")
print(f"Nested access: {accessor.get_data('nested_data.level1.level2.1')}")

# Failed access
print(f"Failed access: {accessor.get_data('list_data.10')}")
print(f"Failed access: {accessor.get_data('dict_data.z')}")

# Fallback access
result = accessor.safe_get_with_fallback(
    'dict_data.z', 
    'dict_data.a', 
    'default_value'
)
print(f"Fallback access: {result}")

print("\n=== LookupError examples completed ===")