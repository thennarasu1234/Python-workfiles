# pack

a=[1,2,3,4,5]#pack

#unpacking
b,c,d,e,g=a
print(a)
print(b)
print(c)
print(d)
print(e)

# packing it, converts to tuple
a=1,2,3,4,5
print(a)

b,c,*d,e=a
print(a)
print(b)
print(c)
print(d)
print(e)
