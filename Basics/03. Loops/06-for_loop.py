# -->> NOTE: "for loop" is most using data type in Programming World. 

# --> Example Task 1:
# Iteration Over a String:

name = 'Jacka'

for i in name:
    print(i)
    # if (i == 'a'):
        # print("This new line statement which print after using a letter.")

# --> Example Task 2:
# Iteration Over a list:

colors = ['Red', 'Yellow', 'Blue', "Purple", "Green"]
for color in colors:
    print(color)

    for i in color:
        print(i)


# --> Example Task 3:
# Range data type: "range()"  

for k in range(7):
    print(k)                    # use only k variable print the range of 0 to 1 less than your range
    print(k + 1)                    # use k + 1 variable print the range of 1 to your range

for k in range(1, 7):
    print(k)                     #-> print - 0,1,1,2,2,3,3,4,4,5,5,6,6
    print(' ')
    print(k + 1)                 #-> print - 2,3,4,5,6,7


# --> Example Task 4:
# -> Use third perameter and check the output.
for a in range(3, 30, 7):
    print(a)                                    #Third perameter work to add the amount in first perameter, It will run for second perameter.
    print(a + 1)
