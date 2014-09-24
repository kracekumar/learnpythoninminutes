try:
    l = [1, 2, 3]
    print(l[5])
except IndexError as e:
    print(e)

try:
    d = {'a': 1}
    print(d['b'])
except KeyError as e:
    print(e)

try:
    l = [1, 3, 3]
    d = {'a': 1}
    print(l[5], d['a'])
except (IndexError, KeyError) as e:
    print(e)
finally:
    print("end")
