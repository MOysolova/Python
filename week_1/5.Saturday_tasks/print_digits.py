n = input("Write a number: ")
n = int(n)
while n != 0:
    digit = n % 10
    print(digit)
    n = n // 10