n = input("Enter N: ")
n = int(n)
original = n
rev_number = 0
while n != 0:
    digit = n % 10
    rev_number = rev_number * 10 + digit
    n = n // 10

if rev_number == original:
    print("Is palindrom.")
else:
    print("Nope. The number is not palindrom.")