print("=== RuntimeError Examples ===")

import sys

# 1. Basic RuntimeError examples
print("1. Basic RuntimeError examples:")

# Manually raising RuntimeError
try:
    raise RuntimeError("This is a generic runtime error")
except RuntimeError as e:
    print(f"Runtime error: {e}")

# RuntimeError for unexpected state
def process_data(data, state):
    if state not in ["READY", "PROCESSING", "DONE"]:
        raise RuntimeError(f"Invalid state: {state}. Expected READY, PROCESSING, or DONE")
    return f"Processing {data} in state {state}"

try:
    result = process_data("test", "INVALID_STATE")
except RuntimeError as e:
    print(f"State error: {e}")

# 2. RecursionError (subclass of RuntimeError)
print("\n2. RecursionError examples:")

# Infinite recursion
def infinite_recursion(n):
    return infinite_recursion(n + 1)

try:
    infinite_recursion(0)
except RecursionError as e:
    print(f"Recursion error: {e}")

# Deep recursion with limit check
def deep_recursion(n, depth=0):
    if depth > 100:  # Manual limit
        raise RuntimeError(f"Recursion too deep: {depth}")
    if n <= 0:
        return 1
    return n * deep_recursion(n - 1, depth + 1)

try:
    result = deep_recursion(200)
except RuntimeError as e:
    print(f"Deep recursion error: {e}")
except RecursionError as e:
    print(f"System recursion limit hit: {e}")

# Check current recursion limit
print(f"Current recursion limit: {sys.getrecursionlimit()}")

# 3. RuntimeError in multithreading context
print("\n3. RuntimeError in threading context:")

import threading
import time

class ThreadSafeCounter:
    def __init__(self):
        self._value = 0
        self._lock = threading.Lock()
        self._is_locked = False
    
    def increment_unsafe(self):
        # Simulate runtime error for unsafe access
        if not self._is_locked:
            raise RuntimeError("Counter must be locked before modification")
        self._value += 1
    
    def increment_safe(self):
        with self._lock:
            self._is_locked = True
            self._value += 1
            self._is_locked = False
    
    def get_value(self):
        return self._value

counter = ThreadSafeCounter()

# Unsafe access
try:
    counter.increment_unsafe()
except RuntimeError as e:
    print(f"Thread safety error: {e}")

# Safe access
counter.increment_safe()
print(f"Counter value: {counter.get_value()}")

# 4. RuntimeError for resource management
print("\n4. RuntimeError for resource management:")

class DatabaseConnection:
    def __init__(self):
        self.is_connected = False
        self.is_transaction_active = False
    
    def connect(self):
        if self.is_connected:
            raise RuntimeError("Already connected to database")
        self.is_connected = True
        print("Connected to database")
    
    def disconnect(self):
        if not self.is_connected:
            raise RuntimeError("Not connected to database")
        if self.is_transaction_active:
            raise RuntimeError("Cannot disconnect with active transaction")
        self.is_connected = False
        print("Disconnected from database")
    
    def begin_transaction(self):
        if not self.is_connected:
            raise RuntimeError("Must be connected to start transaction")
        if self.is_transaction_active:
            raise RuntimeError("Transaction already active")
        self.is_transaction_active = True
        print("Transaction started")
    
    def commit_transaction(self):
        if not self.is_transaction_active:
            raise RuntimeError("No active transaction to commit")
        self.is_transaction_active = False
        print("Transaction committed")

db = DatabaseConnection()

# Test connection states
try:
    db.begin_transaction()  # Should fail - not connected
except RuntimeError as e:
    print(f"Transaction error: {e}")

db.connect()
db.begin_transaction()

try:
    db.disconnect()  # Should fail - transaction active
except RuntimeError as e:
    print(f"Disconnect error: {e}")

db.commit_transaction()
db.disconnect()

# 5. RuntimeError in generator context
print("\n5. RuntimeError in generator context:")

def stateful_generator():
    state = "INIT"
    try:
        while True:
            if state == "INIT":
                value = yield "Starting"
                state = "RUNNING"
            elif state == "RUNNING":
                value = yield f"Processing: {value}"
            elif state == "ERROR":
                raise RuntimeError("Generator is in error state")
            else:
                raise RuntimeError(f"Unknown generator state: {state}")
    except Exception as e:
        state = "ERROR"
        yield f"Error occurred: {e}"

gen = stateful_generator()
print(next(gen))  # Starting
print(gen.send("data1"))  # Processing: data1

# Force error state manually (simulation)
try:
    # This would normally happen due to some error condition
    raise RuntimeError("Simulated generator error")
except RuntimeError as e:
    print(f"Generator error: {e}")

# 6. RuntimeError for API misuse
print("\n6. RuntimeError for API misuse:")

class FileProcessor:
    def __init__(self):
        self.file_opened = False
        self.processing_started = False
    
    def open_file(self, filename):
        if self.file_opened:
            raise RuntimeError("File already opened. Close current file first.")
        self.filename = filename
        self.file_opened = True
        print(f"Opened file: {filename}")
    
    def start_processing(self):
        if not self.file_opened:
            raise RuntimeError("No file opened for processing")
        if self.processing_started:
            raise RuntimeError("Processing already started")
        self.processing_started = True
        print("Started processing")
    
    def get_result(self):
        if not self.processing_started:
            raise RuntimeError("Processing not started. Call start_processing() first.")
        return f"Processed content of {self.filename}"
    
    def close_file(self):
        if not self.file_opened:
            raise RuntimeError("No file to close")
        self.file_opened = False
        self.processing_started = False
        print(f"Closed file: {self.filename}")

processor = FileProcessor()

