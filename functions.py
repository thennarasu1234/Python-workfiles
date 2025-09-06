

def print_statement():
    print("Welcome to india")
    print("how are you")


print_statement()


# def - keyword for user defined function definition

def age_verifier(age:int,name:str):
    if age>18:
        print("{name}eligible to vote".format(name=name))
    else:
        print(18-age,"years remains for {name} to meet eligible criteria".format(name=name))

age_verifier(name="nk",age=17.0)



# recursive function

# for factorial

def factorial(num):
    if num==1:
        return 1
    else:
        return num*factorial(num-1)
    
"""
5*factorial(4)
4*factorial(3)
3*factorial(2)
2*factorial(1)->1
"""

factorial_result=factorial(5)
print(factorial_result)



# fibonacci series -> 0,1,1,2,3,5,8,13......



def fibonacci(n):
    if n==0:
        return 4
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
"""
fibonacci(4)->3 + fibonacci(3)->2
    |
    v
fibonacci(3)-> 2 + fibonacci(2) -> 1
    |
    v
fibonacci(2) ->1 + fibonacci(1) -> 1
    |
    v
fibonacci(1) + fibonacci(0) -> 1
    |               |
    v               v
    1               0
"""
    
fibonacci(5)


# lambda function 

# anonymous function

check=lambda x:x%2==0
print(check)
print(check(3))

# multiply two numbers

mul=lambda x,y:x*y
print(mul(30,5))


# unpacking in functions


# *args will get the input and have it as tuple
def print_num(*args):
    for i in args:
        # print(args)
        print(i)

print_num((1,2,3,"nirmal"))



# kwarg will get dict as it input
def print_num(**nirmal):
    print(nirmal)
    for i in nirmal.items():
        # print(args)
        print(i)

print_num(a=1,b=2,c=3,d=4)



# scopes and namespaces 


b=20
def check_scope():
    a=10
    print(a)
    print(b)

check_scope()
# print(a)
print(b)


# global
a=5
def check_scope():
    global a
    a=10
    print(a)

check_scope()
print(a)


# non local
a=5
def check_1():
    a=10
    print(a)
    def check_2():
        nonlocal a
        print(a)
    check_2()
    print(a)

check_1()
