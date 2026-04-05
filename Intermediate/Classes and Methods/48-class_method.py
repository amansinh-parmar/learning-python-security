class Employee:
    company = "Apple"
    def show(self):
        print(f"This is {self.name} and His company name is {self.company}.")

    # class-method use to re-use the variable from above function in the same class.
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

emp = Employee()
emp.name = "Apex"
emp.show()
emp.change_company("Microsoft")
emp.show()
print(Employee.company)