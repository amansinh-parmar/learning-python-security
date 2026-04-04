l = [9,5,1,2,3,4,2,2,2]
print(l)
# l1 = [5,6,7]
l.append(7)                #'Add' the value
l.sort(reverse=False)      #'Sorting' a list
print(l)
l.reverse()                #'Reverse' the list
print(l)
print(l.index(5))          #find the "index" of the value in list
print(l.count(2))          #'Count' the value inside the list

n = l.copy()               #'Copy' list and new value inside the list
n[0] = 5
print(n)

l.insert(1,9)              #'Add new value' to specific path.
print(l)

m = [11,15,19]             #'Add new value' end of the list
# l2 = l + l1              #'Marge' the list
l.extend(m)                #'Marge' the list
print(l)

