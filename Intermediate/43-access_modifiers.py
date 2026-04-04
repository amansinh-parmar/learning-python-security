# >> Public Access Modifiers <<
class Employee:
    def __init__(self):
        self.name = "Jack"
        self.age = 26

a = Employee()
# print(a.name)
print(f"My name is {a.name} and I'm {a.age} years old.")


# >>Private Access Modifiers<< ##--> using "__" with anyone variable or fuction it become 'private' 
class Myself:
    def about_me(self):
        self.name = "Apex"
        self.language = "Python"
        self.experince = 4
        self.__passion = "Hacking"

a = Myself()
# print(a.name))
a.about_me()
print(f"Name: {a.name}\nProgramming Language: {a.language}\nWorking Exeprince: {a.experince}")
# print(a.__passion)          # Private Access Modifiers ## Can't be access directly

#->Name Mangling Method:
print(a._Myself__passion)       ## Can be access indirectly
print(a.__dir__())


# >>Protected Access Modifiers<< ## use of single "_"  
class Student:
    def __init__(self):
        self._name = "Apex"

    def _fullname(self):            # Protected Method
        return "Tech By Apex"

class Subject(Student):             # Inherited Class
    pass

obj = Student()
obj = Subject()
print(obj._name)
print(obj._fullname())

obj1 = Student()
obj1 = Subject()
# print(dir(obj1))

print(obj1._name)
print(obj1._fullname())
