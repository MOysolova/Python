a = input("Enter A: ")
a = int(a)
b = input("Enter B: ")
b = int(b)
while a <= b:
    if a % 2 == 0:
        print(str(a) + " - even")
    else:
        print(str(a) + " - odd")
    a += 1
