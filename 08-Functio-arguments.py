# how to pass arguments
def average(a,b):
    print("the average is",(a+b)/2)

# average(a,b)

#default arguments
def average(a=9,b=5):
    print("value of a:",a)
    print("value of b:",b)
    print("the average is",(a+b)/2);
# average(7,8)
# average()

# keyword arguments
# average(b=8,a=7)

# array as arguments and splat opeartor 
def function(*numbers):
    for i in numbers:
        print(i)

# function(1,2,3,4)

# return statements in python
def sum(*numbers):
    ans=0
    for i in numbers:
        ans+=i
    return ans

print(sum(1,2,3,4))

