class Employee:
    company_name = "Apple"          # Class Variable
    no_of_employee = 0
    def __init__(self, name):
        self.name = name
        self.rais_amount = 0.02     # Instance Variable
        Employee.no_of_employee += 1

    def show_details(self):
        print(f"The employee name is {self.name}. The company employee size is {self.no_of_employee}. Company name is {self.company_name} and The raise amount is {self.rais_amount}.")

a = Employee("Apex")
a.rais_amount = 0.4
# Employee.company_name = "Google"
# print(Employee.company_name)
a.show_details()                # Both are the same thing

b = Employee("Jack")
b.company_name = "Microsoft"
Employee.show_details(b)        # Both are the same thing

c = Employee("Amanda")
c.company_name = "Google"
c.show_details()
