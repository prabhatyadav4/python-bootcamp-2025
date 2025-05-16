class Employee:
    company = "Asus"  # Class attribute

    def __init__(self, name, salary, bond, company):
        # Instance attributes
        self.name = name
        self.salary = salary
        self.bond = bond
        self.company = company

    def get_info(self):
        # Method to display employee details
        print(f"Name: {self.name}\nSalary: {self.salary}\nBond: {self.bond} years\nCompany: {self.company}")

# Create an instance of Employee
e1 = Employee("John McKley", 40000, 4, "Tesla")

print(e1.company)       # Prints instance attribute 'company'
print(Employee.company) # Prints class attribute 'company'

print(dir(e1))          # Prints all attributes and methods of the instance (object introspection)