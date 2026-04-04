f = open(r'D:\PyCharm\Basics\12. File Handling\marks.txt', 'r')
i = 0

while True:
    i = i + 1
    line= f.readline()
    if not line:
        break
    # print marks in different order using "loop" 
    m1 = int(line.split(",")[0])
    m2 = int(line.split(",")[1])
    m3 = int(line.split(",")[2])
    print(f"Marks of students {i} in Maths is: {m1}")
    print(f"Marks of students {i} in English is: {m2}")
    print(f"Marks of students {i} in Science is: {m3}")
    # average of scores 
    average = (int(m1)+int(m2)+int(m3))/3
    print(f"Your Average Score is: {int(average)}\n")


#==> Example: "(writeline())"
# Creating new file with "writelines('variable_name')":
with open("myfile.txt", 'w') as f:  
    lines = ["Line 1\n", "Line 2\n", "Line 3\n","Line 4\n"]
    f.writelines(lines)
    f.close()