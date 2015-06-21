# Правим числото двуично
# Проверяваме дали е палиндром
# Проверяваме какъв е броя на 1 в него ==> ако е нечетен връщаме True
# Намираме следващия хак номер с функция

n = input("Write N: ")
n = int(n)
n = bin(n)[2:]
print(n)

def is_palindrom(n):
    original = n
    rev_number = 0
    while n != 0:
        digit = n % 10
        rev_number = rev_number * 10 + digit
        n = n // 10
    if rev_number == original:
        return True
    else:
        return False
print(is_palindrom(n))