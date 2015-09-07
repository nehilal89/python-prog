# Interesting things about python

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
