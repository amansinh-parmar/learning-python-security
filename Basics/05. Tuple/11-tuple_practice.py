#-> Practice Task: 2
'''Create an empty Tuple.'''
tup = ()
print(type(tup))
print(tup)

#-> Practice Task: 2
'''Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)'''
cusions = ("Jack","Alexa","Amanada", "Apex")
print("Your Sibling Names Are: ",cusions)
print("You have",len(cusions), "numbers of siblings.")

#-> Practice Task: 3
# Join brothers and sisters tuples and assign it to siblings
brother_name = ("Jack",'Apex','Alexander','Elon')
print("You have", len(brother_name), "brothers.")
sisters_name = ("Alex", 'Amanada', 'Selena', 'Alia')
print("You have", len(sisters_name), "sisters.")
siblings = brother_name + sisters_name

# How many siblings do you have?
print("You have", len(siblings), "numbers of siblings.")
print(siblings)

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
father = "Tom Crus"
mother = "Jane"
family_members = (father,mother) + siblings
print(family_members)
print("Your file type is: ",type(family_members))
print("Your family members are total: ",len(family_members))

#-> Practice Task: 4
# Unpack siblings and parents from family_members
# siblings, father, mother = family_members[:-2], family_members[-2], family_members[-1]

print("Siblings: ", family_members[2:])
print("Father: ", family_members[0])
print("Mother: ", family_members[1])

#-> Practice Task: 5
# Create fruits, vegetables and animal products tuples. 
# Join the three tuples and assign it to a variable called food_stuff_tp.

fruits = ("Mango","Apple","Banana","Kiwi")
vegetables = ("Potato", "Tomato", "Onion", "Peas")
animals = ("Dog", "Cat", "Hores", "Cow")

food_stuff_tp = fruits + vegetables + animals
print(food_stuff_tp)
print("You have middle item in your tuple or list is: ", food_stuff_tp[5])
print("Your first three items are: ",food_stuff_tp[:3])
print("Your last three items are: ",food_stuff_tp[-3:])


# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_tp = list(food_stuff_tp)
print("You have total items: ",len(food_stuff_tp))
print(food_stuff_tp)

# # Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
print("You have middle item in your tuple or list is: ", food_stuff_tp[5])

# # Slice out the first three items and the last three items from food_staff_lt list
print("Your first three items are: ",food_stuff_tp[:3])
print("Your last three items are: ",food_stuff_tp[-3:])

# Delete the food_staff_tp tuple completely
food_stuff_lt = list(food_stuff_tp)
del food_stuff_tp
print(food_stuff_lt)

# Check if an item exists in tuple
print("Orange" in fruits)                      # Output: False
print("Tomato" in vegetables)                  # Output: True

#-> Practice Task: 6
'''Check if an item exists in tuple:
Check if 'Estonia' is a nordic country
Check if 'Iceland' is a nordic country'''

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)