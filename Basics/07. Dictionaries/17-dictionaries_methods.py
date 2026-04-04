employee = {122:45, 
            123:80,
            902:40,
            245:90}
    
employee1 = {942:80,
             892:85}

#-> Example: "update":
employee1.update({942:52})          # "'variable_name'.update({'key':'value'})" for change dictionaries
employee1.update(employee)          # "update or merge" dictionaries
print(employee1)
print("Length of the employee dictionaries:",len(employee))

#-> Example: "remove" dictionaries:
# del employee1                        # use of "del", it will delete whole dictionary 
# print(employee1)
# employee1.clear()                   # dictionary would be empty
# print(employee1)                    # {}

# employee1.pop(942)                    # use ".pop('key_name')" to show particular key and value.
del employee1[942]
print(employee1)
print("Length of the dictionaries:",len(employee1))

employee1.popitem()                   # use ".popitem()" to remove last element of the dict.  
print(employee1)                      # However, add key name in ".popitem()". it will through an error