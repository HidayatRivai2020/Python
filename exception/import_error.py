# ImportError Examples

print("=== ImportError Examples ===\n")

# 1. Basic ImportError examples
print("1. Basic ImportError examples:")

# Try to import non-existent module
try:
    import nonexistent_module
except ImportError as e:
    print(f"Module import error: {e}")

# Try to import non-existent submodule
try:
    import os.nonexistent_submodule
except ImportError as e:
    print(f"Submodule import error: {e}")

# 2. ModuleNotFoundError (subclass of ImportError)
print("\n2. ModuleNotFoundError examples:")

# Python 3.3+ has ModuleNotFoundError for missing modules
try:
    import completely_missing_module
except ModuleNotFoundError as e:
    print(f"ModuleNotFoundError: {e}")
    print(f"Error name: {e.name}")

# Catch both with ImportError
try:
    import another_missing_module
except ImportError as e:
    print(f"ImportError (includes ModuleNotFoundError): {e}")

# 3. ImportError with specific names
print("\n3. ImportError with specific imports:")

# Try to import non-existent function from existing module
try:
    from math import nonexistent_function
except ImportError as e:
    print(f"Function import error: {e}")

# Try to import non-existent class
try:
    from datetime import NonexistentClass
except ImportError as e:
    print(f"Class import error: {e}")

# 4. Conditional imports and optional dependencies
print("\n4. Conditional imports and optional dependencies:")

# Optional import with fallback
def safe_import_with_fallback():
    try:
        import numpy as np
        print("NumPy is available")
        return np
    except ImportError:
        print("NumPy not available, using fallback")
        
        # Create a simple fallback
        class NumpyFallback:
            @staticmethod
            def array(data):
                return list(data)
            
            @staticmethod
            def mean(data):
                return sum(data) / len(data) if data else 0
        
        return NumpyFallback()

numpy_like = safe_import_with_fallback()
data = [1, 2, 3, 4, 5]
print(f"Array: {numpy_like.array(data)}")
print(f"Mean: {numpy_like.mean(data)}")

# Multiple optional imports
def check_optional_packages():
    """Check for optional packages and provide alternatives"""
    packages = {}
    
    # Check for requests
    try:
        import requests
        packages['http'] = requests
        print("Requests library available for HTTP")
    except ImportError:
        print("Requests not available, using urllib as fallback")
        import urllib.request
        packages['http'] = urllib.request
    
    # Check for json (this should always work in modern Python)
    try:
        import json
        packages['json'] = json
        print("JSON library available")
    except ImportError:
        print("JSON library not available (very rare)")
        packages['json'] = None
    
    # Check for a definitely non-existent package
    try:
        import definitely_not_a_real_package
        packages['fake'] = definitely_not_a_real_package
    except ImportError:
        print("Fake package not found (as expected)")
        packages['fake'] = None
    
    return packages

available_packages = check_optional_packages()

# 5. ImportError in module loading
print("\n5. ImportError in module loading:")

# Create a problematic module dynamically (simulation)
import tempfile
import os
import sys

# Create temporary Python file with import error
temp_dir = tempfile.mkdtemp()
temp_file = os.path.join(temp_dir, "problematic_module.py")

with open(temp_file, "w") as f:
    f.write("""
# This module has an import error
import this_does_not_exist

def my_function():
    return "This won't be reached"
""")

# Add temp directory to Python path
sys.path.insert(0, temp_dir)

try:
    import problematic_module
except ImportError as e:
    print(f"Module loading failed: {e}")

# Cleanup
sys.path.remove(temp_dir)
try:
    os.remove(temp_file)
    os.rmdir(temp_dir)
except OSError:
    pass

# 6. Circular import simulation
print("\n6. Circular import handling:")

# Simulate circular import issue
def simulate_circular_import():
    """Demonstrate circular import problem"""
    
    # Create two temporary modules that import each other
    temp_dir = tempfile.mkdtemp()
    
    module_a_path = os.path.join(temp_dir, "module_a.py")
    module_b_path = os.path.join(temp_dir, "module_b.py")
    
    with open(module_a_path, "w") as f:
        f.write("""
print("Loading module A")
import module_b

def function_a():
    return "From A: " + module_b.function_b()
""")
    
    with open(module_b_path, "w") as f:
        f.write("""
print("Loading module B")
import module_a

def function_b():
    return "From B"
""")
    
    # Add to path and try to import
    sys.path.insert(0, temp_dir)
    
    try:
        import module_a
        print("Circular import succeeded (Python handled it)")
    except ImportError as e:
        print(f"Circular import failed: {e}")
    
    # Cleanup
    sys.path.remove(temp_dir)
    
    # Remove from sys.modules if loaded
    modules_to_remove = [mod for mod in sys.modules.keys() if mod.startswith('module_')]
    for mod in modules_to_remove:
        del sys.modules[mod]
    
    try:
        os.remove(module_a_path)
        os.remove(module_b_path)
        os.rmdir(temp_dir)
    except OSError:
        pass

