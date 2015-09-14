# Chapter1.py
# Author: Nilu Hilal
# Date: 9/12/2015

# Create a function called 'exists' which returns true if a given
# Int 'x' exists in a given list called 'xs'
def exists(x, xs):
    return x in xs

# Create a function called exists2 which uses a for loop to do the same thing
def exists2(x, xs):
    for i in xs:
        if i == x:
            return True
    return False

# Create a function that returns the legnth of a list called 'xs'
def length(xs):
    count = 0
    for _ in xs:
        count = count + 1
    return count

# Create a function that returns a new list of elements squared in a list
# called 'xs'
def squared(xs):
    ds = []
    for i in xs:
        ds.append(i ** 2)
    return ds

# Create a function called 'myFilter' that returns a new list of elements from
# a given list called 'xs', where those elements are less then 4
def myFilter(xs):
    ts = []
    for i in xs:
        if i < 4:
            ts.append(i)
    return ts

# Create a function called 'sum2' that returns the values of a list called 'xs'
# added together
def sum2(xs):
    count = 0
    for i in xs:
        count = count + i
    return count

# Create a function called countOccurrances that returns the number of times
# a given Integer 'x' exists in a given list 'xs'
def occur(x, xs):
    count = 0
    for i in xs:
        if i == x:
            count = count + 1
    return count

# Create a function called 'sillySort' that returns a new list that is sorted
# in asecnding order from a given list 'xs'
def sillySort(xs):
    sortedList = []
    return sortedList

# Create a function 'binarySearch' that does what that exists2 function does,
# only without having to search every element in a given list called 'xs'.
# You are guarenteed that 'xs' will be a sorted list in ascending order


def main():
    xs = [2,3,4,5,10,4,4,12,15]
    print "This is the sample list", xs
    print "Exists (var=5)", exists2(5, xs)

    print "Squared", squared(xs)
    print "myFilter", myFilter(xs)
    print "sum2", sum2(xs)
    print "Occur (val=4)", occur(4,xs)
    print filter(lambda c: c == 4, xs)

if __name__ == '__main__':
    main()
