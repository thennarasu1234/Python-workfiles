# indexed ,ordered,mutable,allows duplicate

list_1=[]
list_1=list()

list_1=[1,2,3,4,5,6]
# index 0 to n-1
list_1[0]
#mutable
list_1[2]=5
list_1
# allows duplicate
list_1.append("nirmal")
list_1
list_1.pop()
list_1


# 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
dir(list_1)


# ---> sort
# ---> sort the function ascending order

list_2=["Nirmal","ajay","thennarasu"]
list_2.sort(reverse=True)
list_2

# ---> reverse
# ---> reverse the list in the place
list_2.reverse()
list_2

list_3=[1,2,3,4,"Nirmal"]
list_3.reverse()
list_3


# 1d
list_4=[1,2,3,4,5]
list_4[1]

# 2d
list_5=[1,2,3,[4,5,6]]
list_5[3][1]

# 3d
list_6=[1,2,3,[2,3,4,[5,6,7]]]
list_6[3][3][2]
 

 # ---> copy
 # ---> A list of copy()  creates a new element
 # ---> But copy referes the element, if the element are mutable 
 # ---> Changes will affeect both side

list_1 = [1,2,3,4,5,6]
print(list_1)

list_2 = list_1.copy()
print(list_2)

# ---> index
# ---> the element index() access the first element

list_4 = ["thennarasu","lufy","lucky","john","monster","vishal"]
print(list_4)

print(list_4[1:2])
print(list_4[2:5])

list_5 = ["1","2","3","4"]
print(list_5)

print(list_5[1:2])
print(list_5[2:5])

# ---> remove
# ---> the element remove() , it remove the element in the list

list_6 = ["hari","mughi","thenn","aghi"]
list_6.remove("aghi")
print(list_6)

