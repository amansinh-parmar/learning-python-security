# Long formation: 
'''if condition:
    result = value_if_true
else:
    result = value_if_false'''

# Sort-hand formation:
# result = value_if_true if condition else value_if_false

#==> Example
a = 330
b = 3303

print("A") if a > b else print("=") if a == b else print("B")

print(a) if a > b else print("=") if a == b else print(b)

c = 9 if a>b else 0
print(c)

