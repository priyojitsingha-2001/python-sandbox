# the elements of tuple can not be changed
# insert append tuple[index] not possible in tuple
tuple =(1,2,3)
print(tuple)

# check the length
print(len(tuple))

# print the elements of tuple
for i in range(len(tuple)):
    print(tuple[i])

# to get the first occurence of the given element
print(tuple.index(1))

# count the occurence of an element in tuple
num=(0,0,1,2,3,3,3,4,5)
print(num.count(3))

# to get the first occurence of the given element in a range
# syntax - tuple.index(element,start,end)
print(num.index(3,0,7))

# to join two tuples
tuple1=(1,2,3)
tuple2=(4,5,6)
tuple3=tuple1+tuple2
print(tuple3)





