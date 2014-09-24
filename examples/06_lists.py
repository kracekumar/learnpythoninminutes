collection = ['Ruby', 23, 45.9, True] # Collection of different elements.
"""Representaion of list
       ---------------------------
       |'Ruby'| 23 | 45.9 | True|
       ---------------------------
        0        1      2      3

"""
print(collection)
# Access the first element
print(collection[0])
# Access the last element
print(collection[-1])
# Replace the first element
collection[0] = 'Python'
print(collection[0])
# Add an element at the last position
collection.append("last")
print(collection[-1])
# Insert an element at position 2
print(collection)
collection.insert(2, 12)
print(collection)
# Delete the last element
del collection[-1]
print(collection)
# Length of the list
print(len(collection))
