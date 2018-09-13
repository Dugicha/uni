# Find all multiples of c between a and b
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

def first():
    op = 1 # operation count
    count = 0 # multiple count
    i = a
    while i <= b:
        op += 1
        if i % c == 0:
            count += 1
            #print(i)
        i += 1

    print("count: {}".format(count))
    print("op: {}".format(op))

def second():
    op = 2
    count = (b // c) - ((a - 1) // c)
    print("count: {}".format(count))
    print("op: {}".format(op))

print("FIRST:")
first()
print("SECOND:")
second()