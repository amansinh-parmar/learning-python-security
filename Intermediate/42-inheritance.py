"""class BaseClass:
   Body of base class
   class DerivedClass(BaseClass):
   Body of derived class"""

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def details(self):
        print(f"This is the employee detail:\n Name is {self.name} and ID:{self.id}")

e1 = Employee("Jack", 290)
e1.details()
e2 = Employee("Amanda", 970)
e2.details()

# >> inheritance <<     Create a new class and add a parent class
class Programmer(Employee):
    def showLanguage(self):
        print("Python is a default Language.")

e2 = Programmer("Apex", 90)
e2.showLanguage()
