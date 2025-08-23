# loops , conditions , strings
# Exercise----> write a program that takes a list of string and prints only those start with capital letter and end with a vowel

words = ["Apple","banana,","Orange","umbrella","Elephant","Fan"]

for word in words:
    if word[0].isupper()and word[-1].lower() in 'aeiou':
        print(word)

# Arithmetic operators conditions
# Exercise----> ask user to input 3 numbers and print the largest using only if-elif-else

a = int(input("enter the first number:"))
b = int(input("enter the second number:"))
c = int(input("enter the third number:"))
if a>=b and a>=C:
    largest = a
elif b>=a and b>=c:
    largest = b
else:
    largest = c
    print("largest number is:",largest)
 

# Dictionary + string manipulation
# Exercise-----> you are given a dictionary of names and their email addresses.print all names whose ends with "@gmail.com"

email = {"Arun": "arun123@gmail.com","Meena": "meena@yahoo.com","sam": "sam@gamilcom"}
for name, email in email.items():
    if email.endswith("@gmail.com"):
     print(name)

# Lists + Loops + Operators
# Exercise-----> given a list of numbers,filter and print all even numbers whose square is greater than 100

nums = [4,10,15,20,5]
for num in nums:
    if num % 2 == 0 and num**2 > 100:
        print(num)
    


     