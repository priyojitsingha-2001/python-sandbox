# this is how we declare a function
def sum(a=0,b=0): #this is how you provide default arguments
    return a+b

# print(sum(9,10))
# print(sum(b=10,a=9)) #this is how you provide keyword arguments

def greater(a,b): #here both the argumenst are required arguments since no deafult value is present
    # this is how we use ternary opeartor in python
    # Syntax- value_if_true if condition else value_if_false
    return a if a>b else b

# print(greater(10,1000))

# we can also keep the function body of a function empty 
# to be completed later, for that we can use pass
def function():
    pass

#if you want to take an array of arguments then use *
def sum(*numbers):
    sum=0
    for i in numbers:
        sum+=i
    return sum

# print(sum(1,2,3,4,5))

