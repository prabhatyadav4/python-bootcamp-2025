# Define a decorator factory function that takes an argument `n`
def repeat(n):
    # Define the actual decorator function
    def decorator(func):
        # Define the wrapper function that will replace the original function
        def wrapper(a):
            # Call the original function `n` times
            for i in range(n):
                func(a)
        return wrapper  # Return the wrapper function
    return decorator  # Return the decorator function

# Apply the `repeat` decorator with `n=7` to the `say_hello` function
@repeat(7)
def say_hello(a):
    # Print a greeting message with the provided argument `a`
    print(f"Hello! {a}")

# Call the decorated `say_hello` function with the argument "Harry"
say_hello("Harry")