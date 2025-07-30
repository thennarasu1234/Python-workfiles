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