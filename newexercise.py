# Function + Lists + Conditons
# Exercise--> Clean & Keep Long Words
# Write a function clean_long(words,min_len) that returns a new list with words that (a) are alphabetic (no digits/symbols)
# (b) length > min_len.

def clean_long(words,min_len):
    return[w for w in words
            if w.isalpha() and len(w) >= min_len]
words = ["hello","go!","ai2","python","pro"]
print(clean_long(words,4))

# Loops + Conditons + Math
# Exercise--> fizzBuzz range take two integers a and b (a<b).
# print numbers from a to b with:

# FizzBuzz---> if the number is ddivisible by both 3 and 5 ,print "FizzBuzz"
#--> If the number is divisible by 3 but not 5, print "Fizz"
#--> If the number is divisible by 5 but not 3, print "Buzz"

def FizzBuzz(a,b):
    for i in range(a,b+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz",end=",")
        elif i % 3 == 0:
            print("Fizz", end=",")
        elif i % 5 == 0:
            print("Buzz", end=",")
        else:
            print(i, end=",")
            print()

# Dictionary + Loops
# Exercise--> Inventory value filter 
# Given stock = {"pen":(price,qty),...},print items whose total value price*qty > 100
            
stock = {"pen":(10,5),"notebook":(50,3),"marker":(25,2)}
for item, (price,qty) in stock.items():
    value = price*qty
    if value >= 100:
        print
        print(f"{item} ({value})")
            
# Lists + List Comprehension + Operators
# Exercise--> Squares Not ending with 5 from a list of integers,build a new of their squares excludig those whose square ends with digit 5

nums = [5,6,7,10,15,11]
squares = [n**2 for n in nums if (n*2) % 10 != 5] 
print(squares)


# Tuples + Unpacking + Conditions
# Exercise--> Min/Max by tuple field --> You have a tuples(names.age,score).
# Print the name with highest score, and the name with lowest age.

data = [("Thenn", 19,88),("Mughi", 21,92),("Hari", 18,90)]
top_score = max(data, key=lambda x: x[2])
youngest = min(data, key=lambda x: x[1])
print(f"Top Score: {top_score[0]},youngest: {youngest[0]}")

# String + Functions + Dict
# Exercise--> Character Frequency(letter only) write a funciton letter_freq(s) that
#  returns a dict a loercase letter counts(ignore digits/spaces/symbols)

def letter_freq(s):
    freq = {}
    for ch in s.lower():
        if ch.isalpha():
            freq[ch] = freq.get(ch, 0) + 1
            return freq
        s = "Hello Python 3 !"
        print(letter_freq(s))

# Nested loop + Dict of Lists
# Exercise--> Sunjects-wise topper given marks per subjects,
# Find the top students for each subjects.

marks = {"Math": [("Ravi",85), ("Divya",92), ("Sam",76)],
         "English": [("Ravi",78), ("Divya",88), ("Sam",98)]}

for subject, records in marks.items():
    topper = max(records,key = lambda X: X[1])
# pick tuple with highest marks
    print(f"{subject} {topper[0]} ({topper[1]})")         

# Tuple + Dict + Conditons(cart validator)
# Exercise--> Validate & total bill products(tuple) and prices dict given
# ask user for a comma-separated cart like "apple:2,banana:3".
# validated:product must exits;qty muat be positive int.print per-item totoal and gtand total


products = ("apple", "banana", "orange")
prices = {"apple": 10, "banana": 5, "orange": 8}

cart = "apple:2, orange:3"   
items = [x.strip() for x in cart.split(",")]
total = 0
for item in items:
    name, qty = item.split(",")
    name, qty = name.strip(),
qty.strip()
if name in products and qty.isdigit () and int (qty) > 0:
  qty = int (qty)
  cost = prices [name] * qty
  total += cost
  print(f"{name} x{qty} = ₹{cost}")
else:
    print(f"Invalid item:{item}")
    print(f"Total = ₹{total}")


# Loops + String Methods + Slicing
# Exercise--> Palindrome sentences(cleaned) from a list of sentences, print those that are 
# palindromes after removing spaces and punctuations, case-insensitive

lines = ["Never odd or even","Hello world","Madam, I'm Adam","No lemon, no melon"]
def clean(s):
    return"".join(ch.lower() for ch in s if ch.isalnum())
for line in lines:
    if clean (line) == clean(line) [::-1]:
        print(line)

# Final challenge--> Task manager (multi-concept mini app)
# Build a task manager with menu:
# Add task (title ,priority:low/med/high)
# list all task (sorted by priority: high>med>low)
# Delete task
# Exit

tasks = []

while True:
    print("\n1) Add  2) List  3) Done  4) Delete  5) Exit")
    choice = input("> ")

    if choice == "1":     
          # Add
        title = input("Title: ")
        priority = input("Priority (low/med/high): ")
        tasks.append({"title": title, "priority": priority, "done": False})
        print("Added!")

    elif choice == "2":  
         # List
        for t in tasks:
            status = "[x]" if t["done"] else "[ ]"
            print(f"{status} ({t['priority']}) {t['title']}")

    elif choice == "3":  
         # Mark done
        title = input("Title to mark done: ")
        for t in tasks:
            if t["title"] == title:
                t["done"] = True
                print("Marked done.")
                break
        else:
            print("Task not found.")

    elif choice == "4": 
          # Delete
        title = input("Title to delete: ")
        for t in tasks:
            if t["title"] == title:
                tasks.remove(t)
                print("Deleted.")
                break
        else:
            print("Task not found.")

    elif choice == "5":   
        # Exit
        print("Goodbye")
        break

    else:
        print("Invalid choice")