n = input("Enter count of numbers: ")
n = int(n)

count = 1
numbers = []
lenght = 0
while count <= n:
    number = input("Enter number: ")
    number = int(number)
    count += 1
    if number % 2 == 0:
        numbers += [number]
        lenght += 1
print ("The number of evens: " + str(lenght))
for evens in numbers:
    print(evens)