# Define a decorator function
def decorator(func):
    def wrapper():
        # Code to execute before the function call
        print("I am about to execute a function...")
        func()  # Call the original function
        # Code to execute after the function call
        print("I have executed a function...")
    return wrapper  # Return the wrapper function

# Define a simple function to be decorated
@decorator  # Apply the decorator to the function
def say_hello():
    print("Hello...")

# Call the decorated function
say_hello()

"""
We can manually call the decorator by this method:
def say_hello():
    print("Hello...")

f = decorator(say_hello)
f()
"""