print("=== OSError Examples ===")

import os
import tempfile
import socket

# 1. FileNotFoundError examples
print("1. FileNotFoundError examples:")

# Try to open non-existent file
try:
    with open("nonexistent_file.txt", "r") as f:
        content = f.read()
except FileNotFoundError as e:
    print(f"FileNotFoundError: {e}")
    print(f"Error code: {e.errno}")
    print(f"Error message: {e.strerror}")
    print(f"Filename: {e.filename}")

# Try to remove non-existent file
try:
    os.remove("nonexistent_file.txt")
except FileNotFoundError as e:
    print(f"Remove failed: {e}")

# Try to access non-existent directory
try:
    os.chdir("nonexistent_directory")
except FileNotFoundError as e:
    print(f"Directory change failed: {e}")

# 2. PermissionError examples
print("\n2. PermissionError examples:")

# Create a temporary file to demonstrate permission errors
temp_file = tempfile.NamedTemporaryFile(delete=False)
temp_file_path = temp_file.name
temp_file.close()

try:
    # Try to open a file that might have permission issues
    # On Windows, we'll simulate this differently
    print("Simulating permission error scenarios...")
    
    # Create a read-only file scenario
    with open(temp_file_path, "w") as f:
        f.write("test content")
    
    # Make file read-only
    os.chmod(temp_file_path, 0o444)  # Read-only permissions
    
    # Try to open for writing
    try:
        with open(temp_file_path, "w") as f:
            f.write("should fail")
    except PermissionError as e:
        print(f"PermissionError: {e}")
        print(f"Error code: {e.errno}")

except OSError as e:
    print(f"OS error during permission test: {e}")

finally:
    # Cleanup
    try:
        os.chmod(temp_file_path, 0o666)  # Restore permissions
        os.unlink(temp_file_path)
    except OSError:
        pass

# 3. FileExistsError examples
print("\n3. FileExistsError examples:")

# Create a temporary file
temp_file = tempfile.NamedTemporaryFile(delete=False)
temp_file_path = temp_file.name
temp_file.close()

try:
    # Try to create a file that already exists
    # Using os.open with O_CREAT | O_EXCL flags
    fd = os.open(temp_file_path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    os.close(fd)
except FileExistsError as e:
    print(f"FileExistsError: {e}")
    print(f"Error code: {e.errno}")
    print(f"Filename: {e.filename}")

# Try to create directory that exists
try:
    os.mkdir(".")  # Current directory always exists
except FileExistsError as e:
    print(f"Directory creation failed: {e}")

finally:
    # Cleanup
    try:
        os.unlink(temp_file_path)
    except OSError:
        pass

# 4. IsADirectoryError examples
print("\n4. IsADirectoryError examples:")

# Try to open directory as file
try:
    with open(".", "r") as f:  # "." is current directory
        content = f.read()
except IsADirectoryError as e:
    print(f"IsADirectoryError: {e}")
    print(f"Error code: {e.errno}")

# 5. NotADirectoryError examples
print("\n5. NotADirectoryError examples:")

# Create a regular file
temp_file = tempfile.NamedTemporaryFile(delete=False)
temp_file_path = temp_file.name
temp_file.close()

try:
    # Try to use file as directory
    fake_path = os.path.join(temp_file_path, "subfile.txt")
    with open(fake_path, "w") as f:
        f.write("test")
except NotADirectoryError as e:
    print(f"NotADirectoryError: {e}")
    print(f"Error code: {e.errno}")
except OSError as e:
    print(f"OSError (might be NotADirectoryError): {e}")

finally:
    # Cleanup
    try:
        os.unlink(temp_file_path)
    except OSError:
        pass

# 6. ConnectionError examples (network-related OSError)
print("\n6. ConnectionError examples:")

# Try to connect to non-existent server
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # Short timeout
    sock.connect(("192.0.2.1", 80))  # Non-routable IP address
except ConnectionError as e:
    print(f"ConnectionError: {e}")
    print(f"Error type: {type(e).__name__}")
except OSError as e:
    print(f"Network OSError: {e}")
    print(f"Error code: {e.errno}")
finally:
    try:
        sock.close()
    except:
        pass

# 7. Generic OSError handling
print("\n7. Generic OSError handling:")

def safe_file_operations(filename):
    """Demonstrate comprehensive OSError handling"""
    try:
        # Try multiple file operations
        print(f"Attempting operations on: {filename}")
        
        # Check if file exists
        if os.path.exists(filename):
            print("File exists")
            
            # Get file stats
            stats = os.stat(filename)
            print(f"File size: {stats.st_size} bytes")
            
            # Try to read file
            with open(filename, "r") as f:
                content = f.read(100)  # Read first 100 chars
                print(f"Content preview: {content[:50]}...")
        else:
            # Try to create file
            with open(filename, "w") as f:
                f.write("Test content")
            print("File created successfully")
    
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except PermissionError as e:
        print(f"Permission denied: {e}")
    except IsADirectoryError as e:
        print(f"Is a directory: {e}")
    except OSError as e:
        print(f"OS error: {e}")
        print(f"Error code: {e.errno}")
        print(f"System message: {e.strerror}")

# Test with various scenarios
safe_file_operations("test_file.txt")
safe_file_operations(".")  # Directory
safe_file_operations("/root/protected.txt")  # Permission issue (on Unix)

# 8. OSError with errno codes
print("\n8. OSError errno codes:")

import errno

def handle_os_error_by_errno(func, *args):
    """Handle OSError based on errno codes"""
    try:
        return func(*args)
    except OSError as e:
        if e.errno == errno.ENOENT:
            print("Error: No such file or directory")
        elif e.errno == errno.EACCES:
            print("Error: Permission denied")
        elif e.errno == errno.EEXIST:
            print("Error: File already exists")
        elif e.errno == errno.EISDIR:
            print("Error: Is a directory")
        elif e.errno == errno.ENOTDIR:
            print("Error: Not a directory")
        else:
            print(f"OS error {e.errno}: {e.strerror}")
        return None

# Test errno handling
handle_os_error_by_errno(open, "nonexistent.txt", "r")
handle_os_error_by_errno(open, ".", "r")

# 9. Cross-platform OSError handling
print("\n9. Cross-platform OSError handling:")

def safe_path_operation(path, operation="read"):
    """Cross-platform safe path operations"""
    try:
        if operation == "read":
            with open(path, "r") as f:
                return f.read()
        elif operation == "write":
            with open(path, "w") as f:
                f.write("test content")
                return "Success"
        elif operation == "delete":
            os.remove(path)
            return "Deleted"
    
    except OSError as e:
        # Platform-independent error handling
        error_type = type(e).__name__
        print(f"Platform error: {error_type}")
        print(f"Error message: {e}")
        
        # Suggest solutions based on error type
        if isinstance(e, FileNotFoundError):
            print("Suggestion: Check if file path is correct")
        elif isinstance(e, PermissionError):
            print("Suggestion: Check file permissions or run as administrator")
        elif isinstance(e, IsADirectoryError):
            print("Suggestion: Use directory operations instead of file operations")
        
        return None

# Test cross-platform handling
safe_path_operation("missing_file.txt", "read")
safe_path_operation(".", "read")

print("\n=== OSError examples completed ===")