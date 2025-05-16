# Take input for the first number
"""
This script demonstrates the use of a `try-except-finally` block in Python to handle exceptions 
and ensure that certain code is executed regardless of whether an exception occurs.
Functions:
    - The script takes two integer inputs from the user.
    - It attempts to perform division of the two numbers.
    - If an exception occurs (e.g., division by zero), it is caught and handled in the `except` block.
    - The `finally` block executes unconditionally, ensuring that cleanup or final actions are performed.
Key Notes:
    - The `finally` block is particularly useful in functions where resources need to be released 
      (e.g., closing files, releasing locks, or cleaning up resources) regardless of whether an 
      exception was raised or not.
    - Even if a `return`, `break`, or `continue` statement is encountered in the `try` or `except` 
      block, the `finally` block will still execute before the control flow leaves the function.
"""
a = int(input("Enter the first number: "))

# Take input for the second number
b = int(input("Enter the second number: "))

try:
    # Attempt to perform division
    c = a/b
    print(c)
except Exception as e:
    # Handle any exception that occurs during division
    print(e)
finally:
    # This block will always execute
    print("This is a division program")
    