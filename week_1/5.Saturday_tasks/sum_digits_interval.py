n = input("Enter N: ")
n = int(n)
m = input("Enter M: ")
m = int(m)
lower_bound = 0
upper_bound = 0

if n < m:
    lower_bound = n
    upper_bound = m
else:
    lower_bound = m
    upper_bound = n

start = lower_bound

while start <= upper_bound:
    n = start
    total_sum = 0
    while n != 0:
        digit = n % 10
        total_sum += digit
        n = n // 10

    print("Total sum of digits " + str(start) + " = " + str(total_sum))
    start += 1