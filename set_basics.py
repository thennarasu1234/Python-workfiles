# unordered, not indexed ,don't allow duplicate ,mutable

# mutable in the sense new data can be inserted and value can be removed but it isn't interchange it
set_1={1,2,3}
set_1={}
type(set_1)
set_2=set()

set_1={1,2,3,4,5}
set_2={1,2,3,2,3,4}
set_2

dir(set_2)

# 'add', 'clear', 'copy', 'difference', 
# 'difference_update', 'discard', 'intersection',
# 'intersection_update', 'isdisjoint', 'issubset',
# 'issuperset', 'pop', 'remove', 'symmetric_difference', 
# 'symmetric_difference_update', 'union', 'update'

# symmetric difference
set_1={1,2,3,4}
set_2={1,2,5,6}
set_1.symmetric_difference_update(set_2)

# intersection
set_1={1,2,3,4}
set_2={1,2,5,6}

set_1.intersection(set_2)

# discard
set_1.discard(4)

# remove
set_1.remove(4)

# add

set_2 = {1,2,3,4}
set_2.add(5)
print(set_2)

# update

set_1 = {1,2,3,4}
set_2 = {3,4,5,6}
set_1.update(set_2)
print(set_1)

# pop

set_2 = {1,2,3,4}
set_3 = {3,4,5,6,7}
set_2.pop()
print(set_2)

# clear

set_1 = {1,2,3,4}
set_1.clear()
print(set_1)

# issubset

set_1 = {1,2,3}
set_2 = {1,2,3,4,5,6}
set_1.issubset(set_2)

# issuperset

set_1 = {1,2,3}
set_2 = {1,2,3,4,5,6}
set_1.issuperset(set_2)
set_1>=set_2

# union

set_2 = {1,2,3}
set_3 = {1,2,3,4,5,6}
set_2.union(set_3)
set_2|set_3

# difference

set_2 = {1,2,3}
set_3 = {1,2,3,4,5,6}
set_2.difference(set_3)
set_2-set_3
set_3-set_2

# copy

set_1 = {1,2,3,4,5}
print(set_1)

# differencce_update

set_1 = {1,2,3}
set_2 = {2,5,6}
set_1.difference_update(set_2)
print(set_1)

# intersection_Update

set_1 = {1,2,3,4}
set_2 = {2,3,5}
set_1.intersection_update(set_2)
print(set_1)

# isdisjoint

set_1 = {1,2,3,4}
set_2 = {5,6,7,8}
set_1.isdisjoint(set_2)

# symmetric difference update

set_1 = {'beast','lock','cup'}
set_2 = {'luck','cup'}
set_1.symmetric_difference_update(set_2)
print(set_1)