# Test API misuse
try:
    result = processor.get_result()  # Should fail - no processing started
except RuntimeError as e:
    print(f"API misuse error: {e}")

processor.open_file("test.txt")
processor.start_processing()
result = processor.get_result()
print(f"Result: {result}")
processor.close_file()

# 7. RuntimeError with system state
print("\n7. RuntimeError with system state:")

class SystemMonitor:
    def __init__(self):
        self.system_ready = True
        self.memory_available = True
        self.disk_space_ok = True
    
    def check_system_health(self):
        issues = []
        
        if not self.system_ready:
            issues.append("System not ready")
        if not self.memory_available:
            issues.append("Insufficient memory")
        if not self.disk_space_ok:
            issues.append("Low disk space")
        
        if issues:
            raise RuntimeError(f"System health check failed: {', '.join(issues)}")
        
        return "System healthy"
    
    def perform_operation(self):
        try:
            self.check_system_health()
            return "Operation completed successfully"
        except RuntimeError as e:
            return f"Operation failed: {e}"

monitor = SystemMonitor()
print(monitor.perform_operation())  # Should succeed

# Simulate system issues
monitor.memory_available = False
monitor.disk_space_ok = False
print(monitor.perform_operation())  # Should report issues

# 8. Custom RuntimeError subclasses
print("\n8. Custom RuntimeError subclasses:")

class ConfigurationError(RuntimeError):
    """Raised when configuration is invalid at runtime"""
    pass

class StateError(RuntimeError):
    """Raised when object is in invalid state for operation"""
    pass

class ResourceError(RuntimeError):
    """Raised when required resource is unavailable"""
    pass

def validate_configuration(config):
    if "required_setting" not in config:
        raise ConfigurationError("Missing required_setting in configuration")
    
    if config["required_setting"] < 0:
        raise ConfigurationError("required_setting must be non-negative")
    
    return "Configuration valid"

def operate_with_state(obj_state, operation):
    valid_states = {
        "read": ["READY", "READING"],
        "write": ["READY", "WRITING"],
        "delete": ["READY"]
    }
    
    if operation not in valid_states:
        raise StateError(f"Unknown operation: {operation}")
    
    if obj_state not in valid_states[operation]:
        raise StateError(
            f"Cannot {operation} in state {obj_state}. "
            f"Valid states: {valid_states[operation]}"
        )
    
    return f"Performing {operation} in state {obj_state}"

# Test custom errors
try:
    validate_configuration({})
except ConfigurationError as e:
    print(f"Configuration error: {e}")

try:
    operate_with_state("LOCKED", "read")
except StateError as e:
    print(f"State error: {e}")

# 9. RuntimeError in context managers
print("\n9. RuntimeError in context managers:")

class ManagedResource:
    def __init__(self, name):
        self.name = name
        self.acquired = False
        self.cleanup_called = False
    
    def __enter__(self):
        if self.acquired:
            raise RuntimeError(f"Resource {self.name} already acquired")
        self.acquired = True
        print(f"Acquired resource: {self.name}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if not self.acquired:
            raise RuntimeError(f"Resource {self.name} not acquired")
        
        if self.cleanup_called:
            raise RuntimeError(f"Cleanup already called for {self.name}")
        
        self.acquired = False
        self.cleanup_called = True
        print(f"Released resource: {self.name}")
    
    def use_resource(self):
        if not self.acquired:
            raise RuntimeError(f"Resource {self.name} not acquired")
        return f"Using resource {self.name}"

# Test context manager
try:
    with ManagedResource("database") as resource:
        result = resource.use_resource()
        print(result)
except RuntimeError as e:
    print(f"Context manager error: {e}")

# 10. RuntimeError debugging and information
print("\n10. RuntimeError debugging and information:")

class DetailedRuntimeError(RuntimeError):
    """RuntimeError with additional debugging information"""
    
    def __init__(self, message, error_code=None, context=None, suggestions=None):
        super().__init__(message)
        self.error_code = error_code
        self.context = context or {}
        self.suggestions = suggestions or []
    
    def get_debug_info(self):
        info = {
            "message": str(self),
            "error_code": self.error_code,
            "context": self.context,
            "suggestions": self.suggestions
        }
        return info

def complex_operation(data, mode, timeout):
    """Complex operation that might fail with detailed error info"""
    
    context = {
        "data_size": len(data) if hasattr(data, '__len__') else "unknown",
        "mode": mode,
        "timeout": timeout,
        "system_state": "normal"
    }
    
    try:
        if not data:
            raise DetailedRuntimeError(
                "Operation failed: empty data provided",
                error_code="E001",
                context=context,
                suggestions=["Provide non-empty data", "Check data source"]
            )
        
        if mode not in ["fast", "normal", "safe"]:
            raise DetailedRuntimeError(
                f"Operation failed: invalid mode '{mode}'",
                error_code="E002", 
                context=context,
                suggestions=["Use mode: 'fast', 'normal', or 'safe'"]
            )
        
        if timeout <= 0:
            raise DetailedRuntimeError(
                "Operation failed: invalid timeout",
                error_code="E003",
                context=context,
                suggestions=["Set timeout > 0", "Use default timeout"]
            )
        
        return f"Operation completed: {data} in {mode} mode"
        
    except DetailedRuntimeError as e:
        print(f"Detailed error: {e}")
        debug_info = e.get_debug_info()
        print(f"Debug info: {debug_info}")
        return None

# Test detailed error handling
complex_operation("", "fast", 10)  # Empty data
complex_operation("data", "invalid", 10)  # Invalid mode
complex_operation("data", "fast", -1)  # Invalid timeout
complex_operation("data", "fast", 10)  # Success

print("\n=== RuntimeError examples completed ===")