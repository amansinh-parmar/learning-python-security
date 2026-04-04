my_tuple = (1,2,3,4,5)
print(type(my_tuple), '\n')
print(my_tuple, '\n')
# print(my_tuple[2])

new_tuple = my_tuple[:2]
print(new_tuple, '\n')


x,y,z, * others = ('a', 'b','c', 'd', 'e', 'f', 'h', 'I')
# print(x, '\n')
# print(y,'\n')
print(others, '\n')
print(others.index('h'), '\n')
# print(len(my_tuple), '\n')


my_dict = {
    (1,2) : [4,5,8],
    'greet': 'Hello',
    'age': 28
}

# print(my_dict.items(), '\n')
# print(my_dict['greet'], '\n')