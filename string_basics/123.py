# capitalize() method in python
string = "my name is thenn"
print(string.capitalize())


#casefold() method in python

str_1 = "My name is THENN"
print(str.casefold())

#center() method in python

str = "THENN"
print(str.center(20,"#"))


#count()method in python

str = "This is thenn. This is another thenn."
print(str.count("thenn,6,24"))

#find() method in python

str = "This is first text. This is second text"
print(str.find("text", 20, 40))

# endswith() method in python

str = "This is demo text. This is demo text2"
print(str.endswith("text2"))

#expandtabs() method in python

str = "D\te\tm\to\t"
print(str.expandtabs())
print(str.expandtabs(2))

#index() method in python

str = "This is first text"
print(str.index('i'))

#isalnum() method in python

str = "Thennarasu2005"
print(str.isalnum())

#isalpha() method in python

str = "Thennarasu"
print(str.isalpha())

#isdecimal() method in python

str = "44"
print(str.isdecimal())

# isidentifier() method in python

str = "thenn33"
print(str.isidentifier())

#islower() method of python

str = "my name is thenn"
print(str.islower())

# isnumeric() method is python

str = "1234"
print(str.isnumeric())

str = "87868"
print(str.isnumeric())

# isprintable() method in python

str = "sylvesteer"
print(str.isprintable())

# isspace() method in python

str = "   "
print(str.isspace())

# istitle() method in python

str = "Amit"
print(str.istitle())

# isupper() method in python

str = "MARK RUFFALO "
print(str.isupper())

# join() method in python

str = {"Main", "Purpose", "Thing"}

sep = "&&"

print = (sep.join(str))

# lower() method of python

str_1 = "The Walking Dead"
print(str_1.lower())

# lstrip() method in python

str = "######STRANGER THINGS"

print(str . lstrip("#"))

# replace() method in python

str_3 = "This is demo. This is another demo"
print(str_3.replace("demo","text", 3))

str_4 = "This is our example"
print(str_4.replace("example", "demo"))

#rfind() method in python

str_3 = "This is demo. This is another demo"
print(str_3.rfind("demo"))

# rindex() method in python

str_4 = "This is test. This is another test"
print(str_4.rindex("test"))


#rjust() method in python

str = "Amercian Vandal"
print(str.rjust(25,"A"))


#rsplit() method in python

str = "Football, Archery, Cricket, Squash, Hockey, Volleyball"
print(str.rsplit(",",2))

# rstrip() method in python

str = "STRANGER THINGS#####"
print(str.rstrip("#"))

# split() method in python

str = "One##Two##Three##Four"
print(str.split("##",1))

#splitlines() method in pyton

str = "One\nTwo\nThree\nFour"
print(str.splitlines(False))