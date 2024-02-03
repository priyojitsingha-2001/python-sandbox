# Enumerate function

# This is a simple Python script demonstrating the use of the enumerate function with the start parameter

def print_list_with_indices(my_list):
    """
    This function takes a list as input and prints each element along with its index.
    It starts the index from 1.
    """
    for index, value in enumerate(my_list, start=1):
        print(f"Index {index}: {value}")

# Example usage
my_colors = ['red', 'green', 'blue', 'yellow']

print("Printing list with indices starting from 1:")
print_list_with_indices(my_colors)
