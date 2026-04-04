name_list = ['Jack', 'Apex', 'Amanada','Julia', 'Nora']

name_list[0] = 'Amax'
# print(name_list)
# print(name_list[2])


# print('\n MATRIX')
# matrix = [
#     [1, 4, 1],          #1
#     [0, 1, 0],          #2
#     [1, 0, 1]           #3
# ]
# print(matrix[0][1])         #Index 1 List and 1 Index 


print('\n LIST METHOD')
programing_language = [
    'JavaScript',
    'Python',
    'HTML',
    'React',
    'MongoDB'
]
print(programing_language)
# print('Total item inside the List: ', len(programing_language), '\n')

#=>> Adding Method
print('\n ADD METHOD')
programing_language.append('C++')       # Add item at the end of the list
# print(programing_language, '\n')

print('\n INSERT METHOD')
programing_language.insert(2, 'SQL')    # Add item with particular index
# print(programing_language,'\n')

#=>> Removing Method
print('\n REMOVE METHOD')
# programing_language.pop(2)            # Give Index to remove item from LIST  
# print(programing_language)

new_list = programing_language.pop(-1)      
# print(f'New List: [{new_list}] \n')

# programing_language.clear()             # Clear or Empty entire LIST
# print(programing_language)

#=>> List Method 2
print('Python' in programing_language)

# print(programing_language.count('JavaScript'))
print(programing_language.count('C#'))

#=>> List Method 3
# programing_language.sort()
# print(programing_language)

# programing_language.reverse()
# print(f'Reversed List: {programing_language}\n')

print(f'Sorted List: {sorted(programing_language)}\n')       # 'sorted' produced the new Array/List

#=>> Common List Patterns
print(list(range(1, 11)), '\n')

sentence = ' '
# new_line= sentence.join(['hi', 'my', 'name', 'is', 'DODO.'])
new_line = ' '.join(['Hello','Developer,','Welcome','to','Python','Journey!'])
print(new_line,'\n')

print('List Unpacking')
x,y,z, * other, d = [1,2,3,4,5,6,7,8,9]

print(x)
print(y)
print(z)
print(other)
print(d)