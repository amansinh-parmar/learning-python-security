# my_file = open('text.txt')

# #==> Note: Most of time useable to write code  
# try:    
#     with open('practice.txt') as my_file:
#         print(my_file.read())
# except FileNotFoundError as err:
#     print('Oops, File Not Exists!!!!\n')
#     raise err

# # ==> READ whole file
# print(my_file.read())
# my_file.seek(0)                   # .seek(0) is method of no white space after first line. with 0 index starting file content
# print(my_file.read())

# # ==> READ SINGLE line
# print(my_file.readline())
# # print(my_file.readline())
# # print(my_file.readline())
# print(my_file.readlines())      # READ ALL LINES in LIST. Discribing with '\n' which new lines in that file.
# my_file.close()


# # ==> IO Error
# # use try method and check that, file is exists or not if through or raise and error 
# try:
#     with open('sad.txt', mode='x') as my_file:      # mode='use different mode while playing with files or IO'
#         # text = my_file.wriqte(':(')
#         text = my_file.read()
#         print(text)
# except FileNotFoundError as err:               # Common error while dealing with Files 
#     print('Sorry, File not Found!!')
#     raise err
# except IOError as err:                         # # Common error while dealing with IO
#     print('This is IO Error')
#     raise err

# # => mode='w' means write and create new file 
# with open('practice.txt', mode='r+') as new_file:
#     text = new_file.write('Hello, This is Apex')
#     print(text)

# => mode='r+' means write and read in the same file
# with open('practice.txt', mode='r+') as new_file:
#     text = new_file.write('Hello, This is Apex')
#     print(text)

# => mode='a' means 'append' write at the end of the file and read in the same file
# with open('practice.txt', mode='a') as new_file:
#     text = new_file.write('I hope you enjoy this Python Codes :)')
#     print(text)

with open('practice.txt') as practice:
    print(practice.read())