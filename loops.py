# while,for 


# while true 
# for start to end 

a=1

while a<=100:
    if a%2!=0:
        print(a,end=" ")
    a+=1

for i in range(2,5):
    print(i)

list_1=["nirmal","ajay"]

for name in list_1:
    print(name)

for i in range(1,11):
    print(i)

# execise:
# list_1=[10,20,25,10]
# taget=20
# output=[]

# for i in range(3):
#     if ((list_1[i]+list_1[i+1])==taget):
#         output.append(i)
#         output.append(i+1)
#         break
# print(output)

range(10)
for i in range(0,10):
    print(i,end=" ")

for i in range(1,101):
    if (i%2==0):
        print(i)


# range-> start,stop,step

for i in range(1,100,2):
    print(i)

# pass,continue,break

# break->break the loop
# continue->skips the loop
# pass->pass the loop


# Find the max element from the list using max and without using build in function

list = [20,30,10,55]
max_element = list[0]
for num in list:
    if num > max_element:
        max_element = num
    print("maximum element")
for i in list_1:
    if i==5:
        pass
    print(i)

# count how many times each word appears in a sentences.

sentences = "apple banana apple mango banana apple"

# split sentence into words 
word = sentences.split()

# create empty dictionary 
word_count = {}

# count occurences
for word in word:
    if word in word_count:
        word_count[word] +=1
    else:
        word_count[word] = 1
        print(word_count)


# merged two dictoaries

a = {'x':1,'y':2}
b = {'y':3,'z':4}
merged=a | b
print(merged)

# merged two dictonaries

a = {'x':1,'y':2}
b = {'y':3,'z':4}
merged = a.copy()
merged.update(b)
print(merged)

# print the even number which are divisible by 4

for i in range(1,101):
    if i % 4 == 0:
        print(i)


# count how many subjects scored above 80  

marks = {"math":85,"science":72,"english":90}
count = 0
marks.values()
marks.keys()
for score in marks.values():
    if score > 80:
       count += 1
print("subjects scored above 80:",count)

# filter elements greater than a value 
# print the element in the list greater than 20

list_1 = [10,20,30,40,50] 
for num in list_1:
    if num > 20:
        print(num)

# check if item exists in list like name "banana" exists in a list of fruits

fruits = ["apple","banana","mango","orange"]
name = "banana"
if name in fruits:
    print(f"{name} exists in the list")
else:
    print(f"{name} does not exists in the list")

# make it an ascending order using loop

# Given list
numbers = [20, 30, 10, 55]

# Bubble sort using loops
for i in range(len(numbers)):
    for j in range(len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            # Swap elements
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Sorted list in ascending order:", numbers)


# Get a list of words from a single line of  input like name = "Nirmal is a boy"
# And store it word in list using string method

# split the string into words

name = "Nirmal is a boy" 

# split the string into words
words_list = name.split()

print(words_list)

# sum of 1 to 100

total = 0
for i in range(1,101):
    total += i
    print(total)

a=10
b=20
c=30

if a>b and a>c:
    print("a is greater number")
elif b>a and b>c:
    print("b is greater number")
else:
    print("c is greater number")

# nested if condition
a=40

if a>b:
    if a>c:
        print("a is greater")
    else:
        print("c is greater")
else:
    if b>c:
        print("b is greater")
    else:
        print("c is greater")

list_1=[[1,2,3],[4,5,6],[7,8,9]]

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 

n=5
for i in range(1,n+1):
    print("* "*i)


for i in range(n+1,0,-1):
    print(i)

for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

n=5
while n!=0:
    print("* "*n)
    n-=1

