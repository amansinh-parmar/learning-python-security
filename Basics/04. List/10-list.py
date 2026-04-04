marks = [90,94,97,99,True]
# print(marks)
print(marks[:])
print(marks[1:len(marks)])
# print(marks[2:4])
print(marks[1:2:4])
print(type(marks))              # "list" type
print(len(marks))               #length of list
print(marks[4])                 #Accessing positive index
print(marks[-3])                #Accessing negative index

# -->>List with "Condition Statement":
if 94 in marks:
    print("Yes") 
else:
    print("No")

# -->>List with "for loop"
for mark in marks:
    print(mark)

# -->>List with "loop"
lst = [i for i in range(10)]
print(lst)
lst = [i for i in range(10) if i%2 == 0]
print(lst)