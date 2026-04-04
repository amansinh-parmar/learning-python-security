class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Alternative-Constructors (with use of 'classmethod')
    @classmethod
    def fromstr(cls, string):
        return cls(string.split("-")[0], string.split("-")[1])
            # cls.string = string

p1 = Person("Jack", 26)
print(p1.name)
print(p1.age)
print(f"His name is {p1.name}.")
print(f"His age is {p1.age}.")

string = "Apex-27"
p2 = Person.fromstr(string)
print(f"His name is {p2.name}.")
print(f"His age is {p2.age}.")


#--> Example:
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_str(cls, new_string):
        name, salary = new_string.split(',')
        return cls(name, int(salary))

em1 = Employee.from_str("Amanda, 40000")
print(f"Name: {em1.name}\nSalary: {em1.salary}")
