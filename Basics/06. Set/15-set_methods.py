s1 = {1,2,5,9}
s2 = {4,8,9}

s3 = s1.union(s2)   
print(s3)                 # It print both sets value in one single set.
# print(s1.union(s2))         # Short way to write code.    
# print(s1,s2)                # It print two separate sets 
s1.update(s2)
print(s1,s2)


#-> Example:
cities = {"Berlin","Roterdam","Tokyo","Amsterdam","Budapest"}
cities2 = {"Delhi","Mumbai","Gujarat","Amsterdam","Berlin"} 
#-> "Union" Example:
cities3 = cities.union(cities2)         
# print(cities3)                     # It will merge two values in one set.
# print(cities.union(cities2))

#-> "Intersection" Example:
cities3 = cities.intersection(cities2)
print(cities3)                     # It will remove common element and print rest of other elements.    
cities.intersection_update(cities2)
print(cities)                      # Out-put would be the same. 
#=> Note: This above and below "intersection and intersection_update" print opposite output.
# cities.intersection_update(cities2)
# print(cities)                      # It would be print same out-put of above code.However, We don't need to write multiple lines instead of one line with  

#-> "Symmetric Difference" Example:
cities3 = cities.symmetric_difference(cities2)
print(cities3)                     # print remaining amout of intersection.
cities.symmetric_difference_update(cities2)
print(cities)                      # It would be print same out-put 
#=> Note: This above and below symmentric_difference print opposite output.
# cities.symmetric_difference(cities2)
# print(cities)

#-> DisJoint Example("isdisjoint"):This method returns "False" if items are present,else it return "True".
print(cities.isdisjoint(cities2))   # When anyone items match with another set it prints "False", if it doesn't exists it print "True".

#-> SuperSet Example("issuperjoint"):
city = {"Surat","Goa","Kerala","Spiti"}
city2 = {"Rome","Velencia","Warsaw"}

print(city.issuperset(city2))              # It print "False". However, It print true when all values are in same set.
city3 = {"Surat","Goa","Spiti"} 
print(city.issuperset(city3))              # It print "True". Because, all elements are available in same set. 
print(city3.issubset(city))                # It is a opposite of "issuperset". While it checks the city3 data does it store in city set.

#-> "add" Example:
country = {"India","Spain","USA","Singapore","UAE"}
print(country)
country.add("UK")                   # Add new single item in list
print(country)

#-> "update" Example:
country2 = {"Russia","China","Japan","Germany"}
country.update(country2)            # "update" element merge new set with an old set. 
print(country)

#-> "remove" Example:
country.remove("Singapore")         # "remove" element remove the item from the set.
country.discard("Singaporee")       # "discard" element never through an error.However, you write wrong spelling.
print(country)

#-> "pop" Example:
item = country2.pop()
# print(country)
print(item)


#-> "del" Example:
# del country                          # "del" for delete whole set 
# print(country)                       # It throws an error.    

#-> "clear" Example:
city.clear()                        # "clear" for delete every items from set.
print(city)                         # Out-put is: set()

info = {"Alexa", 90, True, 9.5}

if "Amanda" in info:
    print("Amanda is Present.")
else:
    print("Amanda is Absent.")