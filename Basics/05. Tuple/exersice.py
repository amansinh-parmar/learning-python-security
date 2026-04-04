mine = ()
print(type(mine), '\n')
# print(mine,'\n')

bro = ('Jack','Apex', 'Reacher', 'John')
sis = ('Zoya', 'Nora', 'Julia', 'Selena')

# print(f'Brothers: {bro} \n')
# print(f'Sisters: {sis} \n')

siblings = bro + sis
# print(f'Siblings: {siblings} \n')
# print(f'I have total {len(siblings)} siblings. \n')

family = (list(siblings))
family.append('Amax')
family.append('Amanda')
# print(f'I have total {len(family)} members in my Family. \n')
# print(f'Family members: {family}. \n')


parents = family[-2:]
siblings = family[:9]
# print(f'Parents :{tuple(parents)} \n')
# print(f'Siblings :{tuple(siblings)} \n')

fruits = ('Apple', 'Banana', 'Kiwi', 'Pineple')
vegetables = ('Tomato', 'Potato', 'Brokley')
animals = ('Lion', 'Tiger', 'Dog', 'Bat')

food_stuff_tp = fruits + vegetables + animals
# print(f'This is called Nature: \n{food_stuff_tp} \n')

# print(f'Nature List: \n {list(food_stuff_tp)}')

# print(len(food_stuff_tp))
nature_list = list(food_stuff_tp)
# print(f'OG List: \n{nature_list}\n')
# print(f'First Three: \n {nature_list[:3]}\n')
# print(f'Last Three: \n {nature_list[-3:]}\n')

# del food_stuff_tp
# print(food_stuff_tp)

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print(f'There is Estonia in list: {'Estonia' in nordic_countries}\n')
print(f'There is Iceland in list: {'Iceland' in nordic_countries}\n')
