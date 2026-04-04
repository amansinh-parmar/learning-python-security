import os
folders = os.listdir('File')

print(os.getcwd())                              #-> Find the path: "getcwd()"
# os.chdir("")                             #-> Change the Directory: "chdir("Path name")"

print(folders)

#==> Find the file inside the folder
for folder in folders:
    print(folder)
    print(os.listdir(f"File/{folder}"))                         #-> Find the folder inside the file.
