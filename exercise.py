# I/O
# input 

option=int(input("Enter what operation to do:\n1.ADD\n2.Sub\n3.multipli" \
"cation\n4.Division\nChoose the option:"))
# print(object)
num1=int(input("Enter num 1"))
num2=int(input("Enter num 2"))

if option==1:
    print(num1+num2)
elif option==2:
    print(num1-num2)
elif option==3:
    print(num1*num2)
elif option==4:
    print(num1/num2)
else:
    print("Enter a valid option")


# tuple

tuple_1=(1,2,3,4,5,6)
max(tuple_1)
min(tuple_1)

max=tuple_1[0]
for i in tuple_1:
    if i>max:
        max=i
        print(max)
print(max)

tuple_1.count(5)

list = [10,20,30,40,50,60,70,80,90]
dict_1={"nirmal":[10,20,30],"thenn":[40,50,60],"hari":[70,80,90]}
dict_1.update({"nirmal":[20,67,90]})
dict_1["ajay"]=[10]
dict_1["ragu"]=[5]
dict_1
dir({})


# list method
# --->create a list of 5 fruits
fruits = ["apple","mango","banana","orange","grapes"]

print("original list:",fruits)

# add one fruit to the end
# append() ---> add a single element

fruits.append("pineapple")
print("after adding a fruit:",fruits)

# remove one fruit from the list

fruits.remove("banana")
print("after removing a fruit:",fruits)

# sort the list in alphabetical order 

fruits.sort()
print("sorted list:",fruits) 

# Dictionary
# create a dictionary of 3 students with their marks 

students = {"thenn":90,"mughi":95,"hari":98}
print("initial dictionary:",students)

# add one more students

students["ashvanth"] = 99
print("\nafter addding ashvanth:",students)

# update a student's mark (mughi's mark updated)

students["mughi"] = 96
print("\nafter updating mughi's mark:",students)

# remove a students

del students["thenn"]
print("\nafter removing thenn:",students)

# ---> create two set of numbers

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

print("set1:",set1)
print("set2:",set2)

#union
#union----> it combain unique element

print("union:",set1.union(set2))

#intersection
# ----> finding common element
print("intersection:",set1.intersection(set2))

#difference

print("difference (set1 - set2):",set1.difference(set2))
print("difference (set2 - set1):",set2.difference(set1))


# conditions
#----> odd or even
num = int(input("enter a number:"))
if num % 2 == 0:
     print(num, "12 is even")
else:
    print(num, "7 is odd")

# voting eligibility

age = int (input("enter your age:"))    
print("eligible" if age >= 18 else "not eligible")

# positive,negative or zero

num = int (input("enter a number:"))
print("positive" if num > 0 else "negative" if num < 0 else "zero")

# loops
# sum of numbers use a loop to calculate 1 to 10

total = sum(range(1,11))
print("sum:",total)

# multiplication table 
# using while loop

n = int (input("enter a number:"))
i = 1
while i <= 10:
    print(f"{n} * {i} = {n*i}")
    i += 1

# print even number
# for loop

for i in range(2,21,2):
    print(i,end=" ")

# nested loop & nested conditions

# pattern printing using method loops

rows = 4
for i in range(1,rows + 1):
    for j in range(i):
        print("*", end="")
        print()

# prime numbers between 1-50
# prime number using nested loop

for num in range (2,51):
    is_prime = True
    for i in range (2, int (num**0.5)+1):
        if num % i == 0:
            is_prime = False
            break
        if is_prime:
            print(num, end=" ")

# student grades using nested conditions
# float----> represent the data

marks1 = float(input("enter marks for subject 1:"))
marks2 = float(input("enter marks for subject 2:"))
marks3 = float(input("enter marks for subject 3:"))

# calculate the average
average = (marks1 + marks2 + marks3) / 3

if average >= 90:
    grade = "a"
elif average >= 75:
    grade = "b"
elif average >= 50:
    grade = "c"
else:
    grade = "fail"
    print(f"average:{average},grade:{grade}")
    
from inv import clone_items,normalize,restock
raw = ({"name":"   apple","qty":"3"}, {"name":"banana  ","qty":"12"}, {"name":"oRange","qty":"0"})
clean=normalize(*raw)
copy1 = clone_items(clean)              # shallow
print(copy1)
copy2 = clone_items(clean, deep=True)   # deep
print(copy2)
print(restock(copy2))  # {"Apple":7, "Banana":0, "Orange":10}



