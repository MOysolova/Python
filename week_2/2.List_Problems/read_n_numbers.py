n = input("Enter count of numbers: ")
n = int(n)

def numbers(n):
    count = 1
    numbers = []
    while count <= n:
        number = input("Enter number: ")
        number = int(number)
        numbers = numbers + [number]
        count += 1
    return numbers
print(numbers(n))