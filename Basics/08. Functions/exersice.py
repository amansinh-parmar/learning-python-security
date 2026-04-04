# Udemy Exersice: 
def highest_even(li):
    evens = []
    for item in li:
        if item % 2 == 0:
            evens.append(item)
    return max(evens)
print(f"Heighest Even number is {highest_even([4, 5, 8, 14, 82, 44])}")

# ==> Exersice 1: Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_num(num1, num2):
    return num1 + num2

print(f'Total of two numbers: {add_two_num(4,5)}')

# ==> Exersice 2: Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(r):
    pi = 3.14
    area = pi * r * r
    print(f'Area of Circle is {area}.')
    return
area_of_circle(5)

# ==> Exersice 3: Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*args):
    total = 0

    for i, value in enumerate(args):
        if not isinstance(value, (int, float)):
            return f"Error: Arrgument at position {i} ('{value}') is not a number."
        total += value
    return total
print(f"Add all numbers from Arguments: {add_all_nums(4,5,9)}")

# ==> Exersice 4: Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(c):
    fahrenheit = (c * 9/5) + 32
    return fahrenheit
print(f"Covert Celsius to Fahrenheit is {convert_celsius_to_fahrenheit(24)}")

# ==> Exersice 5: Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    if not isinstance(month, str):
        return "Error: Month must be a string."

    month = month.lower()

    if month in ["september", "october", "november"]:
        return "Autum"
    elif month in ["march", "april", "may"]:
        return "Spring"
    elif month in ["december", "january", "february"]:
        return "Winter"
    elif month in ["june", "july", "august"]:
        return "Summer"
    
print(f"January month is {check_season('january')} Season.")
print(f"March month is {check_season('march')} Season.")

# ==> Exersice 6: Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list. 
def print_list(li):
    for item in li:
        print(item)
print_list([1,2,3,4,5])

# ==> Exersice 7: Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr
print(reverse_list([1,2,3,4, 5]), '\n')

# ==> Exersice 8: Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(arr):
    capital_arr = []
    for i in arr:
        capital_arr.append(i.capitalize())
    return capital_arr
food_stuff = ['potato', 'tomato', 'mango', 'milk']
print(capitalize_list_items(food_stuff))

# ==> Exersice 9: Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(arr, add):
    capital_arr = []
    for item in arr:
        capital_arr.append(item)
    capital_arr.append(add)
    return capital_arr
food_stuff = ['potato', 'tomato', 'mango', 'milk']
print(add_item(food_stuff, 'banana'))
# Another method
def add_item(arr, item):
    new_arr = arr.copy()
    new_arr.append(item)
    item.capitalize()
    return new_arr
food_stuff = ['potato','kiwi' ,'tomato', 'mango', 'milk']
print(add_item(food_stuff, 'banana'), '\n')

# ==> Exersice 10: Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(arr, item):
    new_arr = arr.copy()
    if item in new_arr:
        new_arr.remove(item)
    return new_arr

food_stuff = ['potato','kiwi', 'tomato', 'mango', 'milk']
print(remove_item(food_stuff, 'kiwi'), '\n')

# ==> Exersice 11: Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
def odd_or_even(num):
    if num % 2 == 0:
        return f'{num} number is Even Number.'
    return f'{num} is Odd Number.'
print(odd_or_even(45))
