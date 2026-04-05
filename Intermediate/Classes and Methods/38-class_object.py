class Person:
    name = "Jack"
    occupation = "Software Engineer"
    networth = 10 
    # create a function 
    def info(self):                     # "self" method use and we have to call a variable inside the class and use it in funtion. 
        print(f"{self.name} is a {self.occupation}.")

b = Person()
b.name = "Jack"
b.occupation = 'Computer Engineer'
b.info()
a = Person()
a.name = "Apex"
a.occupation = 'IT Engineer'
# print(a.name, a.occupation)
a.info()


#--> Example:
class Details:
    name = "Jack"
    age = 25

    def info(self):
        print(f"My name is {self.name} and I'm {self.age} years old.")

obj1 = Details()
obj2 = Details()
obj2.name = 'Amanda'
obj2.age = 27
obj1.info()
obj2.info()