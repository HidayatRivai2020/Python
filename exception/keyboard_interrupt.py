print("=== KeyboardInterrupt Examples ===")

import time
import signal

# 1. Basic KeyboardInterrupt handling
print("1. Basic KeyboardInterrupt handling:")
try:
    print("Simulating KeyboardInterrupt (normally Ctrl+C)")
    # Simulate KeyboardInterrupt since we can't press Ctrl+C in script
    raise KeyboardInterrupt("Simulated user interruption")
except KeyboardInterrupt:
    print("User interrupted the program!")

# 2. Long-running operation with interruption
print("\n2. Long-running operation with graceful interruption:")
def long_running_task():
    try:
        for i in range(10):
            print(f"Working... step {i+1}/10")
            time.sleep(0.5)  # Simulate work
            # Simulate interruption after 3 steps
            if i == 2:
                raise KeyboardInterrupt("User pressed Ctrl+C")
        print("Task completed successfully!")
    except KeyboardInterrupt:
        print("\nTask interrupted by user")
        print("Performing cleanup...")
        return False
    return True

success = long_running_task()
print(f"Task success: {success}")

# 3. KeyboardInterrupt with cleanup
print("\n3. KeyboardInterrupt with resource cleanup:")
class ResourceManager:
    def __init__(self, name):
        self.name = name
        self.is_open = False
    
    def open(self):
        self.is_open = True
        print(f"Resource {self.name} opened")
    
    def close(self):
        if self.is_open:
            self.is_open = False
            print(f"Resource {self.name} closed")

def process_with_resources():
    resource1 = ResourceManager("Database")
    resource2 = ResourceManager("File")
    
    try:
        resource1.open()
        resource2.open()
        
        print("Processing data...")
        time.sleep(0.2)
        
        # Simulate interruption
        raise KeyboardInterrupt("User interruption")
        
        print("Processing completed")
        
    except KeyboardInterrupt:
        print("\nInterrupted! Cleaning up resources...")
    finally:
        resource1.close()
        resource2.close()

process_with_resources()

# 4. Ignoring KeyboardInterrupt (generally not recommended)
print("\n4. Ignoring KeyboardInterrupt (demonstration only):")
def critical_operation():
    try:
        print("Starting critical operation...")
        time.sleep(0.2)
        raise KeyboardInterrupt("Attempted interruption")
        print("Critical operation completed")
    except KeyboardInterrupt:
        print("KeyboardInterrupt ignored - operation too critical to stop")
        print("Critical operation continued and completed")

critical_operation()

# 5. Partial interruption handling
print("\n5. Partial interruption - save progress:")
def save_progress_task():
    progress = []
    try:
        for i in range(5):
            # Simulate work
            work_result = f"work_item_{i+1}"
            progress.append(work_result)
            print(f"Completed: {work_result}")
            time.sleep(0.1)
            
            # Simulate interruption after 3 items
            if i == 2:
                raise KeyboardInterrupt("User interruption")
                
    except KeyboardInterrupt:
        print(f"\nInterrupted! Saving progress...")
        print(f"Completed items: {progress}")
        print("You can resume from where you left off")
        return progress
    
    print("All work completed!")
    return progress

saved_progress = save_progress_task()

# 6. Signal handling (Unix/Linux systems)
print("\n6. Signal handling demonstration:")
def signal_handler(signum, frame):
    print(f"\nReceived signal {signum}")
    print("Custom signal handler executed")
    # In real scenario, this would be called by actual Ctrl+C

# Register signal handler (this is for demonstration)
print("Signal handler registered (demonstration)")
signal_handler(signal.SIGINT, None)

# 7. KeyboardInterrupt in loops
print("\n7. KeyboardInterrupt in different loop patterns:")

# While loop
def while_loop_with_interrupt():
    count = 0
    try:
        while True:
            count += 1
            print(f"Loop iteration: {count}")
            time.sleep(0.1)
            
            # Simulate interruption after 3 iterations
            if count == 3:
                raise KeyboardInterrupt("Loop interrupted")
                
    except KeyboardInterrupt:
        print(f"\nWhile loop interrupted at iteration {count}")

while_loop_with_interrupt()

# For loop
def for_loop_with_interrupt():
    try:
        for i in range(10):
            print(f"Processing item {i+1}")
            time.sleep(0.1)
            
            # Simulate interruption
            if i == 2:
                raise KeyboardInterrupt("For loop interrupted")
                
    except KeyboardInterrupt:
        print(f"\nFor loop interrupted at item {i+1}")

for_loop_with_interrupt()

print("\n=== KeyboardInterrupt examples completed ===")