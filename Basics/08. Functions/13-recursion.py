#=> What is factorial?
# factorial(7) = 7*6*5*4*3*2*1
# factorial(6) = 6*5*4*3*2*1
# factorial(5) = 5*4*3*2*1
# factorial(5) = 5*4*3*2*1
# factorial(0) = 1

# factorial(n) = n * factorial(n - 1)

def factorial(num):
    if (num == 0 or num == 1):
        return 1
    else:
        return (num * factorial(num - 1))
    
# print(factorial(3))
# print(factorial(4))
print(factorial(5))

# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
# 5 * 4 * 3 * 2 * 1 

#=>Quick Quiz: Write a program to print the Fibbonacci Sequence:
# f(0) = 0 
# f(1) = 1
# f(2) = f(1) + f(0)
# f(n) = f(n-1) + f(n-2)

def fibonacci(n):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Recursive call for Fibonacci sequence
        return fibonacci(n-1) + fibonacci(n-2)

# Input: number of terms to print in the Fibonacci sequence
num_terms = int(input("Enter the number of terms: "))

# Print the Fibonacci sequence up to num_terms
print("Fibonacci Sequence:")
for i in range(num_terms):
    print(fibonacci(i), end=" ")

