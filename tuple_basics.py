# tuple indexed,ordered,immutable,allows duplicate

tuple_1=()
tuple_2=tuple()

tuple_3=(1,2,3,2,(2,3,4,3))

# ordered
# indexed
tuple_3[1]
tuple_3[1]=5 #it returns error

dir(tuple_3)

# 'count', 'index'

tuple_3[4].count(3)

tuple_3.index(3)