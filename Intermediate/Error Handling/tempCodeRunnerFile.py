
# # Value Error and Zero Division Error
# while True:
#     try:
#         usr = int(input("What's your age: "))
#         10/usr
#         print(f'\nHello, Welcome to ERROR HANDLING. {usr} is a great age to start your Journey.\n')
#     # except block most cases use for set the error. 
#     except ValueError:
#         print('\n Please Enter ONLY NUMBERS\n')
#     except ZeroDivisionError:
#         print('\n AGE Should be ABOVE 10.\n')
#     else:
#         print('Thank you for your time.\n')
#         break


# # Type Error
# def sum(num1, num2):
#     try:
#         return num1 + num2
#     except TypeError as err:
#         # print('Please Enter ONLY NUMBER\n' + err)
#         print(f'Please Enter ONLY NUMBER, ( {err} )\n')
# print(sum(3,'4'))

# # Another Example of using both error and get the error message in one except block
# def sum(num1, num2):
#     try:
#         return num1/num2
#     except (TypeError, ZeroDivisionError) as err:
#         print(err)
#         # print(f'Please Enter ONLY NUMBER, ( {err} )\n')
# print(sum(3,0),'\n')


# # use of 'finally' Error Block
# while True:
#     try:
#         usr = int(input("What's your age: "))
#         10/usr
#         print(f'\nHello, Welcome to ERROR HANDLING. {usr} is a great age to start your Journey.\n')
#     # except block most cases use for set the error. 
#     except ValueError:
#         print('\n Please Enter ONLY NUMBERS\n')
#         continue    # whenever usr enter string loop working continue
#     except ZeroDivisionError:
#         print('\n AGE Should be Higher than 0.\n')
#         break       # while loop is break here.
#     else:
#         print('Thank you for your time.\n')
#     finally:
#         print("Okay, I'm finally done..!!\n")
#     print('Can you HEAR ME? \n')
