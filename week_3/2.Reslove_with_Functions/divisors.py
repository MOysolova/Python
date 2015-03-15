n = input("Enter a number N: ")
n = int(n)

def devisors(n):
    start = 1
    list_div = []
    end = n - 1
    while start < end:
        if n % start == 0:
            list_div += [start]
        start += 1
    return list_div
print("Divisors are: " + str(devisors(n)))
