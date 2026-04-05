class ParentClass:
    def parent_method(self):
        print("This is a 'Parent Method'.")

class ChildClass(ParentClass):
    def parent_method(self):
        print("Jack Child Method.")
        return super().parent_method()
    
    def child_method(self):
        print("This is a 'Child Method'.")

        super().parent_method()

child_object = ChildClass()
child_object.child_method()
child_object.parent_method()


# --> Example:
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id 

class Programmer(Employee):
    def __init__(self, name, emp_id, language):
        super().__init__(name, emp_id)
        self.language = language

jack = Employee("Jack", 999)
print(jack.name, jack.emp_id)

apex = Programmer("Apex", 777, "Python")
print(f"Name:{apex.name}\nID:{apex.emp_id}\nProgramming Language:{apex.language}")
