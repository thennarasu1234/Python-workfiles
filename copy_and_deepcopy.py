import copy

# a=[1,2,3,4,5]
# b=a
# b[1]=6
# print(a)

# id(a)
# id(b)

a=[1,2,3,4,5]
copy_1=copy.copy(a)
print(copy_1)
copy_1[1]=3
print(a)
print(copy_1)

# [
#     1,
#     2,
#     3,
#     [
#         4,
#         5,
#         6
#     ]
# ]

b=[1,2,3,[5,6,7]]
copy_2=copy.copy(b)
print(b)
print(copy_2)

copy_2[3][1]=3
print(b)
print(copy_2)

id(b[1])
id(copy_2[1])

# deep copy

copy_3=copy.deepcopy(b)
copy_3[3][1]=10
print(b)
print(copy_3)

id(b[3][1])
id(copy_3[3][1])