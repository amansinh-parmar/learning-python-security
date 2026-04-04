#==> This keyword is the syntax which always executed.
# Either it return under the function will be successfully executed or not
#  the "finally" keyword always print. 

'''try:
    #statements which could generate
    #exception 
except:
    #solution of generated exception
finally:
    #block of code which is going to 
    #execute in any situation'''

def fun1():
    try:
        l = [2, 5, 9, 8]
        print(l)
        i = int(input("Enter the index: "))
        print(l[i])
        return 1
    except:
        print("SORRY!!!!! Some errors are occurred.")
        return 0
    finally:
        print("Finally Always executed.. ")

x = fun1()

print(x)
