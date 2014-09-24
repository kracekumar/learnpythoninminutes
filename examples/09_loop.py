for i in ['Python', 23, 45.9, True]: # During every iteration i value is replaced, `python` -> `23` -> `45.9` -> `True`
    print(i)

for ch in "Python":
    print(ch)

for number in range(0, 10): # Produces list of numbers starting from 0 til 9, 10 is excluded.
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")
