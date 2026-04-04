# --> Slicing ('variable name[])
x = 'Welcome to learning Python.'
print(x)

print(x[2:8])
print(x[:7])

#--> Negative Indexing: 
y = 'Hey, Welcome to PYTHON.'
print(y[-7:-1])

# --> Upper Case "Upper()"
a = "Hello Python Learner."
print(a.upper())

# --> Lowere Case "lower()"
b = "Hello Python Learner."
print(b.lower())

# --> Remove Whitespace "strip()"
a = " Hello, Python Learner..!! "
print(a)
print(a.strip())

#--> Replace String "replace()"
a = " Hello, Python Learner..!! "
print(a.replace('Learner', 'Coder'))

# --> Split String "split()"
a = " Hello, Python Learner..!! "
print(a.split(','))

# --> Capitalize String "capitalize()"
a = "hello, Python Learner..!!"
print(a.capitalize())

# --> Center String "center()"
a = " Hello, Python Learner..!! "
# print(len(a))
print(a.center(50))
# print(len(a.center(50)))
# print(a.center(50, "."))

# --> Count String "count()"
a = " Hello, Python Learner..!! "
b = a.capitalize()
print(b.count("l"))

# --> End STring "endswith()"
a1 = "Welcome to Python Learning Series !!"
print(a1.endswith("."))
print(a1.endswith("to", 4, 10))

# --> Find String "find()"
name = "He's name is Jack. He is hard working person."
print(name.find("Apex"))

# --> Index finding String "index()"
name = "He's name is Jack. He is hard working person."
print(name.index("Jack"))

# --> To check does this String is alphabet or numeric "isalnum()"
a1 = "WelcomeToPythonLearningSeries"
print(a1.isalnum())

# --> To check does this String is Aplhabet "isalpha()"
a1 = "WelcomeToPythonLearningSeries"
print(a1.isalpha())

# --> To check does this String is lower alphabets or not "islower()"
a1 = "Welcome to Python Learning Series !!"
# a1 = "now, is it right?"
print(a1.islower())

# --> To check does all values are Stringa and then print. "isprintable()"
a1 = "Welcome to Python Learning Series !!"
print(a1.isprintable())

# --> To check this String have white sopace(space,tab). "isspace()"
str1 = "        "       #using Spacebar
print(str1.isspace())
str2 = "        "       #using Tab
print(str2.isspace())

# --> To check does this Title in Upper letter or not. "istitle()"
a1 = "World Health Oraganization"
a2 = "Welcome to Python Learning Series !!"
print(a1.istitle())
print(a2.istitle())

# --> To check all alphabets are in Upper letter. "isupper()"
name = "WELCOME TO, PYTHON. "
print(name.isupper())

# --> To check does the first world or letter is it Right or Wrong. "startswith()"
a2 = "Welcome to Python Learning Series !!"
print(a2.startswith("Welcome"))

# --> Change the font "Upper to Lower" and "Lower to Upper". "swapcase()"
a2 = "Welcome to Python Learning Series !!"
name = "WELCOME TO, PYTHON."
a1 = "now, is it right?"
print(a1.swapcase())
print(a2.swapcase())
print(name.swapcase())

# --> Converting into title font. "title()"
a1 = "welcome to, python learning series. it's a right direction."
print(a1.title())
