import os

print("WELCOME TO, ")
os.system("python --version")           # To get version 
os.system('python -h')                  # To get full description


# --> Example 1:
x = 4 
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print('x is zero')
    # case with if-condition
    case 4:
        print("x case is 4")
    # so it is basically just an else:
    case _:
        print(x)

# --> Same example like above with some addition
x = 7
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print('x is zero')
    # case with if-condition
    case 4 if x % 2 == 0:
        print("x % 2 == 0 and case is 4")
    # Empty case with if-condition
    case _ if x < 10:
        print('x is < 10')
    # default case (will only be matched if the above cases were not matched)
    # so it is basically just an else:
    case _:
        print(x)

# --> Example 2:
x = int(input("Enter the value of x: "))

match x:
    case 0:
        print("x is zero")
    case 4:
        print('case is 4')
        
    case _ if x != 90:
        print(x, 'is not 90')
    case _ if x != 70:
        print(x, 'is not 70')
    case _:
        print(x)