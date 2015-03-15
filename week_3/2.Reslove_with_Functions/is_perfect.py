n = input("Enter a number N: ")
n = int(n)

def perfect(n):
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
    if sum_div == n:
        return True
    else:
        return False

print("Is this number perfect? " + str(perfect(n)))
