# ==>> Manipulating Tuples:

countries = ("Spain", "Netherlands", "Latvia", "France", "Hugary", "Germany")
print("Length of Tuple is: ", len(countries))
print(countries)
temp = list(countries)
print("Length of List is: ", len(temp))         
temp.append("Czech Republic")
print(type(temp))
print(temp)                 # list always take 1 less element from inside value
print(temp[3])
countries = tuple(temp)
print("First Index is: ",countries[0])
print("Length of Tuple is: ", len(countries))
print(type(countries))
print(countries)

# ==>>Example(list()):

countries = ("India", "Spain", "France", "Latvia")
captial = ("Delhi", "Madrid", "Paris", "Riga")

country = list(countries)
capitals = list(captial)
countries_capitals = countries + captial
print(type(countries_capitals))
print(countries_capitals)


# ==>>Example(count()):
tup = (0,1,2,3,2,8,9,2,2,9)
cont = tup.count(2)
print(f"This Tuple has 2 Count: {cont} Times.")

# ==>>Example(index())
res = tup.index(2)
print(f"Length of Tuple is: ", len(tup))
print(f"The Element on 3 Index Value is: ",res)