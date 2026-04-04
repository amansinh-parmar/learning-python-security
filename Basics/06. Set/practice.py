my_list = [1,2,3,4,5,5]
my_list.append(7)
my_list.append(9)


my_set = {1,2,3,4,5,5}

my_set.add(7)
my_set.add(9)



# print(type(my_list), '\n')
# print(my_list, '\n')
# print(set(my_list))

# print(type(my_set), '\n')
# print(my_set, '\n')
# print(22 in my_set,'\n')
# print(len(my_set), '\n')
 
print('Practice for set')
# print(my_set, '\n')

# print('COPY SET AND DELETE OLD ONE')
new_set = my_set.copy()
my_set.clear()
# print('Delete Set: ', my_set, '\n')

# print(f'New Set: {new_set}')



# 'set' METHODS:
my_set = {1,3, 5, 'd', 'f',7,9}
your_set = {'a', 2, 4, 5, 'd', 'f', 9}


diff = my_set.difference(your_set)
print(f'Difference: {diff} \n')

my_set.discard(5)
your_set.discard(5)
print(your_set, '\n')

my_set.intersection(your_set)
print(my_set)


print(my_set.isdisjoint(your_set))

print(my_set.union(your_set))
print(my_set | your_set)