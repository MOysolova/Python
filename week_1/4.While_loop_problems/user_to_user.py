a = input("Enter A: ")
a = int(a)
b = input("Enter B: ")
b = int(b)
if a < b:
    while a <= b:
        print(a)
        a += 1
elif a > b:
    while b <= a:
        print(b)
        b += 1
