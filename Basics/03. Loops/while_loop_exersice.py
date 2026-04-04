# =========== Exersice 1 =========== 
print('Exersice 1:\n==> Iterate 0 to 10 using for loop, do the same using while loop.\n')
i = 0
while i < 10:
    print(i)
    i+=1

# =========== Exersice 2 =========== 
print('\nExersice 2:\n==> Iterate 10 to 0 using for loop, do the same using while loop.\n')
i = 10
while i >= 0:
    print(i)
    i-=1

# =========== Exersice 3 =========== 
print('\nExersice 3:\n==> Write a loop that makes seven calls to print(), so we get on the output the following triangle:\n')
for i in range(1, 8):
    print(f'#'* i)

# =========== Exersice 4 =========== 
print('\nExersice 4:\n==> Use nested loops to create the following:\n')
for i in range(8):
    for j in range(8):
        print('#', end='')
    print()

# =========== Exersice 5 =========== 
print('\nExersice 5:\n==> Print the following pattern:')
for i in range(1, 11):
    print(f'{i} x {i} = {i*i}')


# =========== Exersice 6 =========== 
print("\nExersice 6:\n==> Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.\n")
py_list = ['Python', 'Numpy','Pandas','Django', 'Flask']

for i in py_list:
    print(i)


# =========== Exersice 7 =========== 
# print('\nExersice 7:\n==> Use for loop to iterate from 0 to 100 and print only even numbers\n')
# for num in range(0, 100, 2):
#     print(num)

# =========== Exersice 8 =========== 
# print('\nExersice 8:\n==> Use for loop to iterate from 0 to 100 and print only odd numbers\n')
# for num in range(0, 101):
#     if num % 2 != 0:
#         print(num)
 

# =========== Exersice 9 =========== 
print('\nExersice 9:\n==> Use for loop to iterate from 0 to 100 and print the sum of all numbers.\n' )
total = 0
for num in range(0, 101):
    total += num

print(f'The sum of all numbers is {total}')


# =========== Exersice 10 =========== 
print('\nExersice 10:\n==> Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.\n')

# Initialize sum
sum_even = 0
sum_odd = 0

# Loop through 0 to 100
for num in range(0, 101):
    if num % 2 == 0:
        sum_even += num
    else:
        sum_odd += num

print(f'Total of all even numbers is {sum_even}')
print(f'Total of all odd numbers is {sum_odd}')