#-->> Practice Task: 1
'''Declare an empty list'''
lst = []
print(lst)
print(type(lst))

#-->> Practice Task: 2
'''Declare a list with more than 5 items'''
lst = ['Apex', 'Alexa', 5, 9.4, True]
print(lst)

# Find the length of your list
print(len(lst))

# Get the first item, the middle item and the last item of the list
lst = ['Apex', 'Alexa', 5, 9.4, True]
print(lst[0])
print(lst[2])
print(lst[4])

#-->> Practice Task: 3
'''Declare a list called mixed_data_types, put 
your(name, age, height, marital status, address)'''
mixed_data_types = ['Jack', 26, 170, 'Single', 'India']
print(mixed_data_types)

#-->> Practice Task: 4
'''Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.'''
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle','Amazon']
print(it_companies)

# Print the number of companies in the list
print(f"IT Comapnies List is: ", len(it_companies))

# Print the first, middle and last company
print(it_companies[0])
print(it_companies[3])
print(it_companies[6])

# Print the list after modifying one of the companies
it_companies[4] = 'NVIDIA'
print(it_companies)

# Add an IT company to it_companies
it_companies.append('IT Company') 
print(it_companies)

# Insert an IT company in the middle of the companies list
it_companies.insert(4,'IT Company')
it_companies[4] = it_companies[4].upper()
print(it_companies)

# Join the it_companies with a string '#;  '
result = '#, '.join(it_companies)
print(result)

# Check if a certain company exists in the it_companies list.
comapny_to_check = 'Google'

if comapny_to_check in it_companies:
    print(f"{comapny_to_check} exists in the list.")
else:
    print(f"{comapny_to_check} does not exists in the list.")

# Sort the list using sort() method
it_companies.sort(reverse=True)
print(it_companies)

# Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# Slice out the first 3 companies from the list
print(it_companies[:3])

# Slice out the last 3 companies from the list
print(it_companies[5:])

# Slice out the middle IT company or companies from the list
print(it_companies[3:5])

# Remove the first IT company from the list
del it_companies[0]
# it_companies.pop(0)
print(it_companies)

# Remove the middle IT company or companies from the list
del it_companies[4]
print(it_companies)

# Remove the last IT company from the list
# it_companies.pop()
del it_companies[-1]
print(it_companies)

# Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# Destroy the IT companies list
del it_companies

#--> Practice Task: 5
# Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

full_stack = front_end + back_end
print(full_stack)

# Copy the joined list and assign it to a variable full_stack, 
# then insert Python and SQL after Redux

full_stack.insert(5, 'Python')
full_stack.insert(6, 'MYSQL')

print(full_stack)

#-->> Practice Task: 6

# The following is a list of 10 students ages:
'''1.Sort the list and find the min and max age
2.Add the min age and the max age again to the list
3.Find the median age (one middle item or two middle items divided by two)
4.Find the average age (sum of all items divided by their number )
5.Find the range of the ages (max minus min)
6.Compare the value of (min - average) and (max - average), use abs() method'''

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print(ages)
# 2
ages.sort()
num_students = len(ages)
# 3
if num_students % 2 != 0:
    median_age = ages[num_students // 2]
else:
    median_age = (ages[num_students // 2 - 1] + ages[num_students // 2]) / 2
    
print(median_age)
# 4
# Find the sum of all ages
total_age = sum(ages)
# Find the number of students (length of the list)
num_students = len(ages)
# Calculate the average age
average_age = total_age / num_students
print(f"Average age is: ",average_age)
# 5
max_age = max(ages)
min_age = min(ages)
avg_age = max_age - min_age
print(avg_age)

# 6
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Find the sum of all ages and the number of students
total_age = sum(ages)
num_students = len(ages)

# Calculate the average age
average_age = total_age / num_students

# Find the maximum and minimum ages
max_age = max(ages)
min_age = min(ages)

# Calculate the absolute differences
abs_diff_min = abs(min_age - average_age)
abs_diff_max = abs(max_age - average_age)

# Compare the two absolute differences
print(f"Absolute difference between min and average: {abs_diff_min}")
print(f"Absolute difference between max and average: {abs_diff_max}")

if abs_diff_min > abs_diff_max:
    print("The difference between min and average is greater.")
elif abs_diff_max > abs_diff_min:
    print("The difference between max and average is greater.")
else:
    print("The differences are equal.")

#-->> Practice Task: 7
'''Divide the countries list into two equal lists if it is even if not one more country for the first half.'''

countries = ['USA', "Canada", "Mexico", "Brazil", "Argentina", "Germany", "France", "Italy", "UK", "Australia"]

half = len(countries) // 2

if len(countries) % 2 != 0:
    first_half = countries[:half + 1]
    second_half = countries[half + 1:]
else:
    first_half = countries[:half]
    second_half = countries[half:]

print("First Half: ", first_half)
print("Second Half: ",second_half)
    