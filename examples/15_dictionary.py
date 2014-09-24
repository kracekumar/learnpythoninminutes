months = {'jan': 31, 'feb': 28, 'mar': 31, 'apr': 30} # Colon is used to separate key and value

# `jan` is key and `31` is value
""" Visual representation of Dictionary
-----------
|Key|Value|
-----------
|jan|31   |
-----------
|feb|28   |
-----------
|mar|31   |
-----------
|apr|30   |
-----------
"""
print(months) # Dictionary don't maintain the order of insertion.
print(months['jan']) # Values in dictionary are accessed using key, in list index is used.
print(months.get('jan')) # .get returns None if the key is missing
print('dec' in months) # `in` is used to check presence of key in dictionary.
print(len(months)) # len function is used to find total key, value pair in dictionary.
for key, value in months.items(): # .items() returns two values during every iteration. First is key, second is value
    print(key, '->', value)
months['feb'] = 29 # Leap year! if key is already present value will be replaced else key, value pair will be added.
print(months)
months['dec'] = 31
print(months)
