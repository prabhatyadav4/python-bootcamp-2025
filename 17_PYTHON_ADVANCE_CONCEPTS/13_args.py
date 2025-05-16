# Function to calculate the sum of all arguments passed
def sum(*args):
    total = 0  # Initialize total to 0
    for item in args:  # Iterate through all arguments
        total += item  # Add each argument to total
    return total  # Return the final sum

# Call the function with multiple arguments and print the result
print(sum(3, 5, 8, 9))