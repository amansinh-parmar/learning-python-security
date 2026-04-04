# Default Arguments:
def average(a=9, b=1):       # Default Arguments
    print("The average is: ", (a+b)/2)
    
average()

#-->> Example:
def usrname(fname, mname="Jack", lname="Reacher"):
    print("Hello, ", fname, mname, lname)

usrname("Mr.")
usrname("Mr.", 'Apex','Santoni ')

#-->> Example (Key Arguments):
def usrname(fname, mname="Jack", lname="Reacher"):
    print("Hello, ", fname, mname, lname)

usrname(mname="Dr.", lname='Alexa', fname='Rachel')

#-->> Example (Required Arguments):
def usrname(fname,mname, lname):               #->Note: Perameters = Arguments
    print("Hello, ",fname, mname, lname)

# usrname(mname='Alexa', lname='Rachel')       #->Note: Requirment for Argument if an add perameter.
usrname(fname='Ms', mname='Alexa', lname='Rachel')

#-->> Example (Arbitrary Arguments):
def average(*numbers):
    print(type(numbers))
    sum = 0 
    for i in numbers:
        sum = sum + i
    print("Average is: ", sum / len(numbers))

average(5,6,7)

#-->> Example (Keyword Arbitrary Arguments):
def name(**name):
    print(type(name))
    print('Hello,', name["fname"], name["mname"], name["lname"])
    
name(fname="Jack",mname="John",lname="Reacher")

#-->> Example ("return" Statement):
def average(*numbers):
    print(type(numbers))
    sum = 0 
    for i in numbers:
        sum = sum + i
    # print("Average is: ", sum / len(numbers))
    return sum / len(numbers)
    return sum       #->Note: First "return" statement excuted after "first return" all would deny.

c = average(5,6,7)
print(c)

#-->> Practice Task: 
# Helper function to calculate the average
def calculate_average(num1, num2):
    return (num1 + num2) / 2

# Main program
def main():
    # Taking two numbers as input from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
        
    # Calculating average using the helper function
    average = calculate_average(num1, num2)
        
    # Displaying the average
    print(f"The average of {num1} and {num2} is: {average}")

# Run the program
if __name__ == "__main__":
    main()
