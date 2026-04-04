# sets
#-> Practice Task: 1
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
#1.Find the length of the set it_companies
print(len(it_companies))

#2.Add 'Twitter' to it_companies
it_companies.add("Twitter")
print(it_companies)

#3.Insert multiple IT companies at once to the set it_companies
companies = {"Wipro","Infoysis","Meta"}
it_companies.update(companies)
print(it_companies)

#4.Remove one of the companies from the set it_companies
it_companies.remove("IBM")
print(it_companies)

#5.What is the difference between remove and discard
it_companies.discard("ibm")         # Here, added remove value lower case ibm and it will not through an error. 
print(it_companies)                 
# it_companies.remove("ibm")        # However, "remove" element through an error    
# print(it_companies)

#-> Practice Task: 2
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
#1.Join A and B
# A = A.union(B)
# print(len(A),A)

#2.Find A intersection B
intersec = A.intersection(B)
print(len(intersec),intersec)

#3.Is A subset of B
subset = A.issubset(B)
print(subset)

#4.Are A and B disjoint sets
disjoint = A.isdisjoint(B)
print(disjoint)

#5.Join A with B and B with A
# Join A with B
A_union_B = A.union(B)
# Join B with A (this is equivalent to A_union_B due to commutativity)
B_union_A = B.union(A)
print("A union B:", A_union_B)
print("B union A:", B_union_A)

#6.What is the symmetric difference between A and B
symmetric = A.symmetric_difference(B)
print(symmetric)

#7.Delete the sets completely
union = A.union(B)
# del union                 # This will raise a NameError because A is deleted
print(union.clear())        # It will clear you set and make it empty
print(union)

#-> Practice Task: 3
age = [22, 19, 24, 25, 26, 24, 25, 24]
#1.Convert the ages to a set and compare the length of the list and the set, which one is bigger?
lst = list(age)
print(f"The length is:{len(lst)}\n",lst)
lst.sort()
print(lst)

age = [22, 19, 24, 25, 26, 24, 25, 24]

# Convert the list to a set
age_set = set(age)

# Compare the lengths
list_length = len(age)
set_length = len(age_set)

print("Length of the list:", list_length)
print("Length of the set:", set_length)

# Determine which is bigger
if list_length > set_length:
    print("The list is bigger.")
elif list_length < set_length:
    print("The set is bigger.")
else:
    print("The list and set are the same size.")

#2.Explain the difference between the following data types: string, list, tuple and set
str_age = str(age)              # For String
print(f"The Length of String is: {len(str_age)}\n",str_age)

list_age = list(age)            # For List
print(f"The Length of List is: {len(list_age)}\n",list_age)

tuple_age = tuple(age)          # For Tuple
print(f"The Length of Tuple is: {len(tuple_age)}\n",tuple_age)

set_age = set(age)              # For Set
print(f"The Length of Set is: {len(set_age)}\n",set_age)
'''Summary of Key Differences:
Data Type	Mutability	Ordered	Allows Duplicates	Use Case
String	Immutable	Yes	Yes	Represents text data.
List	Mutable	Yes	Yes	Ordered collection, can change during runtime.
Tuple	Immutable	Yes	Yes	Ordered, fixed-size collection.
Set	Mutable	No	No	Unordered, unique items, no duplicates.
Key Points:
Strings: Immutable and used for text.
Lists: Mutable, ordered, and can have duplicates.
Tuples: Immutable and ordered, often used for fixed collections.
Sets: Mutable, unordered, and only store unique elements.'''

#3.I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people"

# Split the sentence into words
words = sentence.split()

# Convert the list of words into a set to remove duplicates
unique_words = set(words)

# Get the number of unique words
unique_word_count = len(unique_words)

print("Number of unique words:", unique_word_count)
