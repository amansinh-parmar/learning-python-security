# a = int(input("Enter the value between 1 to 10: "))
# print(a)
# st_a = str(a) 
# b = "quit"
# b = str(a)

user_input = input("Enter the value between 1 to 10 (or type 'quit' to exit): ")

# Check if the user wants to quit
if user_input.lower() == 'quit':
    print("You chose to quit.")
else:
    try:
        # Convert the input to an integer
        a = int(user_input)

        # Check if the value is within the valid range
        if a < 1 or a > 10:
            raise ValueError("The value should be between 1 and 10.")
        else:
            print(a)
    
    except ValueError as ve:
        print(f"Error: {ve}")



#==> Defining Custom Exceptions
'''class CustomError(Exception):
    # code......
    pass

try:
    # code.....
except CustomError:
    # code.....'''

