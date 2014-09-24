def fxy(f, x, y): # f(x, y) = f(x) . f(y)
    return f(x) * f(y)

def square(x):
    return x * x

print(fxy(square, 2, 3))
