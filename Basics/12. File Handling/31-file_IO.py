#==> READING a file:

# "File Path"/"File_name"
f = open(r'D:\PyCharm\Basics\12. File Handling\file.txt', 'r')

text = f.read()
f.close()                     # .close() must be important to run the file
print(text)


#==> WRITING a file:
f = open(r'D:\PyCharm\Basics\12. File Handling\write_file.txt', 'w')
# text inside the 'write()'
f.write('Hello, Welcome to File Handling Series.')
f.close()


# #==> APPENDING TEXT in file:
f = open(r'D:\PyCharm\Basics\12. File Handling\write_file.txt', 'a')
# text inside the 'write()'
f.write("Instead using 'w' rathr than, Use 'a' to append anything in the file Without remove previous data.")
f.close()


#==> WITH Statement to WRITE file:
with open("Write_file.text", 'a') as f:
    f.write("Hey, I am inside with statement. ")


#==> WITH Statement to READ file:
with open(r'D:\PyCharm\Basics\12. File Handling\write_file.text', 'r') as f:
    text = f.read()
    f.close()
    print(text)