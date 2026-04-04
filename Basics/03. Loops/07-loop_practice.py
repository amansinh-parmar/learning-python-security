'''
-->>Exercise 1:
    Iterate 0 to 10 using for loop, do the same using while loop.
'''
i = 0
while i <= 10:
    print(i)
    i = i + 1
'''
-->>Exercise 2: 
Iterate 10 to 0 using for loop, do the same using while loop.
'''
i = 10
while i >= 0:
    print(i)
    i -= 1
'''
-->>Exercise 3:
    Write a loop that makes seven calls to print(), so we get on the output the following triangle:
# '''
for i in range(7):
    i = i + 1
    print("#" * i)
# '''
# -->>Exercise 4:
#     Use nested loops to create the following:
# '''
for i in range(5):  # Outer loop for rows
    for j in range(5):  # Inner loop for columns
        print('#', end=' ')  # Print '#' with a space, without moving to a new line
    print()  # After printing all columns, move to the next line
# '''
# -->>Exercise 5:
#     Print the following pattern:'''
for i in range(11):
    print(f"{i} x {i} = {i*i}")
# '''
# -->>Exericse 6:
#     Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.'''

lst =  ['Python', 'Numpy','Pandas','Django', 'Flask'] 
for item in lst:
    print(item)
# '''
# -->>Exercise 7:
#     Use for loop to iterate from 0 to 100 and print only even numbers.
# '''
for i in range(101):
    if i % 2 == 0:
        print(i)    
'''
-->>Exercise 8:
    Use for loop to iterate from 0 to 100 and print only odd numbers
'''
for i in range(101):
    if i % 2 != 0:
        print(i)
'''
-->>Exercise 9:
Use for loop to iterate from 0 to 100 and print the sum of all numbers.
# '''
total_sum = 0  # Initialize the sum variable

for i in range(101):  # Loop through numbers from 0 to 100
    total_sum += i  # Add the current number to the sum

print("The sum of all numbers from 0 to 100 is:", total_sum)  # Print the total sum
'''
-->>Exercse 10:
    Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
'''
even_sum = 0  # Initialize the sum of even numbers
odd_sum = 0   # Initialize the sum of odd numbers

for i in range(101):  # Loop through numbers from 0 to 100
    if i % 2 == 0:    # Check if the number is even
        even_sum += i  # Add the even number to even_sum
    else:
        odd_sum += i   # Add the odd number to odd_sum

print("The sum of all evens is:", even_sum)  # Print the sum of even numbers
print("The sum of all odds is:", odd_sum)    # Print the sum of odd numbers
'''
-->>Example 11:
    This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
'''
lst_fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []

for i in range(len(lst_fruits)-1, -1, -1):  # Start from the last index to the first
    reversed_fruits.append(lst_fruits[i])   # Append each item in reverse order

print(reversed_fruits)  # Print the reversed list
