# A lambda function is a small anonymous function without a name. 
# It is defined using the lambda keyword and has the following syntax:
# lambda arguments: expression


#==> Note: lambda function "most" use is when we use "function with an arguments":   

def appl(fx, value):
  return 6 + fx(value)

double = lambda x: x * 2
cube = lambda x: x * x * x
avg = lambda a,b, c: (a+b+c)/3


print(f"Number of Double is: {double(5)}")
print(f"Number of Cube is: {cube(2)}")
print(f"Number of Average is: {avg(3,5,10)}")

# function value "6 + lambda value" and lambda value is "2x2=4" 
# out-put is 10
print(appl(lambda x: x * x , 2))