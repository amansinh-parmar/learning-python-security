a = "Coding"
b = 'For'
c = 'All'
# d = 'Python'
company = "Coding For All."

print(f"Out Put is,{company}.") 
print(company[9:11])
print(len(company)) 
print(company.upper())
print(company.lower())
print(company.title())
print(company.capitalize())
print(company.swapcase())
print(company[:6])
print(company.index('For'))
# print(company.index('Welcome'))                 #Note: Invalid variable can through the "ValueError".
print(company.find('Coding'))
print(company.replace('Coding', 'Python'))

firm = company
print(firm.replace('Coding For All.', 'Python For Everyone.'))
firm = 'Python For Everyone.'
print(firm.split())

companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split())

a = "coding for all people"
cap = a.capitalize()
index = cap.index('f')
# print(f"The index for 'F' is: {index}. ")
print(cap.rfind('l'))

usr = 'You cannot end a sentence with because because because is a conjunction'
print(usr.rindex('because'))
print(usr.find('because'))
print(usr[30:55])

c = '   Coding For All      '
print(c.startswith('cod'))
print(c.endswith('a'))
print(c.strip())

usr = '30DaysOfPython'
day = 'thirty_days_of_python'

print(usr.isidentifier())
print(day.isidentifier())

lib = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
join_lib = ' # '.join(lib)
print(join_lib)

print("I am enjoying this challenge. \n I just wonder what is next.")

#--> Use a tab escape sequence to write the following lines.
title = 'Name\tAge\tCountry\tCity'
lis = 'Asabeneh 250\tFinland\tHelsinki'
print(title)
print(lis)

#--> Use the string formatting method to display the following:
radius = 10
area = 3.14 
print(f'The area of a circle with radius {radius} is {area * radius ** 2} meters square.')

a = 8
b = 6

sum = a + b
print(f"The Value of {a} + {b} is: {a + b}")
print(f"The Value of {a} - {b} is: {a - b}")
print(f"The Value of {a} * {b} is: {a * b}")
print(f"The Value of {a} / {b} is: {a / b}")
print(f"The Value of {a} % {b} is: {a % b}")
print(f"The Value of {a} // {b} is: {a // b}")
print(f"The Value of {a} ** {b} is: {a ** b}")