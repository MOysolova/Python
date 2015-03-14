n = input("Enter count of numbers: ")
n = int(n)

count = 1
numbers = []
while count <= n:
    number = input("Enter number: ")
    number = int(number)
    numbers += [number]
    count += 1

sum_numbers = 0
for number in numbers:
    sum_numbers += number
n = len(numbers)
average = sum_numbers / n
print("The average is: {}" .format(average))