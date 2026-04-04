# for i in [1,2,3,4,5,6,7,8,9]:
#     print(i)

# for j in [1,2,3,3,4,5,6,7]:
#     for i in ('Jack', 'Julia', 'Apex', 'Amanda'):
#         print(i, j)
        # print(i, j)
# print(type(j))


# ============== Iterables ==============
# my_dict =[
#         {
#         'name': 'Jack',
#         'age': 25,
#         'profession': 'B.Tech in CS'
#         },
#         {
#             'name':'Julia',
#             'age': 24,
#             'profession': 'Manager'
#         },
#         {
#             'name': 'Apex',
#             'age': 28,
#             'profession': 'Web Developer'
#         },
#         {
#             'name': 'Amanada',
#             'age': 27,
#             'profession': 'Modeling'
#         }
# ]


# for student in my_dict:
#     for key, value in student.items():
#         print(key, value)

# for student in my_dict:
#     print(student)
#     for key in student.keys():
#         print(key)
#     for value in student.values():
#         print(value)


# employee = {
#     'name':'Apex',
#     'age': 28,
#     'work_status': False
# }

# for item in employee.items():
#     print(item)


#==>> Exersice 
my_list = [1,2,3,4,5,6,7,8,9,10]
counter = 0
print(type(my_list))

# for num in my_list:
#     counter = counter + num

# print(counter)

#==>> 'range()' 
# for i in range(1, 8):
#     print(i)

# for _ in range(8, 0, -1):
# for _ in range(1, 8):
    # print(list(range(8)))

#==>> 'enumerate()' 
# for i, char in enumerate('Hello, Developers'):
# for i, char in enumerate((1,2,3,4,5)):
#     print(i, char)

#==>> Small Exersice:
for index, char in enumerate(list(range(100))):
    print(index, char)
    if char == 50:
        print(f'Your Index value of 50 is: {index}')
        break