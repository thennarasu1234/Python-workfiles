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


# sort
list_2=["Nirmal","ajay","thennarasu"]
list_2.sort(reverse=True)
list_2
# reverse
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

# remove

list_2 = [1,2,3,4]
list_2.remove(3)
print(list_2)


