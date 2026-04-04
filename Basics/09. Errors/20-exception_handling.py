#==> Avoid the program crashing, without this process and run code without throughing any error. 
'''try:
    #statements which could generate
    #exception 
except:
    #solution of generated exception'''

a = input("ENTER YOUR NUMBER: ")
print("Multiplication table of {a} is: \n")

try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except:
    print("Invalid Code...")
    # print("Sorry!! Some Error Occur")

print("Some Lines of Code")
print("End of Your Program")


#--> Example "Value Error" and "Index Error" :
try:
    num = int(input("Enter an integer: "))
    a = [9,2]
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")
except IndexError:
    print("INDEX ERROR..!!")