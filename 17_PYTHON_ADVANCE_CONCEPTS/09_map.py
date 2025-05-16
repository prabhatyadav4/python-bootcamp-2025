# List of numbers
numbers = [10, 2, 5, 8, 6]

# Function to calculate the square of a number (commented out)
# def square(x):
#     return x * x
# new = list(map(square, numbers))

# OR,

# Apply the square function to each element in the list using map with a lambda function
new = list(map(lambda x: x * x, numbers))

# Print the resulting list of squared numbers
print(new)
