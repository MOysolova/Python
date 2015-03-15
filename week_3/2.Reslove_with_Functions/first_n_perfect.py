n = input("Enter how many perfect numbers you want from me: ")
n = int(n)

def first_n_perfect(n):
    start = 6
    list_perfect = []
    while True:
        divisors_sum = 0
        divisor = 1
        while divisor < start:
            if start % divisor == 0:
                divisors_sum += divisor
            divisor += 1
        if divisors_sum == start:
            list_perfect += [start]
            n = n - 1
        if n == 0:
            break
        start += 1
    return list_perfect
print(first_n_perfect(n))
