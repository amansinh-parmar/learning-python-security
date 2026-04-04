#==>> 'for loop':
for i in range(8):
    # i = i + 1
    # print(i)
    if i == 4:                            # use of 'condition'  
        break          # using "break" loop is successfully completed and "else statement doesn't print".

else:
    print("Sorry you are doing something wrong. There is no 'i'")

#-> Example: 
for x in range(5):
    print("Iteration no {} in for loop".format(x*1))
else:
    print("'else' block in loop")
print("OUT OF LOOP.")

#==>> 'while loop':
i = 0
while i<7:
    print(i)
    i = i + 1

else:
    print("Sorry no i")

