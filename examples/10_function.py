def square(x): # No need to specify type of the argument.
    return x * x

def cube(x):
    return square(x) * x

def msg(): # Function with no arguments and doesn't return any value
    print("End")


print(square(2))
print(square(23))
msg()
