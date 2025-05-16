class Employee:
    # Constructor to initialize salary, name, and bond
    def __init__(self, salary, name, bond):
        self.salary = salary
        self.name = name
        self.bond = bond

    # Method to get the salary of the employee
    def get_salary(self):
        return self.salary

    # Method to print employee details
    def get_info(self):
        print(f"Name: {self.name}\nSalary: {self.salary}\nBond Years: {self.bond}")

# Creating an Employee object
e1 = Employee(34000, "John Doe", 4)

# Displaying employee information
e1.get_info()