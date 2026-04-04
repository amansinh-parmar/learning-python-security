it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

it_companies.add('Twitter')
it_companies.update(['Oneplus', 'Asus', 'Tata', 'Relince'])
print(type(it_companies))
# print(f'Sets: \n{it_companies}\n')

# it_companies.remove('Meta')
# print(it_companies, '\n')

it_companies.discard('Meta')
print(it_companies, '\n')


A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# print(A)
# print(B)
# print(f'Whole Set: \n{A.union(B)}')
# print(f'Intersection Set: \n{A.intersection(B)}')
# print(f'Issubset Set: \n{A.issubset(B)}')
# print(f'DisJoint Set: \n{A.isdisjoint(B)}')
# print(f'A with B: \n {A | B}\n')
# print(f'B with A: \n {B | A}\n')
# print(f'Symmetric Difference:\n{A.symmetric_difference(B)}')

del A, B
# print(A, B)

age = [22, 19, 24, 25, 26, 24, 25, 24]
print(f'Age List Length: {len(age)}')
age_set=set(age)
print(f'Age Set Length: {len(age_set)}')
# print(type(age_set))
print(f'Age Set:\n{age_set}\n')
print(f'Age Tuple:\n{tuple(age)}\n')
print(f'Age List:\n{age}\n')


# sentence  = {'I', 'am', 'a','teacher', 'and','I', 'love', 'to', 'inspire', 'and', 'teach', 'people'}
sentence = 'I am a teacher and I love to inspire and teach people'

words = sentence.lower().replace('.', '').split()
unique_word = set(words)

print(f'Unique Words:\n {unique_word}\n')
print(f'Number of unique word:\n{len(unique_word)}\n')

# print(f'Sentence:\n{sentence}')