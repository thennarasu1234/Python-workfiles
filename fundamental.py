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

# tuples + Conditions
# Erercise----> create a tuple of 5 fruits.ask the user to enter a fruit.

fruits = ("apple", "banana", "mango", "orange", "grape")
user_fruit = input("Enter a fruit: ").lower()

if user_fruit in fruits:
    print("Yes, its available")
else:
    print("No, not available")

# String + Loop + Conditions
# Exercise----> count how many digits, letters, and special characters are in this string

text = "Welcome123@2025!"
letters = digits = specials = 0
for char in text:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1
    else:
        specials += 1
        print(f"letter:{letters},digits:{digits},specials{specials}")

# Nested loops + list + Dictionary
# Exercise----> given a list of students marks as a dictionary,calculate and print each students average


marks = {"Ravi": {"Math": 85, "English": 78, "Science": 90},"Divya": {"Math": 92, "English": 88, "Science": 95},}

for student, subjects in marks.items():
    total = 0
    count = 0
    for subject, score in subjects.items():
        total += score
        count += 1
    average = total / count
    print(f"{student} - {average:.1f}")


# Tuple + Dictionary (Mini Billing system)     
# Exercise-----> you are given a tuple of products and a dictionary with prices. ask the user for a product nme and quantity, then shoow the bill

products = ("apple","banana","orange")
prices = {"apple":10,"banana":5.,"Orange":8}  
product = input("enter product name:").lower()
quantity = int(input("enter quantity:"))
if product in products:
    total = prices[product]*quantity
    print(f"total = {total}")
else:
    print("product not available")

# Loop + String functions
# Exercise----> from a list of sentences,print those that contain the word "python"(case-insensitive),using lower() and in

lines = ["I Love Python","Coding is fun","PYTHON is powerful","Try Java"]
for line in lines:
    if "python" in line.lower():
        print(line)    
     
# Final challenge 
#---->multi-concept mini app

contacts = {}

while True:
    print("\n1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        contacts[name] = phone
        print("Contact added.")
    elif choice == "2":
        if contacts:
            for name, phone in contacts.items():
                print(f"{name} - {phone}")
        else:
            print("No contacts available.")
    elif choice == "3":
        search_name = input("Enter name to search: ")
        if search_name in contacts:
            print(f"{search_name} - {contacts[search_name]}")
        else:
            print("Contact not found.")
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice.")