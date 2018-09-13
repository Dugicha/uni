# Search a for v value and print index

def array_search(arr, value):
    # Iterate and compare
    for i, e in enumerate(a):
        if e == value:
            return i
    return None

# Input v
v = int(input("v: "))

# Generate random array
import random
a = [i for i in range(0, 100)]
random.shuffle(a)

ans = array_search(a, v)
if ans != None:
    print("v found at index {}".format(ans))
else:
    print("v not found")