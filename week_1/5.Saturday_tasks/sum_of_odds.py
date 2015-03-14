n = input("Write a number: ")
n = int(n)
sum = 0
start = 1
while start <= n:
    if start % 2 == 1:
        sum += start
    start += 1
print(sum)