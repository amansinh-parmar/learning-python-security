#-> Practice Task: 1
#1.Create an empty dictionary called dog
dog = {}
print(type(dog),dog)

#2.Add name, color, breed, legs, age to the dog dictionary
dog.update({"Name":"Tiger",
            "Color":"White and Grey",
            "Bread":"Huskie",
            "Age":"5 Years"})
print(dog)

# Create a student dictionary and add 
# first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student_dict = {"First Name":"Jack",
                "Last Name":"Reacher",
                "Gender":"Male",
                "Age":26,
                "Marital Status":"Single",
                "Skills":["Programming","Networking","DSA","Linux"],
                "Country":"Europe",
                "City":"Madrid",
                "Address":"55, Gold-cost area, Madrid. SP-1001"}
        
print(student_dict.keys())

#4.Get the length of the student dictionary
print("This Student Details Length is:",len(student_dict))
#-> Bonus Task:
for key, value in student_dict.items():
    print(f"The Student {key} is {value}. " )

#5.Get the value of skills and check the data type, it should be a list
print(student_dict.get("Skills"))
# print(type(student_dict.values,"Skiils"))
print(type(student_dict.get("Skills")))

#6.Modify the skills values by adding one or two skills
# Add single item
student_dict["Skills"].append("Cryptography")
student_dict["Skills"].extend(["Cloud Computing","IoT"])
print(student_dict)

#7.Get the dictionary keys as a list
key_lst = list(student_dict.keys())
print(key_lst)

#8.Get the dictionary values as a list
value_lst = list(student_dict.values())
print(value_lst)

#9.Change the dictionary to a list of tuples using items() method
dic_lst = list(student_dict.items())
print(dic_lst)

#10.Delete one of the items in the dictionary
del student_dict["Address"]
print(student_dict)

#11.Delete one of the dictionaries
del student_dict