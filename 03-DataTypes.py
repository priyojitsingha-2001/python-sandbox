import datetime
# Numeric Data Types


print("Numeric Data Types:")

# Integer
integer = 10
print(integer, type(integer))

# Floating-point number
float_number = 3.14159
print(float_number, type(float_number))

# Complex number
complex_number = 1 + 2j
print(complex_number, type(complex_number))

# Sequence Data Types
print("\nSequence Data Types:")

# List
numbers = [1, 2, 3, 4, 5]
print(numbers, type(numbers))

# Tuple
fruits = ("apple", "banana", "orange")
print(fruits, type(fruits))

# Range
range_object = range(10)
print(range_object, type(range_object))

# Mapping Data Types
print("\nMapping Data Types:")

# Dictionary
capitals = {"USA": "Washington D.C.", "Canada": "Ottawa", "Mexico": "Mexico City"}
print(capitals, type(capitals))

# Set
unique_numbers = {1, 2, 3, 4, 5, 4}
print(unique_numbers, type(unique_numbers))

# Frozenset
immutable_numbers = frozenset({1, 2, 3, 4, 5})
print(immutable_numbers, type(immutable_numbers))

# Boolean Data Type
print("\nBoolean Data Type:")

# Boolean value
is_true = True
print(is_true, type(is_true))

# Binary Data Types
print("\nBinary Data Types:")

# Bytes object
bytes_data = b"Hello, World!"
print(bytes_data, type(bytes_data))

# Bytearray object
mutable_bytes = bytearray(b"Hello, World!")
print(mutable_bytes, type(mutable_bytes))

# Memoryview object
memory_view = memoryview(bytes_data)
print(memory_view, type(memory_view))

# Other Data Types
print("\nOther Data Types:")

# None value
nothing = None
print(nothing, type(nothing))

# String
greeting = "Hello, Python!"
print(greeting, type(greeting))

# Datetime object
current_date = datetime.datetime.now()
print(current_date, type(current_date))

