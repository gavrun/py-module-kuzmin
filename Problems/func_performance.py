import time
import functools # Useful for decorators

def performance_tracker(func_to_track):
    """
    Higher-Order Function (decorator) to measure the execution time of another function.
    """
    @functools.wraps(func_to_track) # Preserves original function's metadata (name, docstring, etc.)
    def wrapper_function(*args, **kwargs):
        # 1. Record start time
        start_time = time.perf_counter()

        # 2. Call the original function
        result = func_to_track(*args, **kwargs)

        # 3. Record end time
        end_time = time.perf_counter()

        # 4. Calculate duration
        elapsed_time = end_time - start_time

        # 5. Print the performance
        print(f"Function '{func_to_track.__name__}' took {elapsed_time:.4f} seconds to execute.")

        # 6. Return the original function's result
        return result
    return wrapper_function

# Define some functions and "decorate" them to track their performance

@performance_tracker
def long_running_task(delay_seconds):
    """Sample function that simulates a task taking some time."""
    print(f"Starting long_running_task, will sleep for {delay_seconds}s...")
    time.sleep(delay_seconds)
    print("long_running_task finished.")
    return "Task complete!"

@performance_tracker
def quick_calculation(n):
    """Sample function that does a quick calculation."""
    print(f"Starting quick_calculation with n={n}...")
    total = sum(i for i in range(n))
    print("quick_calculation finished.")
    return total

# Call our decorated functions
result1 = long_running_task(1.5) # Sleep for 1.5 seconds
print(f"Result from long_running_task: {result1}\n")

result2 = quick_calculation(1000000) # Sum numbers up to 999,999
print(f"Result from quick_calculation: {result2}")

