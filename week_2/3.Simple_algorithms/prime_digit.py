n = input("Write a number: ")
n = int(n)
def prime_digit(n):
    list_digits = []
    list_primes = [2, 3, 5, 7]
    while n != 0:
        digit = n % 10
        list_digits += [digit]
        n = n // 10
    for digit in list_digits:
        if digit in list_primes:
            return ("At least one prime digit found")
            break
        return ("No prime digits found")
print(prime_digit(n))