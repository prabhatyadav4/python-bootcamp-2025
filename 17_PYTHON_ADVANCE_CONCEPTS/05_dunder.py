# Employee class definition
class Employee:
    Company = "HP"  # Class attribute

    # Initialize name and salary
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # User-friendly string representation
    def __str__(self):
        return f"The name is: {self.name} and the salary is: {self.salary}"

    # Developer-friendly string representation
    def __repr__(self):
        return f"Name: {self.name}\nSalary: {self.salary}"

    # Return the length of the employee's name
    def __len__(self):
        return len(self.name)

# Create an Employee instance
e = Employee("Harry", 10000)

print(e.name, e.salary)  # Print name and salary
print(str(e))  # Print user-friendly string
print(repr(e))  # Print developer-friendly string
print(len(e))  # Print length of name
