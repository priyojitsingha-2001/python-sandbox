marks=[90,78,68,80]
print(marks[0])

# in python we can also use negative index
# which counts from the back -1 means element at the end
print(marks[-2])

# to add elements at the end we use append
marks.append(30)

# to add elements at any index
marks.insert(0,100)

# to print the length of the list/array
print(len(marks))

# to check if a given element is present in the list or not
print(100 in marks)

# to empty a list we use clear method
marks.clear()
print(marks)

#list comprehension- we can create lists on the fly, either by giving expressions or from other list
# this list will store numbers from 1 to 10
arr=[i+1 for i in range(10)]
print(arr)
