arr=[12,11,9,1,2,3,4]
#to get the index of element use index()
print(arr.index(11))#1

#to reverse an array use the reverse method
arr.reverse()
print(arr)

#use sort method to sort the list
arr.sort()
print(arr)

#to sort in descending order use reverse=True as an argument
arr.sort(reverse=True)
print(arr)

#to copy one list to another use copy()
arr2=arr.copy()
print(arr)
print(arr2)
# this will copy all the elements of arr to arr2
# so both arrays dont have the same reference

#to expand a list by adding elements from another list, use extend()
a=[1,2,3,4,5]
b=[6,7,8]
a.extend(b)
print(a)

#but if you wanted to create a new array all together, then do this
c=a+b
print(c)