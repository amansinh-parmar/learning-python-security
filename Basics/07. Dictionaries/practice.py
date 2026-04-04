#==>> [ TIP ] = LIST ARE SORTED, REVERSED, CHANGE. WHEREAS, DICTIONARY ALWAYS HAVE KEY WITH VALUE.
        #       SO, USE WISELY 

my_dict = {
    'HTML' : 'Frontend',
    'React' : 'Frontend',
    'ExpressJS': 'Backend',
    'MongoDB': 'Server-Side'
}

# print(my_dict,'\n')

my_list = [
    {
        'x': [1,2,3],
        'y': 'Hello',
        'z':True
    },
    {
        'w': [4,5,8],
        'q': 'Hello',
        'f':True
    }
]
# print(my_list,'\n')

# print(my_list[1]['w'][1])          # '1' First Dictonary, 'w' Select Key, '1' Item on second INDEX  
# print(my_dict['HTML'][:-1])



#==>> Dictionary Methods
print('\nDictionary Methods')
user ={
    'basket': [1,2,3],
    'greet': 'hello',
    'age': 25
}
print(user, '\n')
print(f'User age: {user.get('age', 28)}')

new_user = dict(name = 'Jack Reacher')
print(new_user, '\n')

print('Dictionary Method 2')
print(user.items(), '\n')

# print('basket' in user)
# print('skill' in user, '\n')

# print('hello' in user.values())
# print('item' in user.keys())
user.update({'age': 28})
print(user)
user['greet'] = 'Hello Developer'
print(user)

# print(user.pop('age'))      # Remove particular key [pair]
# print(user.popitem())         # Remove last key [pair]
# print(user.clear())         # Empty Dictionary