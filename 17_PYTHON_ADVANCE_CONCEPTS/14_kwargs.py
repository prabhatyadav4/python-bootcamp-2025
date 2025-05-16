# Define a function `marks` that accepts any number of keyword arguments
def marks(**kwargs):
    # Iterate through the keys of the keyword arguments
    for item in kwargs.keys():
        # Print the marks of each student in a formatted string
        print(f"The marks of {item} is {kwargs[item]}")
    
# Call the `marks` function with student names as keys and their marks as values
marks(Shubham = 32, Vikrant = 45, Prabhat = 78, Pankaj = 82)