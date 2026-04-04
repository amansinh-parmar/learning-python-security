#-->> Declaring and Calling a Function:
''' 
# syntax
# Declaring a function
def function_name():
    codes
    codes
# Calling a function
function_name()
'''
#-->> Example :
def generate_full_name ():
    first_name = 'Jack'
    last_name = 'Reacher'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name () # calling a function

#-->> Example "return" statement:
def generate_full_name ():
    first_name = 'Jack'
    last_name = 'Reacher'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())


#-->> Example :
def calculateGmean(a,b):           # def 'functionname'(perameter)
    mean = (a*b)/(a+b)             # Code 
    print(mean)                    # Code

calculateGmean(31,23)              # Calling funtion

def isGrater(a,b):
    if (a>b):
        print("First Number is Grater.")
    elif (a==b):
        print("Both Numbers are Equal.")
    else:
        print("Second Number is Grater.")
# Calling function with add argument        
isGrater(7,7)

def isLesser():
    pass            # Use pass statement later to add value code would be compile. 