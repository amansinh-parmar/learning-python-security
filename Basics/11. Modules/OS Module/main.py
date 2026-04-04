import os 

# if folder not exists create a new folder
if(not os.path.exists("File")):
    os.mkdir("File")                #-> use of "mkdir" to create new folder

# create more folder or file using  "loop"
for i in range(0, 101):
    os.mkdir(f"File/Day {i+1}")                                                 #-> Create a new file
    
    # os.rename(f"File/Python Challenge{i+1}", f"File/Day {i+1}")               #-> "rename" the file name

