# i = 1
# while i < 8:
#     print(i)
#     break

# i = 1;
# while i < 8:
#     print(i)
#     i += 1
#     break
# else:    # using else statement would help to when break is executed 'else:' would't work.  
#     print('Done with all the work')


#==>> Difference between 'for loop' vs 'while loop':
# my_list = [1,2,3,4]

# # for loop
# print('For Loop')
# for i in my_list:
#     print(i)

# print('\n')
# # while loop
# print('While Loop')
# i = 0
# while i < len(my_list):
#     print(my_list[i])
#     i += 1

#==>> Cool Example of While Loop in Python:
while True:
    usr = input('Say something: ')
    print(usr, '\n')
    if (usr == 'Python'):
        break

    
