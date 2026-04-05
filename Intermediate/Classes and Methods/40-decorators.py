# def greet(fx):
#     def mfx():
#         print("Good Morning")
#         fx()
#         print("Thanks for using function")
#     return mfx

# @greet
# def hello():
#     # usr = input("Enter your name:")
#     print("Hello, World")
    
# # greet(hello)()           # insted of using this call decorator fuction befor write new function and at the end just call the function.
# hello()

# >> Using "*args, **kwargs" <<
def greet(mx):
    def arg(*args, **kwargs):
        print("Good Morning")
        mx(*args, **kwargs)
        print("This is a right way.")
    return arg

@greet
def welcome():
    print("hello world")


def add_num(a,b):
    # total = a + b
    print(a+b)
    # print(type(total))

welcome()
greet(add_num)(4,9)         # without using greet decorator.



#==> Example:
import logging

def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated

@log_function_call
def my_function(a, b):
    return a + b