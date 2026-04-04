#-->> For "break" Statement

for i in range(14):
    if (i == 12):
        break                       #using "break" statement to stop 'for loop'
    print("7 X",(i+1),"=",7 * (i+1))
#Exit the loop and print new line.
print("Break Statement Executed..!!")

#-->> Example:
i = 1 
while True:
    print(i)
    i = i + 1
    if(i%31 == 0):
        break

#-->> Example:
for i in range(1, 101, 1):
    print(i , end=' ')
    if(i == 50):
        break
    else:
        print("Missinginpipp..!!")

print('Thank You.....')



# #-->> For "continue" Statement
for i in range(14):
    if (i == 10):
        print("Skip The Iteration!!")
        continue                    #using "continue" statement to skip the next loop Iteration
    print("7 X",(i+1),"=",7 * (i+1))

#-->> Example:
for i in [2,4,8,9,0,5]:
    if (i % 2!= 0):
        continue
    print(i)