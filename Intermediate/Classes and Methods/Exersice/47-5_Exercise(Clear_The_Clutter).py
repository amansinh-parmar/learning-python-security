"""Write a program to clear the clutter inside a folder on your computer. 
You should use os module to rename all the png images from 1.png all the way till n.png 
where n is the number of png files in that folder. Do the same for other file formats."""

# - sfdsf.png --> 1.png
# - vfsf.png --> 2.png
# - this.png --> 3.png
# - design.png --> 4.png
# - name.png --> 5.png

import os 
# for rename any file (os.rename(r'file_name', 'rename_file_name'))
# os.rename(r"D:\PyCharm\Intermediate\Practice Exercise\clutterFolder\file.txt", "D:\PyCharm\Intermediate\Practice Exercise\clutterFolder\myfile.txt")

files = os.listdir(r"D:\PyCharm\Intermediate\Practice Exercise\clutterFolder")
# rename name start with '1'.
i = 1
# for '.png' file
for file in files:
    if file.endswith(".png"):
        print(file)
        os.rename(f"D:\PyCharm\Intermediate\Practice Exercise\clutterFolder\{file}", f"D:\PyCharm\Intermediate\Practice Exercise\clutterFolder\{i}.png")
        i = i + 1
        print(file)
        # print(os.listdir(r"D:\PyCharm\clutterFolder"))

# for '.jpg' file.
for file in files:
    if file.endswith('.jpg'):
        print(file)

# rename the file        
os.rename(r"D:\PyCharm\Intermediate\Practice Exercise\clutterFolder\City Office.jpg", r"D:\PyCharm\Intermediate\Practice Exercise\clutterFolder\4.jpg")