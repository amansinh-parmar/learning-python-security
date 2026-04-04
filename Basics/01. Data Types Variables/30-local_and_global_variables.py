# 'Local variables' are destroyable. However, 'Global variables' are not destroy 

x = 'Apex'          # Global Variable
age = 26

def self():
    global age
    age = 27        # Local Variable
    # x = 'Jack'                
    y = 9
    print(f"My name is {x}. I'm {age} years old.")
    # return 
    print(y)
self()

print(f"My name is {x}. I'm {age} years old.")
# print(y)    # This will cause an error because y is a local variable and is not accessible outside of the function

