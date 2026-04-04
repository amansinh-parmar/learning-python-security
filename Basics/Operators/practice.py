print('Truthy vs Falsey\n')
is_old =  ''
is_new = 5
# if is_old and is_new:
#     print('You are old enough to drive, and you have licenced.\n')
# else:
#     print('Your age is not qualified to drive.\n')
#     print('OKOKOKOK\n')
#====>>>>
print('TRUTHY')
# print(bool('hello'))
# print(bool(5), '\n')

print('FALSEY')
# print(bool(''))         # Empty string 
# print(bool(0))          # int 0

print('\n')# Example: 
username = 'jack-reacher'
# password = 'jack1234'
password = ''
if username and password:
    print("You're successfully.... Login\n")
else:
    print("Opps Something is MISSING....!!\n")


#====>>>>
# print('TERNARY OPERATORS\n')
# condition_if_true if condition else condition_if_else
is_friend = False
can_message = 'message allowed' if is_friend else 'not allowed to message'
print(can_message,'\n')
# 
#==>> [ Short Circuiting ]
is_Friend = True
is_User = False

if is_Friend or is_User:            # use 'or' can don't care about after the 'OR' statement
    print('Best Friend Forever\n')


#==>> [ Logical Operator ]
# print('hello' != 'hello')

#==>> EXERSICE FOR OPERATORS 
is_magican = False
is_expert = True

if is_magican and is_expert:
    print("You're a Master Magician\n")
elif is_magican and not is_expert:
    print("At least you're getting there\n")
elif not is_magican:
    print('You need Magic Power\n')


print('Bool: ', True == 1)
print('Empty String: ', '' == 1)
print('Str vs Int: ','1' == 1)
print('Empty List: ', [] == 1)
print('Int vs Float: ', 10 == 10.0)
print('List vs List: ', [] == [])
print('\n')

print("'=' Vs 'is'\n")
print('Bool: ', True is True)
print('Empty String: ', '' is 1)
print('Str vs Str: ','1' is '1')
print('Int vs Int: ',1 is 1)
print('Empty List: ', [] is 1)
print('Int vs Float: ', 10 is 10.0)
print('List vs List: ', [] is [])
print('\n')
