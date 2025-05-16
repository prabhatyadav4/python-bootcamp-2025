a = [1,5,9,6,7,45,8,6,44,55,96,12,74,89,41]

# Uncomment the following function if you want to use a named function instead of a lambda
# def is_greater(x):
#     if x > 9:
#         return True
#     else:
#         return False

# Using the filter function with a lambda to filter elements greater than 9
new = list(filter(lambda x: x > 9, a))

print(new)
