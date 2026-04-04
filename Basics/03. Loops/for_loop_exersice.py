# =========== TIP to Write a CODE ===========
# Clean
# Readability
# Predictability
# DRY
# Resusable 

#==>> Exersice
picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0],
]

# iterate over picture
# 1 Way
fill = '*'
empty = ' '
for row in picture:
    for pixel in row:
        if (pixel == 1):
            print(fill, end='')
        else:
            print(empty, end='')
    print()

# 2 Way
print('\n')
leaf = '$'
for row in picture:
    for pixel in row:
        if pixel == 0:
            print(empty, end="")
        elif pixel == 1:
            print(leaf, end="")
    print('')
print('\n')


#==>> Exeersice: Check for duplicates in list:
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n'] 

# One WAY:
seen = set()
duplicate = set()

for i in some_list:
    if i in seen:
        duplicate.add(i)
    else:
        seen.add(i)
duplicate_list = list(duplicate)
print(duplicate_list)

# Another WAY:
duplicate = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicate:
            duplicate.append(value)
print(duplicate)