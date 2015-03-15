n = input("Enter a number N: ")
n = int(n)

def sum_divisors(n):
    start = 1
    list_div = []
    end = n - 1
    sum_div = 0
    while start < end:
        if n % start == 0:
            list_div += [start]
        start += 1
    for index in list_div:
        sum_div += index
        index += 1
    return sum_div
print("Divisors sum are: " + str(sum_divisors(n)))
