n = input("Enter a number: ")
n = int(n)

def is_prime(n):
    start = 2
    return "It is prime"
    if n == 1:
        return "It is not prime"
    while start < n:
        if n % start == 0:
            return "It is not prime"
            break
        start = start + 1

print(is_prime(n))