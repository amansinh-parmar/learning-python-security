# from datetime import datetime

# class Person:
#     def usr_name(self):
#         fname = input("Enter your first name:")
#         lname = input("Enter your last name:")
#         name = fname.capitalize() + " " + lname.capitalize()
#         return f"Hello {name}, Welcome to Python."

#     def usr_age(self):
#         usr_num = int(input("Enter your birth-date:"))
#         usr_birth = datetime.strftime(usr_num, "%Y-%m-%d")
#         curr_year = datetime.now()

#         if curr_year.month < usr_num.month or (curr_year.month == usr_num.month and curr_year.day < usr_num.day):
#             age = -1
#             return f"You are {age} years old."
    



from datetime import datetime

# Ask the user for their birthdate in the format YYYY-MM-DD
birthdate_input = input("Enter your birthdate (YYYY-MM-DD): ")

# Convert the input string to a datetime object
birthdate = datetime.strptime(birthdate_input, "%Y-%m-%d")

# Get the current date
current_date = datetime.now()

# Calculate age by subtracting birth year from current year and adjusting for birthday
age = current_date.year - birthdate.year

# If the birthday hasn't occurred yet this year, subtract 1 from the age
if current_date.month < birthdate.month or (current_date.month == birthdate.month and current_date.day < birthdate.day):
    age -= 1

# Display the result
print(f"You are {age} years old.")
