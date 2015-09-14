# Interesting things about python

# --------- HELP! ------------

# ---- if statement syntax ---
# if 'statment':
# -- code
# elif 'statement2':
# -- code
# else:
# -- code
#
# The code inside the if statement must be able to boil down to
# a true or false value. If the statement evalutates to true the
# block will be performed. If it evalues to false, it will check any elifs.
# If the if statment and all elifs evaluate their statements to false then
# the else: block will be called if it was provided

# ---- for statement syntax ---
# for (temporary variable) in (collection):
# -- code
#
# The for loop iterates over a collection. For example
# [1,2,3,4,5]. For every iteration of this collection the block
# 'code' will be called each iteration with temporary variable being
# 1, then 2, then 3, then 4, then 5 in that order, each time

# ----- Creating variables ------
# Integers
# x = 5

# Doubles
# a = 2.3

# Lists
# r = [1,2,3,4,3,3,2,1]

# Dictionaries
# t = { "a" : 3, "b" : 4 }

# Functions
# def a():
#   print a
# myfunc = a

mylist = [15,2,3,2]
mylist.append(69)
print (mylist)

def length (xl):
    count=0
    for _ in xl:
        count=count+1
    return count

print(length(mylist))
print(length([ ]))

def sum(xs):
    count=0
    for i in xs:
        count=count+i
    return count

print(sum(mylist))

def mean(xs):
    return sum(xs)/len(xs)
print (mean(mylist))

#name=head
#parameter 1= list named xs
#returns 1st element in xs
def head(xs):
    if len(xs) == 0:
        raise Exception("Can't do this!")
    return xs[0]

print (head(mylist))

def last(xs):
    if len(xs) == 0:
        raise Exception("Can't do this!")
    return xs[len(xs)-1]

#print (head([]))

# a = [1,3,4,5,6,7,8,9,0]
def tail(xs):
    xs.remove(xs[0])
    return xs
print (tail(mylist))

def mymap(mapper, xs):
    acc=[]
    for i in xs:
        acc.append(mapper(i))
    return acc

def square(x):
    return x ** 2

print (mylist)
print (mymap(square, mylist))
print (mymap(lambda x: x ** 2, mylist))
