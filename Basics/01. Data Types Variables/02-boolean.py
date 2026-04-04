x = 'hello'
y = 20

print(bool(x))
print(bool(y))

print()

a = bool("abc")
print(a)
print(type(a))

b = bool(12.25)
print(b)
print(type(b))

c = bool(["apple", "cherry", "banana"])
print(c)
print(type(c))


#==> Note: bin() and complex 
print(bin(5))
print(int('0b101', 2))