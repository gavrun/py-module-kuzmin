import functools

def validate_arguments(expected_type_for_name, positive_check_for_age=True):
    """
    HOF (decorator factory) to validate arguments of a function.
    - Ensures 'name' argument is a string.
    - Optionally ensures 'age' argument is a positive integer.
    """
    def decorator(func_to_validate):
        @functools.wraps(func_to_validate)
        def wrapper_function(*args, **kwargs):
            # Try to get 'name' and 'age' from args or kwargs
            func_args_names = func_to_validate.__code__.co_varnames[:func_to_validate.__code__.co_argcount]
            bound_args = {}

            # Map positional arguments
            for i, arg_name in enumerate(func_args_names):
                if i < len(args):
                    bound_args[arg_name] = args[i]
                elif arg_name in kwargs:
                    bound_args[arg_name] = kwargs[arg_name]
                # else: argument not provided, could raise error or rely on function's default

            # Check for 'name'
            if 'name' in bound_args:
                name_val = bound_args['name']
                if not isinstance(name_val, expected_type_for_name):
                    raise TypeError(
                        f"Argument 'name' for function '{func_to_validate.__name__}' "
                        f"must be of type {expected_type_for_name.__name__}, "
                        f"but got {type(name_val).__name__}."
                    )
            else:
                # Handle case where 'name' might be missing if not a required arg
                pass


            # Check for 'age' if positive_check_for_age is True
            if positive_check_for_age and 'age' in bound_args:
                age_val = bound_args['age']
                if not isinstance(age_val, int):
                    raise TypeError(
                        f"Argument 'age' for function '{func_to_validate.__name__}' "
                        f"must be an integer, but got {type(age_val).__name__}."
                    )
                if age_val <= 0:
                    raise ValueError(
                        f"Argument 'age' for function '{func_to_validate.__name__}' "
                        f"must be positive, but got {age_val}."
                    )

            # If all checks pass, call the original function
            return func_to_validate(*args, **kwargs)
        return wrapper_function
    return decorator # Decorator factory


# Using the decorator factory to specify checks
@validate_arguments(expected_type_for_name=str, positive_check_for_age=True)
def greet_user(name, age):
    """Greets a user and mentions their age."""
    print(f"Hello, {name}! You are {age} years old.")

@validate_arguments(expected_type_for_name=str, positive_check_for_age=False)
def describe_item(name, category="general"):
    """Describes an item."""
    print(f"Item: {name}, Category: {category}")

# Test cases

# Valid calls
greet_user("Alice", 30)
describe_item("Laptop")
describe_item(name="Book", category="Fiction")

# Invalid calls (will raise errors)
print("\n--- Expecting errors below ---")
try:
    greet_user(123, 30) # name is not a string
except TypeError as e:
    print(f"Caught expected error: {e}")

try:
    greet_user("Bob", -5) # age is not positive
except ValueError as e:
    print(f"Caught expected error: {e}")

try:
    greet_user("Charlie", "twenty") # age is not an int
except TypeError as e:
    print(f"Caught expected error: {e}")

try:
    # This will pass because positive_check_for_age is False for describe_item
    describe_item("Widget", category=-1)
    # If describe_item had an 'age' param and positive_check_for_age was True,
    # and we passed a non-positive age, it would fail.
except Exception as e:
    print(f"Caught unexpected error: {e}")

