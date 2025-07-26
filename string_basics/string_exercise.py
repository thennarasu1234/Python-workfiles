# 1. reverse the string using string indexing


# 2. text="   This is a tutorial   " remove the white space from the front and end of the string

string_1= "   this is a tutorial   "
print(string_1)
print(string_1.strip())


# 3. text="This is a tutoral" -> change the word tutoral to tutorial using string method

string_1="This is a tutoral"
print(string_1.replace("tutoral",""))


# 4. text="nimal" -> check the string has any numerics

text="09"
text.isalnum()


# 5. text_2="There is an apple." -> get the position of the string is

text_2="There is an is apple."
text_2.index("is",7,15)

# 6. text_3="nirmal Kuamr" -> change the uppercase char to lowercase and lowercase to uppercase

string = "nirmal kumar"
print(string.lower())
print(string.upper())

# 7. text_4="thennarasu" -> center the text with 0 and bothends then remove those 0

# 8. text_5="Impossiblem" -> remove Im from front and m from back of the string

# 9. a)text_6="_dont" b)text_6="0dont" -> check the string is a valid identifier or not

# 10. text_7="Thennarasu" -> fill the string with 0. 