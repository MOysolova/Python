n = input("Write a number: ")
n = int(n)
def reverse_int(n):

    new_number = 0
    while n != 0:
        digit = n % 10
        new_number = new_number * 10 + digit
        n = n // 10
    return new_number
print(reverse_int(n))

def sum_digits(n):

    total_sum = 0
    while n != 0:
        digit = n % 10
        total_sum += digit
        n = n // 10
    return total_sum
print(sum_digits(n))

def product_digits(n):

    product_sum = 1
    while n != 0:
        digit = n % 10
        product_sum *= digit
        n = n // 10
    return product_sum
print(product_digits(n))