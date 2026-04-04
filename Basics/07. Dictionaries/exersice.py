dog = {
    'name':'Sandy',
    'color':'White and Grey',
    'breed': 'Huskey',
    'legs': 4,
    'age': 2
}
# print(dog)


print('EXERSICE STUDENT DICTIONARY: \n')
student = {
    'first_name': 'Apex',
    'last_name':'Amanda',
    'gender':'Male',
    'age':28,
    'marital status':'Single',
    'skills':['JavaScript', 'MongoDB', 'Python', 'React'],
    'country':'India',
    'city':'Surat',
    'address':'Ghod Dod Road'
}

print(student,'\n')
print("Number of keys:", len(student), '\n')

skills_value = student['skills']
# print(f'Skills: {skills_value}\n')
# print(type(skills_value))

# Modify the skills values by adding one or two skills
skills_value.append('HTML, CSS')
# print(skills_value, '\n')
# print(student,'\n')

# Get the dictionary keys as a list
student_keys = list(student.keys())
print(f'Student Dictinory Keys: {student_keys}\n')

# Get the dictionary values as a list
student_values = list(student.values())
print(f'Student Dictionary Values: {student_values}\n')

# Change the dictionary to a list of tuples using items() method
item_tuple = list(student.items())
# print(item_tuple,'\n')

delete_item = student.pop('city')
print(delete_item, '\n')

delete_item = student.pop('address')
print(delete_item, '\n')
print(student, '\n')
