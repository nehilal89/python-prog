# Interesting things about python

mylist = [1,2,3,2,5,1]

def length (xl):
    count=0
    for _ in xl:
        count=count+1
    return count


print(length(mylist))
print(length([ ]))
