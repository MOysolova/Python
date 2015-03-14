n = input("Enter N: ")
n = int(n)
rev_number = 0
while n != 0:
    digit = n % 10
    rev_number = rev_number * 10 + digit
    n = n // 10
print("Reversed number: {}" .format(rev_number))