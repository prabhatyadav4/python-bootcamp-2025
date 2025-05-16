try:
    # Taking input for the first number
    a = int(input("Enter the First Number: "))
    # Taking input for the second number
    b = int(input("Enter the second Number: "))

    # Displaying the available operations
    print("Choose Operation: \n1.Addition\n2.Substraction\n3.Multiplication\n4.Division")

    # Taking input for the operation choice
    o = input("Enter Operation: ")
    # Using match-case to perform the selected operation
    match o:
        case "1":
            # Addition
            print(f"The result is {a + b}")
        case "2":
            # Subtraction
            print(f"The result is {a - b}")
        case "3":
            # Multiplication
            print(f"The result is {a * b}")
        case "4":
            # Division
            print(f"The result is {a / b}")

# Handling exceptions for invalid inputs
except Exception as e:
    print("Enter the valid value of a and b.")
