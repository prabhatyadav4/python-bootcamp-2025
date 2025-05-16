class Employee:
    # Constructor to initialize the Employee object with name and salary
    def __init__(self, name, salary):
        self.name = name  # Full name of the employee
        self.salary = salary  # Salary of the employee

    # Property to get the first name of the employee
    @property
    def first_name(self):
        l = self.name.split(" ")  # Split the full name into parts
        return l[0]  # Return the first part (first name)

    # Setter to update the first name of the employee
    @first_name.setter
    def first_name(self, first):
        l = self.name.split(" ")  # Split the full name into parts
        new_name = f"{first} {l[1]}"  # Replace the first name with the new one
        self.name = new_name  # Update the name attribute

# Create an Employee object with a name and salary
e = Employee("Jack Doe", 3455)

# Print the first name of the employee using the property
print(e.first_name)

# Update the first name of the employee using the setter
e.first_name = "John"

# Print the updated full name of the employee
print(e.name)
