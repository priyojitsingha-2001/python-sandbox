# Dictionary is a data structure in python that is a ordered collection of key-value pairs
dict={
    "A":1,
    "B":2
}
print(dict)

# to get the value of a key
print(dict["A"]) # throws error if key doesn't exists
print(dict.get("A")) # gives none if key doesn't exists

# to get all the keys as a array
print(dict.keys())

# to get all the values as a array
print(dict.values())

# you can use these methods, to iterate over keys/values
for key in dict.keys():
    print(key)
for value in dict.values():
    print(value)

# The items() give output as ([(key,value),(key,value)])
print(dict.items())

# How to iterate over the keys & values parallely
for key,value in dict.items():
    print(f"The value of {key} is: {value}")
