#--> For "seek()":
# The seek() function allows you to move the current position within a file to a specific point. 
# The position is specified in bytes, and you can move either forward or backward from the current position

with open(r'D:\PyCharm\Basics\12. File Handling\seek_tell.txt', 'r') as f:
  # Move to the 10th byte in the file
  f.seek(10)

  # Read the next 5 bytes
  data = f.read(5)
  print(data)
  f.close()
  
#--> For "tell()":
# The tell() function returns the current position within the file, in bytes. This can be useful for 
# keeping track of your location within the file or for seeking to a specific position relative to the current position.

with open(r'D:\PyCharm\Basics\12. File Handling\seek_tell.txt', 'r') as f:
    print(type(f))
#   # Move to the 10th byte in the file
    f.seek(10)

    print(f.tell())
#   # Read the next 5 bytes
    data = f.read(5)
    print(data)
    f.close()
  
#--> For trunc
# When you open a file in Python using the open function, you can specify the mode in which you want to open the file.
# If you specify the mode as 'w' or 'a', the file is opened in write mode and you can write to the file.
# However, if you want to truncate the file to a specific size, you can use the truncate function.

with open(r"sample.txt",'w') as f:
    f.write("Hello, Python Coders")
    f.truncate(9)               # use truncate(add_value) 

with open(r"sample.txt",'r') as f:
    print(f.read())
    f.close()