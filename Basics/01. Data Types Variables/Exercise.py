#=>> AGE CALCULATOR EXERCISE: 
print('AGE CALCULATOR EXERCISE\n')
usr = input('What year were you born: ')
current_year = 2026
# 
age = current_year - int(usr)

print(f"You're {age} years old.")
print('\n')

#=>> PASSWORD CHECKER EXERCISE: 
print('PASSWORD CHECKER EXERCISE\n')
usr_name = input('What is your username? ')
usr_password = input('What is your password? ')
passowrd_length = len(usr_password)
hidden_password = 'x' * passowrd_length

print(f"Your username is '{usr_name}'")
print(f"Your password is {hidden_password} is {passowrd_length} long.")
