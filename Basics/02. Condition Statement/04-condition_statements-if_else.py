# --> Example 1:
if(10>50):
    print('10 is grater than 50')
else:
    print('10 is not grater than 50. or less than 50.')

# --> Note: Another examples to understand if else in details. 
num1 = 10
num2 = 50
# num1 = num2

if(num1>num2):
    print('50 is grater than 10.')
if(num1==num2):
    print('10 is Equal to 50.')
else:
    print('50 is still not grater than 10, OR 50 is less than 10.')
    
# --> Example 2:
usr = int(input("Enter your age: \n"))
print(f"Your age is {usr}.")
''' Conditional Operators:
    >, <, >=, <=, ==, !=
    print(num > 18)
    print(num < 18)
    print(num >= 18)
    print(num <= 18)
    print(num == 18)
    print(num != 18)
    '''
if(usr>18):
    print("You can Drive.")
else:
    print("You need to wait to turn your age 18.")

# --> Example 3:
num = 30

if (num>50):
    print('Number is not grater than 20.')
elif(num==30):
    print("Number is equal to 30.")
else:
    print("Number is Below 19.")

# --> Example 4:
applePrice = 70
budget = 500

if(budget - applePrice < 50):
    print('You can buy an Apple.')
elif(budget - applePrice < 100):
    print('Still you can buy an Apple.')
else:
    print('You can not afford to buy an Apple.')

# --> Example 5:
num = int(input('Enter the value of number: '))
if (num < 0):
    print("Number is Negative.")
elif(num == 999):
    print("Number is Special.")
else:
    print("Number is Positive.")

print("You're goin' on RIGHT PATH:)")

# --> Nested if Statement:
num = 7
if(num < 0):
    print("Number is Negative")
elif(num > 0):
    if(num <= 10):
        print("Number is between 1-10.")
    elif(num > 10 and num <= 20):
        print("Number is Between 10-20.")
    else:
        print("Number is grater than 20.")
else:
    print("Number is Zero.")

# --> Example 6:
import time

timestamp = time.strftime("%H:%M:%S")
print(timestamp)
# print(int(timestamp))

timestamp = int(time.strftime("%H"))            #->Note: Using "int" data type to write proper numbers.
print(timestamp)

timestamp = time.strftime("%M")
print(timestamp)

timestamp = time.strftime("%S")
print(timestamp)