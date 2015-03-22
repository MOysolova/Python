numbers = [1, 2, 3, 4, 5]
def is_prime(n): #Тук проверяваме дали номерата са Prime
    start = 2
    is_prime = True
    while start < n:
        if n % start == 0:
            is_prime = False
            break
        start += 1
    return is_prime

def prime_pair(numbers):
    for x in numbers:
        for y in numbers:
            if is_prime(x + y):#Тук викаме горната функция
                return True

    return False

print(prime_pair(numbers))