# Global scope basics 
# Ecercise--> create a function cart(item) that appends to a global list CART 
# Call it 3 times and print CART
 
# Global Variable --> function can directly acces the value of a global variable without
#  any special character

CART = []
def add_to_cart(item):
    global CART          # declare we modifying global   
    CART.append(item)    # using append() to add sinngle element to end an existing
add_to_cart("apple")
add_to_cart("banana")
add_to_cart("orange")
print(CART)


# Nonlocal with closures 
# Exercise--> Write counter(start=0) that returns an inner function inc()
# which increments a hidden variable and returns it.Use nonlocal

def counter(start=0):
    value = start
    def inc():
        nonlocal value
        value += 1 
        return value
    return inc
c = counter(10)
print(c(), c(), c())

# Packing & unpacking (*args,**kwargs)
# Exercise--> Write total (*nums,rounds_to= 0) that sums any number of args and rounds to round_to decimals

def total(*nums, round_to=0):
    s = sum(nums)
    return round(s, round_to)
print(total(1,2,3.456, round_to=2))


# Exercise--> Given params = {"sep":"-","end":"!"},call print("A","B","c",**params)
# using dictionary unpacking and explain what happens

params = {"sep":"-", "end":"!"}   #--> **params unpacks into keyword args:
print("A","B","C", **params)

# Function Parameters: positonal-only /keywords-only # 
# Exercise--> Define def price(qty,/,*,tax=0.0,discount=0.0):...
# Return qty* (1 + tax)*(1-discount).
# Show that qty must be positional and tax/discount must be keywords

def price(qty,/,*,discount=0.0,tax):
    return  qty * (1+tax) * (1-discount)
print(price(10,tax=0.18,discount=0.1))


# Shallow vs Deep copy 
# Exercise--> You have = [["apple",2],[banana"]] .

import cart
cart = [["apple",2],["banana",3]]
cart_copy_shallow = cart.copy()
cart[0][1] = 5
print(cart)
print(cart_copy_shallow)

cart_copy_deep = copy.deepcopy(cart)
cart[1][1] = 10
print(cart)
print(cart_copy_deep)

# Moduoles & namespacing
# Exercise--> create a file math tools.py with:

PI = 3.14159
def circle_area(r):
    return PI * r * r
if __name__ == "__main__": 
   print("Testing circle_area(3)")


# Comprehenssions (lists/dict/set)+function
# Exercise--> 

words = ["Hello","python","WORLD","code"]
uppers = [w for w in words if w.isupper()]
titlecased = [w.title() for w in words if not w.isupper]
length_map = {w: len(w) for w in words if len(w) > 4}
first_letters = {w[0].lower() for w in words}

# Higher-order functions + nonlocal state
# Exercise--> Create maek_discounted_total(discount) returning a function
# Bill(*items) where each item is (name,price).
# Bill rememeber count of times it was called(use nonlocal) and applies discount only from the 3rd call onwards


def make_discounted_total(discount):
    count = 0  
    def bill(*items):
        nonlocal count
        count += 1
        total = sum(price for _, price in items)
        if count >= 3:   
            total *= (1 - discount)
        return total
    return bill        
b = make_discounted_total(0.1)
print(b(("pen", 10), ("book", 90)))
print(b(("bag", 500),)) 
print(b(("shoes", 1000),))        
print(b(("laptop", 2000),)) 


# Mini-project : Module + Copies + Comprehensions + args
# Exercise--> "Invnetory Toolkit"
# Create a module inv.py with:

import copy

def clone_items(items,deep=False):
    if deep==False:
        copy_1=copy.copy(items)
        return copy_1
    else:
        copy_1=copy.deepcopy(items)
        return copy_1        
    

def normalize(*record):
    return {"name":[x["name"].strip().title() for x in record],"qty":[int(y["qty"]) for y in record]}

def restock(items,target=10):
    dict_1={}
    for i in range(len(items["name"])):
        dict_1[items["name"][i]]=max(0,target-items["qty"][i])
    return dict_1
