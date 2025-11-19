print("=== AttributeError Examples ===")

# 1. Basic AttributeError examples
print("1. Basic AttributeError examples:")

# Accessing non-existent attribute on string
try:
    text = "hello world"
    result = text.append("!")  # Strings don't have append method
except AttributeError as e:
    print(f"String attribute error: {e}")

# Accessing non-existent attribute on number
try:
    number = 123
    result = number.split()  # Numbers don't have split method
except AttributeError as e:
    print(f"Number attribute error: {e}")

# Accessing non-existent attribute on list
try:
    my_list = [1, 2, 3]
    result = my_list.keys()  # Lists don't have keys method (dicts do)
except AttributeError as e:
    print(f"List attribute error: {e}")

# 2. Module AttributeError
print("\n2. Module AttributeError:")

import math
import os

# Accessing non-existent function in math module
try:
    result = math.invalid_function(5)
except AttributeError as e:
    print(f"Math module error: {e}")

# Accessing non-existent attribute in os module
try:
    result = os.nonexistent_attribute
except AttributeError as e:
    print(f"OS module error: {e}")

# 3. Custom class AttributeError
print("\n3. Custom class AttributeError:")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Hello, I'm {self.name}"

person = Person("Alice", 30)

# Valid attribute access
print(f"Valid access - Name: {person.name}")

# Invalid attribute access
try:
    email = person.email  # email attribute doesn't exist
except AttributeError as e:
    print(f"Person attribute error: {e}")

# Invalid method access
try:
    result = person.calculate_salary()  # Method doesn't exist
except AttributeError as e:
    print(f"Person method error: {e}")

# 4. AttributeError after object deletion
print("\n4. AttributeError after deletion:")

class Resource:
    def __init__(self):
        self.data = "important data"
        self.connection = "connected"
    
    def close(self):
        # Simulate resource cleanup
        del self.data
        del self.connection

resource = Resource()
print(f"Before close: {resource.data}")

resource.close()

try:
    print(f"After close: {resource.data}")  # Attribute deleted
except AttributeError as e:
    print(f"Deleted attribute error: {e}")

# 5. Safe attribute access patterns
print("\n5. Safe attribute access patterns:")

def safe_getattr(obj, attr_name, default=None):
    """Safely get attribute with default value"""
    try:
        return getattr(obj, attr_name)
    except AttributeError:
        return default

def has_attribute(obj, attr_name):
    """Check if object has attribute"""
    return hasattr(obj, attr_name)

# Test with Person class
person = Person("Bob", 25)

# Safe attribute access
email = safe_getattr(person, "email", "no-email@example.com")
print(f"Safe email access: {email}")

name = safe_getattr(person, "name", "Unknown")
print(f"Safe name access: {name}")

# Check attribute existence
print(f"Has name attribute: {has_attribute(person, 'name')}")
print(f"Has email attribute: {has_attribute(person, 'email')}")

# 6. Dynamic attribute access
print("\n6. Dynamic attribute access:")

class DynamicObject:
    def __init__(self):
        self.existing_attr = "I exist!"
    
    def __getattr__(self, name):
        # Called when attribute is not found through normal means
        if name.startswith("dynamic_"):
            return f"Dynamic attribute: {name}"
        raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")

dynamic_obj = DynamicObject()

# Existing attribute
print(f"Existing: {dynamic_obj.existing_attr}")

# Dynamic attribute
print(f"Dynamic: {dynamic_obj.dynamic_test}")

# Non-existent attribute
try:
    result = dynamic_obj.invalid_attr
except AttributeError as e:
    print(f"Dynamic object error: {e}")

# 7. AttributeError in inheritance
print("\n7. AttributeError in inheritance:")

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def bark(self):
        return "Woof!"

class Cat(Animal):
    def meow(self):
        return "Meow!"

# Create instances
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Valid method calls
print(f"Dog speak: {dog.speak()}")
print(f"Dog bark: {dog.bark()}")
print(f"Cat meow: {cat.meow()}")

# Invalid method calls
try:
    result = dog.meow()  # Dogs don't meow
except AttributeError as e:
    print(f"Dog meow error: {e}")

try:
    result = cat.bark()  # Cats don't bark
except AttributeError as e:
    print(f"Cat bark error: {e}")

# 8. AttributeError with property decorators
print("\n8. AttributeError with property decorators:")

class Temperature:
    def __init__(self):
        self._celsius = 0
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32
    
    # Note: no setter for fahrenheit

temp = Temperature()
temp.celsius = 25
print(f"Celsius: {temp.celsius}")
print(f"Fahrenheit: {temp.fahrenheit}")

# Try to set read-only property
try:
    temp.fahrenheit = 100  # No setter defined
except AttributeError as e:
    print(f"Read-only property error: {e}")

# 9. AttributeError with None objects
print("\n9. AttributeError with None objects:")

def get_user_data(user_id):
    # Simulate database lookup that might return None
    if user_id == 1:
        return {"name": "Alice", "email": "alice@example.com"}
    else:
        return None

# Successful case
user = get_user_data(1)
if user:
    print(f"User name: {user['name']}")

# Failure case
user = get_user_data(999)
try:
    print(f"User name: {user['name']}")  # user is None
except AttributeError as e:
    print(f"None object error: {e}")

# Better handling
user = get_user_data(999)
if user:
    print(f"User name: {user.get('name', 'Unknown')}")
else:
    print("User not found")

# 10. AttributeError prevention and debugging
print("\n10. AttributeError prevention and debugging:")

class DebuggedClass:
    def __init__(self):
        self.valid_attr = "I'm valid"
        self._private_attr = "I'm private"
    
    def __getattribute__(self, name):
        # This is called for ALL attribute access
        try:
            return super().__getattribute__(name)
        except AttributeError as e:
            print(f"Debug: Attempted to access '{name}' which doesn't exist")
            print(f"Available attributes: {[attr for attr in dir(self) if not attr.startswith('__')]}")
            raise e

debug_obj = DebuggedClass()

# Valid access
print(f"Valid: {debug_obj.valid_attr}")

# Invalid access with debugging
try:
    result = debug_obj.nonexistent
except AttributeError as e:
    print(f"Debugged error: {e}")

# Comprehensive attribute checker
def analyze_object(obj):
    """Analyze object attributes and methods"""
    print(f"\nAnalyzing {type(obj).__name__}:")
    print(f"All attributes: {dir(obj)}")
    print(f"Public attributes: {[attr for attr in dir(obj) if not attr.startswith('_')]}")
    print(f"Methods: {[attr for attr in dir(obj) if callable(getattr(obj, attr, None))]}")
    print(f"Data attributes: {[attr for attr in dir(obj) if not callable(getattr(obj, attr, None)) and not attr.startswith('_')]}")

# Analyze different object types
analyze_object("string")
analyze_object([1, 2, 3])
analyze_object(Person("Test", 20))

print("\n=== AttributeError examples completed ===")