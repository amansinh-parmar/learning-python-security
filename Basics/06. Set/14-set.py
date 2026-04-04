#=> 'Empty Set' only create using "set()"
alexa = {}                                 # "{}" cretae a 'empty dictonary'.
jack = set()                              # "set()" create a 'empty set'.
print(type(alexa), alexa)                   # Dict. - {}
print(type(jack),jack)                    # Set - set() 

#-> Example:
s = {1,2,3,4,5}
print(type(s), s)

#=> Note: Sets are print in any order, However, it won't check which element you write first. and 
# When to add same element multiple times in same set it print only single value.
info = {"Carla", 90, 9.5, True, 90}
print(info)

for value in info:
    print(value)