class Employee:
    name = "Jack"
    def __len__(self):
        i = 0
        for c in self.name:
            i = i + 1
            return i 
    def __len__(self):
        i = 0
        for c in self.name:
            i = i + 1
            return i
        
e = Employee()
print(e.name)
print(len(e))


# --> Example:
class Person:
    company = "Microsoft"

    def __len__(self):
        i = 0
        for c in self.company:
            i = i + 1
            return i
        
    # Create a function for length
    def len_fun(self):
        return len(self.company)

p = Person()
print(p.company)
print(p.len_fun())
p.company = "Apple"
print(p.company)
print(p.len_fun())
print("\n")

#--> Example (import module):
from magic import Employee

emp = Employee()
# print(emp)
print(emp.name)
print(str(emp))
print(repr(emp))
emp()                   # '__call__' method