n = input("Enter a 3-digit number: ")
n = int(n)

a = n % 10
n = n // 10
b = n % 10
n = n // 10
c = n % 10
n = n // 10

largest = c
if b >= largest and b >= a:
    largest = b
if a >= largest and a >= b:
    largest = a

smallest = c
if b <= smallest and b <= a:
    smallest = b
if a <= smallest and a <= b:
    smallest = a
print("Smallest digit: " + str(smallest))
middle = a
if (largest == a and smallest == b) or (smallest == a and largest == b):
    middle = c
elif (largest == a and smallest == c) or (smallest == a and largest == c):
    middle = b

max_number = largest * 100 + middle * 10 + smallest
min_number = smallest * 100 + middle * 10 + largest

print("Max number with those digits is: {}" .format(max_number))
print("Min number with those digits is: {}" .format(min_number))