n = input("Write a number: ")
n = int(n)
sum = 0
while n != 0:
    digit = n % 10
    sum += digit
    print(digit)
    n = n // 10
print("The sum is: {}" .format(sum))