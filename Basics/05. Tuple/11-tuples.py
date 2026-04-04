#==>> Not: "tuples" are 'Immutable', "strings" are 'Immutable', "lists" are "Mutable".

tp = (2, 5, 9,0,'Jack')
print(tp)
print(type(tp))
print("Length of Tuple is: ",len(tp))

#-> Indexing:
print(tp[0])
print(tp[2])
print(tp[4])

#-> Range of Index
tup = tp[2:5]
print(tup)

#-> Condition Statement:
if 'Apex' in tp:
    print("This is a 'Jack' name.")
else:
    print("You need to replace name 'Jack' with 'Apex'.")

#-> For Loop:
for t in tp:
    print(t)


#-->> Examples:
animals = ('Dog','Hores','Monkey','Cow','Cat','Goat')
print(animals[::2])                         # Positive Indexing
print(animals[-8:-1:2])                     # Negative Indexing