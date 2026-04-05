# ==>> FOR "dir" METHOD:
x = [1, 2, 3]
print(dir(x))
print(x.__add__)
# --> Example:
y = (1,2,3)
print(dir(y))
print(y.__add__)

# ==>> FOR "dict" METHOD:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.varison = 2

p = Person("John", 27)
print(p.__dict__)

# ==>> FOR "help" METHOD:
print(help(Person))

