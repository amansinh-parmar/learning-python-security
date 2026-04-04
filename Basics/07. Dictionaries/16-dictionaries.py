dic = {"Movie":"Jack Reacher",
       "Actor":"Tom Crus",
       "Country":"USA"}    
print(type(dic),"\n",dic)

#=> Note: Difference between "dictionaries" and "set"
set_dic = {40,80,902.9,92}
print(type(set_dic),"\n",set_dic)

#-> Example:
id_list = {40:"JACK",
           70:"APEX",
           90:"AMANDA",
           52:"ALEXA"}

print(type(id_list),"\n",id_list)
print("Employee ID 90:",id_list[90])

#-> Example:
info = {"Name":"Apex", 
        "Age":26,
        "Eligible":True}
print(info)

#=> Example (Accessing Single Value)
# print(info["name"])                      # insert wrong value can give an "key error"
print(info.get("Name"))                    # However,use "'variable_name'.get('value') give none"
print(info.keys())                         # get 'only_key' from dictionaries
print(info.values())                       # get 'only_value' from dictionaries

#=> Example (Accessing Multiple Values)
for key in info.keys():
    # print(key)                             # get only keys
    # print(info[key])                       # get only values
    print(f"The values corresponding to the key {key} is {info[key]}.")

#=> Accessing key-value pairs:
print(info.items())
for key, value in info.items():
    print(f"The values corresponding to the key {key} is {value}.")
