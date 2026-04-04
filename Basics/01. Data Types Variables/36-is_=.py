# a = 4
# b = '4'

# print(a is b)                   # exact location of object in memory
# print(a == b)                   # value

#--> List:
a = [1,2,3,4]
b = [1,2,3,4]
print("'List':",a is b)             # False
print("'List':",a == b)             # True

#--> Set:
a = (1,2,3,4)
b = (1,2,3,4)
print("'Set':",a is b)             # True
print("'Set':",a == b)             # True

#--> String:
a = "Apex"
a = "Apex"
print("'String':",a is b)          # False
print("'String':",a == b)          # False 

