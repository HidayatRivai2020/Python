print("=== GeneratorExit Examples ===")

# 1. Basic GeneratorExit with generator.close()
print("1. Basic GeneratorExit when closing generator:")
def simple_generator():
    try:
        count = 0
        while True:
            yield f"value_{count}"
            count += 1
    except GeneratorExit:
        print("Generator received GeneratorExit - cleaning up")
        # Must re-raise GeneratorExit
        raise

gen = simple_generator()
print(f"Generated: {next(gen)}")
print(f"Generated: {next(gen)}")
print("Closing generator...")
gen.close()
print("Generator closed")

# 2. GeneratorExit with cleanup operations
print("\n2. GeneratorExit with resource cleanup:")
def resource_generator():
    print("Resource acquired")
    try:
        count = 0
        while True:
            yield f"data_{count}"
            count += 1
    except GeneratorExit:
        print("GeneratorExit caught - releasing resources")
        print("Resource cleanup completed")
        raise  # Must re-raise

gen = resource_generator()
print(f"Got: {next(gen)}")
print(f"Got: {next(gen)}")
print("Closing generator with cleanup...")
gen.close()

# 3. GeneratorExit in context manager
print("\n3. GeneratorExit with context manager:")
def file_reader_generator(filename):
    print(f"Opening file: {filename}")
    try:
        # Simulate file reading
        lines = ["line 1", "line 2", "line 3", "line 4", "line 5"]
        for line in lines:
            yield line
    except GeneratorExit:
        print("GeneratorExit - closing file")
        raise
    finally:
        print("File closed (finally block)")

# Using generator in context-like manner
gen = file_reader_generator("example.txt")
print(f"Read: {next(gen)}")
print(f"Read: {next(gen)}")

# Explicit close triggers GeneratorExit
gen.close()

# 4. GeneratorExit when generator goes out of scope
print("\n4. GeneratorExit during garbage collection:")
def monitored_generator():
    try:
        count = 0
        while True:
            yield f"item_{count}"
            count += 1
    except GeneratorExit:
        print("GeneratorExit during garbage collection")
        raise

def create_and_abandon_generator():
    gen = monitored_generator()
    next(gen)  # Start the generator
    # Generator goes out of scope here

create_and_abandon_generator()
import gc
gc.collect()  # Force garbage collection

# 5. Improper GeneratorExit handling (what not to do)
print("\n5. Improper GeneratorExit handling (demonstration):")
def bad_generator():
    try:
        count = 0
        while True:
            yield f"bad_value_{count}"
            count += 1
    except GeneratorExit:
        print("BAD: Catching GeneratorExit without re-raising")
        # This is wrong - should re-raise GeneratorExit
        return "Should not return here"

gen = bad_generator()
print(f"Generated: {next(gen)}")
try:
    gen.close()
except RuntimeError as e:
    print(f"RuntimeError caught: {e}")

# 6. GeneratorExit with yield in exception handler
print("\n6. GeneratorExit with yield in exception handler (not allowed):")
def problematic_generator():
    try:
        count = 0
        while True:
            yield f"normal_value_{count}"
            count += 1
    except GeneratorExit:
        print("GeneratorExit caught")
        # This would be problematic in real scenarios
        # yield "cleanup_value"  # This is not allowed
        raise  # Must re-raise

gen = problematic_generator()
print(f"Generated: {next(gen)}")
gen.close()

# 7. GeneratorExit with generator delegation
print("\n7. GeneratorExit with yield from:")
def inner_generator():
    try:
        for i in range(5):
            yield f"inner_{i}"
    except GeneratorExit:
        print("Inner generator received GeneratorExit")
        raise

def outer_generator():
    try:
        yield from inner_generator()
    except GeneratorExit:
        print("Outer generator received GeneratorExit")
        raise

gen = outer_generator()
print(f"Generated: {next(gen)}")
print(f"Generated: {next(gen)}")
print("Closing delegating generator...")
gen.close()

# 8. GeneratorExit in async generator (concept demonstration)
print("\n8. GeneratorExit concept in async generators:")
def async_like_generator():
    """Simulates async generator behavior with GeneratorExit"""
    try:
        count = 0
        while True:
            # Simulate async operation
            import time
            time.sleep(0.01)
            yield f"async_result_{count}"
            count += 1
    except GeneratorExit:
        print("Async-like generator shutting down")
        # Cleanup async resources here
        raise

gen = async_like_generator()
print(f"Async result: {next(gen)}")
print(f"Async result: {next(gen)}")
print("Shutting down async generator...")
gen.close()

print("\n=== GeneratorExit examples completed ===")