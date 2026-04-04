age = 28
height = 171.5
print(f'{type(age)}\nAge: {age}')
print(f'{type(height)}\nHeight: {height}')

num = 2 + 5j
# num = complex(2, 5)
# print(num)

# #==> 1) Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
#     # Enter base: 20
#     # Enter height: 10
#     # The area of the triangle is 100
# usr_base = float(input('Enter Base: '))
# usr_height = float(input('Enter Height: '))

# area = 0.5 * usr_base * usr_height
# print(f'The area of the triangle is {round(area)}\n')

# #==> 2) Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
# # Enter side a: 5
# # Enter side b: 4
# # Enter side c: 3
# # The perimeter of the triangle is 12

# a = int(input('Enter side A: '))
# b = int(input('Enter side B: '))
# c = int(input('Enter side C: '))
# perimeter = a + b + c 
# print(f'The perimeter of the triangle is {perimeter}\n')

#==> 3) Get length and width of a rectangle using prompt. Calculate its area (area = length x width)
# length = int(input('Enter Length: '))
# width = int(input('Enter Width: '))
# area = length * width
# print(f'Rectangle Area is {area}\n')

#==> 4) Get radius of a circle using prompt. Calculate the area (area = pi x r x r)
# radius = int(input('Enter Radius: '))
# pi = 3.14
# area = pi * radius * radius
# print(f'Area Radius is {area}')

#==> Exersice 5)
word1 = 'python'
word2 = 'dragon'
check = len(word1) != len(word2)
# print(f'Check: {check}')
# print(f'Python: {'on' in word1}\n')
# print(f'Dragon: {'on' in word2}\n')

#==> Exersice 6)
# sentence = 'I hope this course is not full of jargon'
# print(f'Check Jargon: {'jargon' in sentence}')

# #==> Exersice 7)
# x ='5'
# y =5

# if x != y:
#     print('Wrong')
# else:
#     print('False')

# #==> Exersice 8)
# sample  = 9.8
# print(round(sample))

# #==> 9) Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
# usr_hour = int(input('Enter hours: '))
# usr_rate = int(input('Enter rate per hour:'))
# weekly_earning = usr_hour * usr_rate

# print(f'Your weekly earning is {weekly_earning}')

# #==> 10) Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
# usr_age = int(input('Enter number of years you have lived:'))

# seconds_year = 365 * 24 * 60 * 60
# hours_year = 365 * 24 * 60
# day_year = 365 * 24 

# total_num = seconds_year * usr_age
# hours_num = hours_year * usr_age
# day_num = day_year * usr_age

# print(f'You have lived for {total_num} seconds.\n') 
# print(f'You have lived for {hours_num} hours.\n') 
# print(f'You have lived for {day_num} days.\n') 


#==> 11) Write a Python script that displays the following table
print('\n')
print(1, 1**0, 1**1, 1**2, 1**3)
print(2, 2**0, 2**1, 2**2, 2**3)
print(3, 3**0, 3**1, 3**2, 3**3)
print(4, 4**0, 4**1, 4**2, 4**3)
print(5, 5**0, 5**1, 5**2, 5**3)

print('\n')
for i in range(1, 6):
    print(f"{i} {i**0} {i**1} {i**2} {i**3}")