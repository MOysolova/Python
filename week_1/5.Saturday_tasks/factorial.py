n = input("Enter a number: ")
n = int(n)
def factoriel(n):
    start = 1
    total = 1
    while start <= n:
        total *= start
        start = start + 1
    return total
print(factoriel(n))
