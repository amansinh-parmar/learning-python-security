#==> MAP      "map(function, iterable)":
def cub(x):
    return x*x*x

print("'Map' number: ",cub(2))

# List of numbers
l = [1,2,3,4,5,6,7]
# lst = []
# for item in l:
#     lst.append(cub(item))
# print(lst)
                            # use "map" function instead of loop 
# Double each number using the map function
# lst = list((map(cub, l)))
# print(lst)
print("'Map' number: ",list(map(lambda x: x*x*x, l)))                    # One-line code

#==> FILTER    "filter(predicate, iterable)":
# def filter_function(y):
#     return y > 4

# lst = list(filter(filter_function, l))
# print(lst)
print("'Filter' number: ",list(filter(lambda y: y > 4, l)))                 # One-line code

# Get only the even numbers using the filter function
evens = filter(lambda x: x % 2 == 0, l)

# Print the even numbers
print("'Filter' even number: ",list(evens))

#==> REDUCE    "reduce(function, iterable)":
            # first comment everthing before write code for reduce

from functools import reduce

l = [1,2,3,4,5,6,7]

def mysum(x, y):
    return x + y

sum = reduce(mysum, l)
# sum = reduce(lambda x, y: x+y, l)

print("'Reduce' number: ", sum)