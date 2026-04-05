#==> Default constructors (Self):
class Person:
    name = "Jack"
    occupation = "Software Engineer"
    networth = 10 
    # create a function 
    def info(self):                     # "self" method use and we have to call a variable inside the class and use it in funtion. 
        print(f"{self.name} is a {self.occupation}.")

a = Person()
a.info()

print("\n\n")

#==> Patameterized Constructor (self, 'parameter', 'parameter'):
class Person:
    # name = "Apex"
    # occ = "Devloper"

    "almost everytime use when we use 'class' method."
    def __init__(self, name, occ):
        print("<<Welcome to Python>>")
        # pass
        self.name = name 
        self.occ = occ

    def info(self):
        print(f"{self.name} is a {self.occ}.")


a = Person("Jack", "Devloper")
b = Person("Leo", "HR")
a.info()
b.info()
