# Declare an empty set
var = set()
print(type(var))

# Initialize a set with different data types, sets store unique values(no duplicates)
var = {1, 2.5, "blue"}
print(var)

# Add an item to the set
var.add(90)
print(var)

# Update the set with multiple elements
var.update([3, 4, "green"])
print(var)

# Remove a specified element from the set
var.remove(2.5)
print(var)

# Discard a specified element from the set without raising an error if not found
var.discard("blue")
print(var)

# Pop and return an arbitrary element from the set
popped_item = var.pop()
print(popped_item)

# Clear all elements from the set
var.clear()
print(var)

# Create a shallow copy of the set
new_set = var.copy()
print(new_set)

# Union of two sets, combines the two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)

# Intersection of two sets, returns a new set with the common elements
intersection_set = set1.intersection(set2)
print(intersection_set)

# Difference between two sets
difference_set = set1.difference(set2)
print(difference_set)

# Symmetric difference between two sets
symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)

# Check if set1 is a subset and set1 is a superset of set2
is_subset = set1.issubset(set2)
is_superset = set1.issuperset(set2)
print(is_subset, is_superset)
