import time

timestamp = time.strftime("%H:%M:%S")
print(timestamp)
# print(int(timestamp))

timestamp = int(time.strftime("%H"))            #->Note: Using "int" data type to write proper numbers.
print(timestamp)

timestamp = time.strftime("%M")
print(timestamp)

timestamp = time.strftime("%S")
print(timestamp)