marks = [12, 56, 32, 98, 12, 45, 1, 4]


#=> Usually write this
'''index = 0
for mark in marks:
    print(mark)
    if index == 3:
        print("Jack Reacher")
    index += 1'''


#=> Instead of writting this 
'''for index, mark in enumerate(marks):
    print(mark)
    if index == 3:
        print("Jack Reacher")
print(' ')'''

#-> Example:
'''fruits = ["Apple, Mango, Banana, Cherry"]
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
    # if index == 3:
        # fruit.append("Kiwi")
        # print(index,fruit)'''

fruits = ["Apple, Mango, Banana, Cherry, Blueberry"]

for index, fruit in enumerate(fruits):
    print(fruit)
    if index == 2:
        fruits.append("Kiwi")
        print(fruits)