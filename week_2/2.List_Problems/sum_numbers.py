n = input("Enter count of numbers: ")
n = int(n)

count = 1
numbers = []
total_sum = 0
while count <= n:
    number = input("Enter number: ")
    number = int(number)
    count += 1
    total_sum += number
    numbers += [number]

print ("The total sum is: " + str(total_sum))
