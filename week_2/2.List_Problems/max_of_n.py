n = input("Enter count of numbers: ")
n = int(n)
max_number = 0
count = 1
while count <= n:
    number = input("Enter number: ")
    number = int(number)
    if max_number < number:
        max_number = number
    count += 1
print("The max is: {}" .format(max_number))