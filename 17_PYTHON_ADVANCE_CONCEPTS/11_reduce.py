from functools import reduce

# List of numbers to be reduced
numbers = [1, 3, 5, 9, 6, 7]

# Function to calculate the sum of two numbers
def sum(a, b):
    return a + b

c = reduce(sum, numbers)

# Using reduce to apply the sum function cumulatively to the items of the list
# Iteration steps:
# Step 1: sum(1, 3) -> 4
# Step 2: sum(4, 5) -> 9
# Step 3: sum(9, 9) -> 18
# Step 4: sum(18, 6) -> 24
# Step 5: sum(24, 7) -> 31

# Print the final result
print(c)