# -->>Practice Task: 1
'''Declare a function add_two_numbers. It takes two parameters and 
it returns a sum.'''
def add_two_numbers(a,b):
    sum = a + b
    print(sum)
    # return sum 
add_two_numbers(7,7)

# -->>Practice Task: 2
'''Area of a circle is calculated as follows: area = π x r x r. 
Write a function that calculates area_of_circle.'''
def area_of_circle(radius):
    pi = 3.14
    circle = pi * radius * radius
    print(circle)
    # return circle
area_of_circle(7)
# print(area_of_circle(7))

# -->>Practice Task: 3
'''Write a function called add_all_nums which takes arbitrary number of arguments 
and Sums all the arguments. Check if all the list items are number types. 
If not do give a reasonable feedback.'''

def add_all_nums(*numbers):
    total = 0
    for num in numbers:
        if isinstance(num, (int, float)):
            total += num
        else:
            return f"Error: '{num} is not a valid number. Please provide only numbers.'"
        return total

print(add_all_nums(1,2,3))
print(add_all_nums(1,'a',3))


# -->>Practice Task: 4
'''Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function 
which converts °C to °F, convert_celsius_to-fahrenheit.'''

def celsius_to_fahrenheith(celsisus):
    fahrenheit = (celsisus * 9/5) + 32
    return fahrenheit

print(celsius_to_fahrenheith(0))
print(celsius_to_fahrenheith(100))
print(celsius_to_fahrenheith(-40))

# -->>Practice Task: 5
'''Write a function called check-season, it takes a month parameter
and returns the season: Autumn, Winter, Spring or Summer.'''

def check_season(month):
    # Define the seasons based on the month
    if month in ['December', 'January', 'February']:
        return 'Winter'
    elif month in ['March', 'April', 'May']:
        return 'Spring'
    elif month in ['June', 'July', 'August']:
        return 'Summer'
    elif month in ['September', 'October', 'November']:
        return 'Autumn'
    else:
        return 'Invalid month'  # Handle invalid month input

# Example usage:
print(check_season('January'))  # Output: Winter
print(check_season('April'))    # Output: Spring
print(check_season('July'))     # Output: Summer
print(check_season('October'))  # Output: Autumn
print(check_season('InvalidMonth'))  # Output: Invalid month

# -->> Self Practice Task: 
'''Take user input name and birth year and check if it drive or not.'''
def usr_num():
    usr_name = str(input("Enter Your Name: "))
    usr_age = int(input("Enter Your Birth Year: "))
    age = 2024 - usr_age 
    print(usr_name)
    print(f"You are {age} old.")
    if age > 18:
        print("You are Eligible to Drive.")
    elif age == 18:
        print("You have to wait for 1 year.")
    else:
        print("You are 'Not Allow' to Drive.")
    return 

print(usr_num())

