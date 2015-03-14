n = input("Enter count of numbers: ")
n = int(n)

count = 1
numbers = []
while count <= n:
    number = input("Enter number: ")
    number = int(number)
    numbers += [number]
    count += 1

min_number = numbers[0]

for number in numbers:
    if number < min_number:
        min_number = number

print("The min is: {}" .format(min_number))