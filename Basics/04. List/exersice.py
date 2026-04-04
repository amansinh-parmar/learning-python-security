# Exersice 1
print("Declare an empty list")
my_dict = []
print(my_dict)

# Exersice 2
# print('Declare a list with more than 5 items')
# items = ['laptop', 'keyboard', 'mobile', 'computer', 'printer', 'internet']
# print(f'Total items in List is {len(items)}\n')
# print(items,'\n')
# print(items[0], items[3], items[-1])


# Exersice 3
mixed_data_type = [
    'Apex',
    28,
    170,
    'Single',
    'Surat'
]

print(mixed_data_type)


it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

print(len(it_companies))
print(it_companies[0], it_companies[3], it_companies[-1])

it_companies.append('OnePlus')
print(it_companies,'\n')

it_companies.insert(4,'Asus')
# it_companies[7] = it_companies[7].upper()
# print(it_companies,'\n')
# result = '#; '.join(it_companies)
# print(result, '\n')

# print('Samsung' in it_companies)
# print(sorted(it_companies))

# Reverse Order
it_companies.sort(reverse=True)
# print(it_companies)

# print(it_companies[:3])
# print(it_companies[-3:])
# print(it_companies[3:5])

# it_companies.pop(0)
# it_companies.pop(5)
# it_companies.pop(-1)
# it_companies.clear()
# del it_companies
# print(it_companies)


#==> Exersice 2 
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

full_stack = front_end + back_end
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
# print(full_stack)


ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
# print(ages[0])
# print(ages[-1])

average =  sum(ages)/len(ages)
# print(average)

min_ages = min(ages)
max_ages = max(ages)

diff_min = abs(min_ages - average)
diff_max = abs(max_ages - average)

print('Min Avg ABS : ', diff_min)
print('Max Avg ABS : ', diff_max)


countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
# print(countries[5])
print(sorted(countries))
# countries.sort(reverse=True)
# print(countries)

half_index = (len(countries) + 1) // 2

fist_half = countries[:half_index]
last_half = countries[half_index:]

# print(fist_half)
# print(last_half)

first, second, third, * scandic_countries = countries
print('First scandic countries: ', first)
print('Second scandic countries: ', second)
print('Third scandic countries: ', third)
print('Scandic countries: ', scandic_countries)
