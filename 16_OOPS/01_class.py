"""
Class and Object:
A class is a blueprint for creating objects, providing initial values for state (member variables) 
and implementations of behavior (member functions or methods). An object is an instance of a class.
This module defines an `Employee` class with a company attribute and a method to get the salary.
"""

class Employee:
    company = "HP"

    def get_salary(self):
        return 3000
    
e1 = Employee()
print(e1.get_salary())
e2 = Employee()
print(e2.get_salary())
print(e2.company)