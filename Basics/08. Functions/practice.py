# def say_hello():
#     first_name = input('Enter first name: ')
#     last_name = input('Enter last name: ')
#     full_name = first_name + ' ' + last_name
#     print(f'Hello Python Developers, Mr. {full_name}')
#     return
# say_hello()

# def hello():
#     print('Hello Python Developer..!!\n')
#     # return
# hello()
# print(hello())

#==>> use 'return' syntax
# def sum(num1,num2):
#     print('Hello Python Developer..!!')
#     return num1 + num2
    
# total = (sum(2, 4))
# print(sum(5, total))

# def sum(num1, num2):
#     def another_func(n1, n2):
#         return n1 + n2
#     return another_func(num1, num2)
    
# total = sum(4, 5)
# print(total)

#==>> Methods vs Functions
def captial():
    line = 'hello developer'.capitalize()
    # line.capitalize()
    print(line)
    return
captial()

#==>> Docstring
def test(a):
    '''
    Info: This function tests and print params
    '''
    print(a)
# test('!!!!')
# help(test)
print(test.__doc__)


# #==>> Clean Code
# def is_even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False
# print(is_even(40))

# # another method to cleanup code
# def is_even(num):
#     if num % 2 == 0:
#         return True
#     return False
# print(is_even(40))

# # another method to cleanup code
# def is_even(num):
#     return num % 2 == 0
# print(is_even(40))


# #==>> *args and *kwargs
# def super_func(*args):
#     print('\nArguments gives us a Tuple')
#     print(args)
#     return sum(args)
# print(super_func(1,2,3,4,5))

# def super_func(*args, **kwargs):
#     print('\nKeyword Arguments gives us a Dictionary')
#     print(kwargs)
#     return sum(args)
# print(super_func(1,2,3,4,5, num1 = 5, num2 = 9))


def super_func(*args, **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args)+ total

print(super_func(1,2,3,4,5, num1=5, num2=4))

#Rule: params, *args, default parameters,**kwargs


#==>> Scope: What variables do I have access to?
a = 1
def parent():
    a = 20
    def confusion():
        return a
    return confusion()

print(f"Global a: {a}")
print(f"Calling Function confusion(): {parent()}")

# Scope Rules:
#1 - Start with Local
#2 - Parent Local?
#3 - Global
#4 - Built in Python Function

#==>> Global Keyword
total = 0
def counter():
    global total
    total += 1
    return total
counter()
counter()   
print(f'Total Counter is {counter()}\n')


#==>> nonlocal keyword:
def outer():
    x = 'local'
    def inner():
        nonlocal x
        x = 'nonlocal' 
        print('inner:', x)

    inner()
    print('outer:', x)

    print(f"X value is {x}")
outer()