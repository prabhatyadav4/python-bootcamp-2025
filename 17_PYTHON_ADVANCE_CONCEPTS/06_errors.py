# Uncommented code block for continuous input and error handling
# while True:
#     try:
#         a = int(input("Enter the first number: "))  # Take first number as input
#         b = int(input("Enter the second number: "))  # Take second number as input
#         print(f"The division of a and b is: {a/b}")  # Perform division and print result

#     except ValueError:
#         print("Please don't perform bad typecast")  # Handle invalid input type
#     except ZeroDivisionError:
#         print("Hey don't divide by zero")  # Handle division by zero
#     except Exception as e:
#         print("Unknown error occurred!", e)  # Handle any other exceptions

# Take first number as input
a = int(input("Enter the first number: "))
# Take second number as input
b = int(input("Enter the second number: "))

# Raise an error if the second number is zero
if b == 0:
    raise ValueError("Please don't divide by 0")
# Perform division and print result
print(f"The division of a and b is: {a/b}")