simulate_circular_import()

# 7. ImportError with __init__.py issues
print("\n7. Package import issues:")

# Simulate package structure problems
def simulate_package_issues():
    """Demonstrate package import issues"""
    
    temp_dir = tempfile.mkdtemp()
    package_dir = os.path.join(temp_dir, "test_package")
    os.makedirs(package_dir)
    
    # Create package without __init__.py (Python 3.3+ allows this)
    submodule_path = os.path.join(package_dir, "submodule.py")
    
    with open(submodule_path, "w") as f:
        f.write("""
def package_function():
    return "Hello from package"
""")
    
    # Add to path
    sys.path.insert(0, temp_dir)
    
    try:
        from test_package import submodule
        print(f"Package import successful: {submodule.package_function()}")
    except ImportError as e:
        print(f"Package import failed: {e}")
    
    # Cleanup
    sys.path.remove(temp_dir)
    try:
        os.remove(submodule_path)
        os.rmdir(package_dir)
        os.rmdir(temp_dir)
    except OSError:
        pass

simulate_package_issues()

# 8. Version-specific imports
print("\n8. Version-specific imports:")

def version_specific_import():
    """Handle different Python versions or library versions"""
    
    # Try different import paths based on availability
    try:
        # Python 3.8+
        from functools import cached_property
        print("Using functools.cached_property (Python 3.8+)")
        return cached_property
    except ImportError:
        try:
            # Fallback for older Python versions
            from functools import lru_cache
            print("Using functools.lru_cache fallback")
            
            def cached_property(func):
                return property(lru_cache()(func))
            
            return cached_property
        except ImportError:
            print("No caching available")
            return property

caching_decorator = version_specific_import()

# 9. ImportError in relative imports
print("\n9. Relative import simulation:")

# Simulate relative import issues
def simulate_relative_imports():
    """Demonstrate relative import problems"""
    
    temp_dir = tempfile.mkdtemp()
    package_dir = os.path.join(temp_dir, "rel_package")
    os.makedirs(package_dir)
    
    # Create __init__.py
    init_path = os.path.join(package_dir, "__init__.py")
    with open(init_path, "w") as f:
        f.write("# Package init")
    
    # Create module with relative import
    module_path = os.path.join(package_dir, "module_with_relative.py")
    with open(module_path, "w") as f:
        f.write("""
try:
    from .nonexistent import something
except ImportError as e:
    print(f"Relative import failed: {e}")

def test_function():
    return "Relative import test"
""")
    
    sys.path.insert(0, temp_dir)
    
    try:
        from rel_package import module_with_relative
        print(f"Module loaded despite relative import error: {module_with_relative.test_function()}")
    except ImportError as e:
        print(f"Module loading failed: {e}")
    
    # Cleanup
    sys.path.remove(temp_dir)
    try:
        os.remove(module_path)
        os.remove(init_path)
        os.rmdir(package_dir)
        os.rmdir(temp_dir)
    except OSError:
        pass

simulate_relative_imports()

# 10. Best practices for ImportError handling
print("\n10. Best practices for ImportError handling:")

class ImportManager:
    """Manage imports with graceful degradation"""
    
    def __init__(self):
        self.available_modules = {}
        self.import_errors = {}
    
    def optional_import(self, module_name, fallback=None):
        """Import module with optional fallback"""
        if module_name in self.available_modules:
            return self.available_modules[module_name]
        
        try:
            module = __import__(module_name)
            self.available_modules[module_name] = module
            print(f"Successfully imported {module_name}")
            return module
        except ImportError as e:
            self.import_errors[module_name] = str(e)
            print(f"Failed to import {module_name}: {e}")
            if fallback:
                print(f"Using fallback for {module_name}")
                self.available_modules[module_name] = fallback
                return fallback
            return None
    
    def require_import(self, module_name):
        """Import required module or raise clear error"""
        try:
            module = __import__(module_name)
            self.available_modules[module_name] = module
            return module
        except ImportError as e:
            raise ImportError(
                f"Required module '{module_name}' not found. "
                f"Please install it using: pip install {module_name}"
            ) from e
    
    def get_import_summary(self):
        """Get summary of import attempts"""
        return {
            'successful': list(self.available_modules.keys()),
            'failed': self.import_errors
        }

# Test import manager
import_manager = ImportManager()

# Optional imports
import_manager.optional_import('math')  # Should succeed
import_manager.optional_import('numpy')  # Might fail
import_manager.optional_import('fake_module')  # Will fail

# Required import (comment out to avoid actual error)
try:
    import_manager.require_import('os')  # Should succeed
    print("Required import successful")
except ImportError as e:
    print(f"Required import failed: {e}")

# Get summary
summary = import_manager.get_import_summary()
print(f"\nImport summary: {summary}")

print("\n=== ImportError examples completed ===")