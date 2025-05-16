class Employee:
    company = "HP"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    # Instance Method
    def print_info(self):
        info = f"The name of the employee is: {self.name} and the salary is: {self.salary}"
        print(info)
    
    # Static Method
    @staticmethod
    def sum(a, b):
        return a+b
    
    # Class Method
    @classmethod
    def print_comp(cls):
        print(cls.company)

    @classmethod
    def change_comp(cls, new_comp):
        cls.company = new_comp

e1 = Employee("Jack", 12500)
e2 = Employee("Jill", 12000)
e1.print_info()
e2.print_info()
print(e2.sum(4,6))
e1.print_comp()
e2.change_comp("Acer")
print(Employee.company)