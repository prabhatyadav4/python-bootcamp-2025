# Define a function that accepts any number of positional and keyword arguments
def func1(*args, **kwargs):
    # Print the tuple of positional arguments
    print(args)
    # Print the dictionary of keyword arguments
    print(kwargs)

# Call the function with some positional and keyword arguments
func1(1, 2, 5, 9, Mayank=7.1, Koushal=7.2)