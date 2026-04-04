# --> Practice Task 1:
'''Write a Python program that takes an integer input from the user and prints:

  "Even" if the number is even.
  "Odd" if the number is odd.'''

usr = int(input("Enter your number: "))

if usr % 2 == 0:
    print(f"Your {usr} number is EVEN.")
else:
    print(f"Your {usr} number is ODD.")


# --> Practice Task 2:
'''Write a program that takes two numbers as input from the user and prints:

"The first number is greater."
"The second number is greater."
"Both numbers are equal."'''

usr1 = int(input("Enter your first number: "))
usr2 = int(input("Enter your second number: "))

if(usr1>usr2):
    print(f'The first number is greater {usr1}>{usr2}')
elif(usr1<usr2):
    print(f'The second number is greater {usr1}<{usr2} ')
else:
    print("Both numbers are equal.")


# --> Practice Task 3:
'''Write a program that takes a student's score as input and prints the grade based on this scale:

Score ≥ 90: "Grade A"
Score ≥ 80: "Grade B"
Score ≥ 70: "Grade C"
Score ≥ 60: "Grade D"
Score < 60: "Fail"'''

sub1 = int(input('English Subject Score: '))
sub2 = int(input('Maths Subject Score: '))
sub3 = int(input('Physics Subject Score: '))
sub4 = int(input('Chemistry Subject Score: '))

suball = int(sub1 + sub2 + sub3 + sub4)
print("Your Total Score: ", suball,'/400')

avg = int((sub1 + sub2 + sub3 + sub4)/4)
 
if (avg >= 90):
    print(f"Your Percentage is {avg}%, Your Grade is 'A'.")
elif (avg >= 80):
    print(f"Your Percentage is {avg}%, Your Grade is 'B'.")
elif (avg >= 70):
    print(f"Your Percentage is {avg}%, Your Grade is 'C'.")
elif (avg >= 60):
    print(f"Your Percentage is {avg}%, Your Grade is 'D'.")
else:
    print(f"Your Percentage is {avg}%, You're FAIL.' ")
    

# --> Practice Task 4:
'''Write a Python program to check if a year (input by the user) is a leap year or not.

A year is a leap year if it is divisible by 4 but not divisible by 100 unless it is also divisible by 400.'''

usr = int(input("Enter the current year: "))

if (usr % 4 == 0 and usr % 100 != 0) or (usr % 400 == 0):
    print(f'{usr} is leap year.')
else:
    print(f'{usr} is not a leap year.')


# --> Practice Task 5:
'''Write a program that performs addition, subtraction, multiplication, or division based on user input.

Ask the user to enter two numbers.
Ask the user to choose an operation (+, -, *, /).
Use if-elif-else to perform the chosen operation and display the result.'''

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
sign = input("Enter the Operation (+,-,*,/):")

if sign == '+':
    result = num1 + num2
    print(f'The result of {num1} + {num2} = {result}')
elif sign == '-':
    result = num1 - num2
    print(f'The result of {num1} - {num2} = {result}')
elif sign == '*':
    result = num1 * num2
    print(f'The result of {num1} * {num2} = {result}')
elif sign == '/':
    if num2 != 0:
        result = num1 / num2
        print(f'The result of {num1} / {num2} = {result}')
    else:   
        print("Error: Cannot divide by zero!")  
else:
    print("Invalid Operation Occur, Please enter +, -, *, /.")


# --> Practice Task 6:
'''Write a program that takes the color of a traffic light as input (red, yellow, green) and prints:

"Stop" for red.
"Get ready" for yellow.
"Go" for green.'''

usr = str(input("Enter a traffic light colour(red, yellow, green): "))
if usr == usr.lower():
    print(usr.capitalize())
else:
    print(usr)

capusr = usr.capitalize()
if capusr == 'Red':
    print("'Stop' for RED.")
elif capusr == 'Yellow':
    print("'Get ready' for yellow.")
elif capusr == 'Green':
    print("'Go' for Green.")
else:
    print("Invalid Colour, Please choose the colour only one 'Red', 'Yellow', 'Green'.")


# --> Practice Task 7:
'''Ask the user to input a password. Check the following conditions and print:

"Strong Password" if the password is at least 8 characters long and contains a number.
"Weak Password" otherwise.'''

# # Get user input for password
print("Python will be let you know, Whether is it STRONG or WEAK Password.\n")
psw = input("Enter your strong password: \n ")

# Check if the password is at least 8 characters long and contains a number
if len(psw) >= 8 and any(char.isdigit() for char in psw):
    print("STRONG PASSWORD")
else:
    print("WEAK PASSWORD")

    
# --> Practice Task 8:
'''Write a program to classify a person's age into groups based on the input:

Age < 13: "Child"
13 ≤ Age < 20: "Teen"
20 ≤ Age < 60: "Adult"
Age ≥ 60: "Senior Citizen"'''

usr_age = int(input("ENTER YOUR AGE: "))

if(usr_age < 13):
    print(f'Your age is {usr_age}. You are Child.')
elif usr_age > 13 and usr_age <= 20:
    print(f'Your age is {usr_age}. You are Teenage.')
elif usr_age > 20 and usr_age <= 60:
    print(f'Your age is {usr_age}. You are Adult.')
else:
    print(f'Your age is {usr_age}. You are Senior Citizen.')
    

# --> Practice Task 9:
'''Write a program that takes a number as input and checks:

If it is divisible by 3, print "Fizz".
If it is divisible by 5, print "Buzz".
If it is divisible by both 3 and 5, print "FizzBuzz".
Otherwise, print the number itself.'''

num = int(input("ENTER YOUR NUMBER: "))

if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)


# --> Practice Task 10:
'''Write a program that compares a user-input number with a predefined number (e.g., 7) and prints:

"Too low" if the input number is less than the predefined number.
"Too high" if the input number is greater.
"Correct!" if the numbers match.'''

# Predefined number
predefined_number = 7

# Get user input for the number
user_number = int(input("Enter a number: "))

# Compare the input number with the predefined number
if user_number < predefined_number:
    print("Too low")
elif user_number > predefined_number:
    print("Too high")
else:
    print("Correct..!!")



# --> Practice Task 11:
'''Takes the total bill amount as input.
Applies a discount based on the following:
If the amount is less than $50, no discount.
If the amount is between $50 and $100, apply a 10% discount.
If the amount is above $100, apply a 20% discount.
Outputs the final price after applying the discount.'''


# Take the total bill amount as input
bill_amount = float(input("Enter the total bill amount: $"))

# Apply discount based on the given conditions
if bill_amount < 50:
    discount = 0
elif 50 <= bill_amount <= 100:
    discount = 0.10  # 10% discount
else:
    discount = 0.20  # 20% discount

# Calculate the final price after applying the discount
final_price = bill_amount * (1 - discount)

# Output the final price
print(f"The final price after discount is: ${final_price:.2f}")
