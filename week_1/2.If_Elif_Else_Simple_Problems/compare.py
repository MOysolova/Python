a = input("Enter A: ")
b = input("Enter B: ")
a = int(a)
b = int(b)
if a == b:
    print("A ({}) is equal to B ({})".format(a, b))
elif a > b:
    print("A ({}) is bigger than B ({})".format(a, b))
elif b > a:
    print("B ({}) is bigger than A ({})".format(b, a))