# -->> Note: "While Condition" often use for "Compelex Conditions".
''' 
# i = 0
i = int(input("Enter the number: "))

while (i<=30):
    i = int(input("Enter the number: "))
    print(i)
    # i = i + 1                                         # For "Ascending Order"

print('Done with the loop.')
'''

# count = 7

# while count > 0:
#     print(count)
#     count = count - 1                                     # For "Descending Order"


# -->>Note: When while loop condition becomes a false, It break the loop and executed the 'else' statement.
# 
count = 5

while (count > 5):
    print(count)
    count = count - 1
else:
    print("I am insider else.")


# -->>Note: Do while{ }
''' 
do {
    #loop body.
}while(condition)
'''