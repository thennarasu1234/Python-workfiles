# I/O
# input 

option=int(input("Enter what operation to do:\n1.ADD\n2.Sub\n3.multiplication\n4.Division\nChoose the option:"))
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


# list exercise:

nums=[10,20,30,40]

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

# multiplication table

num=5
n=1
while n<=10:
    print("{}*{}={}".format(n,num,n*num))
    n+=1