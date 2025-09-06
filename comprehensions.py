# list set dict
# list comprehensions


# list of odd numbers
list_com_1=[x for x in range(1,101,2)]
list_com_2=[x for x in range(1,101) if x%2!=0]
print(list_com_1)

# set comprehension for list of n numbers
set_1={x for x in range(1,20)}
set_1

# dict comprehensions
dic_1={x:x**2 for x in range(1,101)}

print(dic_1[10])

