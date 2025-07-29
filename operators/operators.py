a=20
b=15
print(a+b)

# Arithmetic Operators
# +,-,*,/,//,%,**

a =15
b =10
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a**b)
print(a%b)

# Assignment Operators
# =,+=,-=,*=,/=,%=,//=,**=,|=,^=,>>=,<<=

# = (simple Assignment)

x = 10
print(x)

# += (Add and Design)

x = 5
x += 3 
print(x)

# -= (Subtract and Assign)

x = 10
x -= 4 
print(x)

# *= (Multiple and Assign)

x = 6
x *= 2
print(x)

# /= (Divide and Assign)

x = 12
x = 12/3
print(x)

# Comparison Operators
#  == , != , > , < , >= , <=

# == (Equal operator)
a=15
b=20
print(a==b)

# != (Not equal Operator)
a=25
b=25
print(a!=b)

# > (Greater Operator)
a=30
b=25
print(a>b)

# < (Less than operator)
a=30
b=25
print(a<b)

# >= (Greater than are equal to)
a=25
b=25
print(a>=b)

# <= (Less than are equal)
a=30
b=25
print(a<=b)

# Logical Operators

# and, or, not

# and (Logical Operators)

# A  B  A and B
# T  T     T
# T  F     F
# F  T     F
# F  F     F

print(10<30 and 20<40) # True and True
print(10>30 and 20<40) #False and True

# or (Logical Operators)

# A  B  A or B
# T  T    T
# T  F    T
# F  T    T
# F  F    F

print(10>30 or 20<30)  # False or True
print(10<30 or 20>30)  # True or False

# not (Logical Operators)

# It inverse the truth value of an operator

a=True
print(not(a))


# Identity Operators

# is, is not

# is (Identity operators)
a=10
b=10
print(a is b)

# is not (Identity Operators)
a=10
b=10
print(a is not b)

# string (Identity Operators)

# is 
a = "Sachin"
b = "Sachin"
print(a is b)

# is not
a = "Sachin"
b = "Sachin"
print(a is not b)

# Membership Operators

# in, not in

# in (Memebership Operator)

str1 = "Thenn Arasu"
list1 = ['a','b',10,20]

print("Th" in str1)

# not in () (Membership Operartor)

str1 = "Thenn Arasu"
list1 = ['a','b',10,20]

print("su" not in str1)


# Bitwise Opeerator  ( Bitwise Operator Work in Binary Operator)

# &, |, ~, ^, <<, >>

# ---> (&) (Bitwise AND oprartor)
# Bitwise AND operator returns 1 if both the bits are 1, otherwise it returns 0.

#  X  Y   X&Y
#  0  0    0
#  0  1    0
#  1  0    1
#  1  1    1

a = 10
b = 6

print(a&b)

# --->(|) Bitwise OR operator
# bitwise OR operator return 1 if any of the bit is 1, otherwise if returns

#  X  Y   X/Y
#  0  0    0
#  0  1    1
#  1  0    1
#  1  1    1

a = 10
b = 6

print(a|b)

# ---> (~) Bitwise NOT Operator inverts the given bits
#  It is a Unary Operator

#  X  ~X
#  0   1
#  1   0

a = 10
print(~a)

# ---> (^) Bitwise XOR operator - carot - return 1, only if the two input bits 
# otherwise it returns 0.

#XOR

#  X   Y   X^Y
#  0   0    0
#  0   1    1
#  1   0    1
#  1   1    0

x = 12
y = 10
print(x^y)

# ---> (<<) Bitwise lift shift operator
# Shift the bits of a binary number towwards the left 
# Y << n shifts the binary representation of integer Y by n positions to the left
# Y << n is as similar as multiplying the integer Y with 2**n.

print(12<<1)
print(12<<2)

# ---> (>>) Bitwise Right shift Operator
# Shift the bits of a Binary number towards thr right 
# Y >> n shifts the binary representation of integer Y by n position to the right
# Y >> n is as similar as dividing the integer Y 2**n.

print(12>>1)
print(12>>2)